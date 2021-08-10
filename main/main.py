import os


def main():
    while True:
        inp = input()
        match inp:
            case "":
                inp = input()
                if inp == "":
                    exec(open('methods/run.py').read())
            case _:
                write(inp)


def write(arg):
    with open("methods/run.py", "a") as file:
        file.write(f"{arg}\n")


def setup():
    with open("main/setup.txt", "r") as text:
        if text.read() == "":
            return True
        else:
            return False


if __name__ == '__main__':
    if setup():
        os.chmod('methods/run.py', 0b111101101)
    main()
