#!/usr/bin/env python3
import os.path
import sys
import traceback

from syllabus import Syllabus
from tyusyutu import tyusyutu


def read_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read()


def main(args):
    # 引数チェック
    if len(args) < 2:
        print("Usage:", args[0], "files...")
        return 2

    # 各ファイルを処理
    status = 0
    for arg in args[1:]:
        try:
            # 各科目を取得
            syl = Syllabus()
            html = read_file(arg)
            for item in tyusyutu(html):
                syl.add(item)

            # JSONで保存
            out = os.path.splitext(arg)[0] + ".json"
            syl.save(out)
            print(f"{arg}: converted as \"{out}\".")
        except Exception:
            # 例外を表示、次のファイルを処理
            traceback.print_exc()
            status = 1
            print(f"{arg}: failed to convert.")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv))
