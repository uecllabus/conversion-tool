import json


def parse_semester(s):
    if s == "通年":
        return 0
    elif s == "前学期":
        return 1
    elif s == "後学期":
        return 2
    raise ValueError(f"{s} is not a semester.")


class Syllabus:
    def __init__(self):
        self.data = {}

    def add(self, item):
        value = {
            "id": item[4],
            "lecturer": item[7],
            "periods": item[3].split(", "),
            "semester": parse_semester(item[2]),
            "title": item[5],
            "url": item[6]
        }
        self.data[value["id"]] = value

    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.data, f)
