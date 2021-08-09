import os
import subprocess


def main(path):
    while True:
        inp = input()
        match inp:
            case "":
                inp = input()
                if inp == "":
                    subprocess.call("path")
            case _:
                write()


def write():
    pass


def setup():
    pass


if __name__ == '__main__':
    if setup():
        os.chmod('a', 0b111101101)
    main(os.path.abspath("methods/run.py"))
