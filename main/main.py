def main():
    while True:
        inp = input()
        match inp:
            case "":
                inp = input()
                if inp == "":
                    exec(open('methods/run.py').read())
                else:
                    main()
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
    main()
