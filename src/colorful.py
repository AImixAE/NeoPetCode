class Colors:
    reset = "\033[0m"


color = Colors()


def clcolor():
    print(color.reset, end="")


def printcl(*args, end="\n", sep=" "):
    clcolor()

    for i in args:
        print(i, end=sep)

        clcolor()

    print(end, end="")


def printls(*args, end="\n", sep=" "):
    clcolor()

    for i in args:
        for v in i:
            print(i, end=sep)

            clcolor()

    print(end, end="")
