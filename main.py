#!/usr/bin/env python3
import sys
import traceback
import tyusyutu


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
            html = read_file(arg)
            for item in tyusyutu.tyusyutu(html):
                print("yield:", item)
        except Exception:
            # 例外を表示、次のファイルを処理
            traceback.print_exc()
            status = 1
            print(arg, "cannot be converted.")

    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv))
