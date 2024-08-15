from locales.colors import color


def clcolor():
    print(color.reset, end="")


def printcl(*args, end="\n", sep=" "):
    clcolor()

    for index, i in enumerate(args):
        print(i, end="" if index == len(args) - 1 else sep)

        clcolor()

    print(end, end="")


def printls(*args, end="\n", sep="\n"):
    clcolor()

    for index_outer, i in enumerate(args):
        for index_inner, v in enumerate(i):
            print(v, end="" if index_inner == len(i) - 1 else sep)

            clcolor()

        # 在外层循环的每个列表之后打印 end，但最后一个列表除外
        # if index_outer != len(args) - 1:
        #     print(end, end="")

    print(end, end="")
