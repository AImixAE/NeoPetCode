from colorful import printcl, printls
from colorful import color as cl

from locales.zh_CN import lang    # 导入语言的方式先做这一个()
from locales.default import lang as dlang


class NeoPetCode(object):
    def __init__(self, argv: list[str], argc: int, baseapp: dict):
        self.argv = argv
        self.argc = argc

        self.baseapp = baseapp

        self.app = {
            "name": "NeoPetCode",
            "version": "Dev Alpha v0.0.1"
        }

    def Cgp_icon(self):
        printls(dlang["icon"])

    def Cgp_HelpDoc(
        self,
        count: int,             # 当前遍历的参整
        IsCommand: bool = False  # 是否是指令(对查找有用)
    ):
        if IsCommand:
            if count + 1 < self.argc:
                match self.argv[count + 1]:
                    case "help":
                        pass

            else:
                printls(lang["help_doc"]["default"])

        else:
            if count + 1 < self.argc and "-" in self.argv[count]:
                pass

            else:
                printls(lang["help_doc"]["default"])

    def CheckArgs(self):
        RunCommand: bool = False  # 是否运行指令
        RunOption: bool = True   # 是否运行选项

        for i in range(1, self.argc):   # 遍历参整
            cnow = self.argv[i]  # 获取当前参数

            # 我知道下面这段代码你可能很懵 但你先别懵
            # 因为我更懵

            # 你不得看看是选项是指令啊(bushi)
            RunOption, RunCommand = (True, False) if (
                RunOption and   # 如果要匹配选项
                "-" in cnow     # 选项里指定会包含 "-"
            ) else (False, True)  # 不然更改规则

            if RunOption:     # 如果运行选项
                match cnow:   # 匹配规则
                    case "-h" | "--help":
                        self.Cgp_HelpDoc(
                            IsCommand=False, count=i)

                        exit()

                    case "--icon":
                        self.Cgp_icon()

                        # exit()
                        print()

            if RunCommand:    # 如果要运行命令
                match cnow:   # 匹配规则
                    case "help":
                        self.Cgp_HelpDoc(
                            IsCommand=True, count=i)

                        exit()

        # 全是什么规则给我都干懵了

    def run(self):
        printcl(f"{cl.cyan}{self.app['name']}")
        printcl(f"{cl.purple}{self.app['version']}")
        print()

        self.CheckArgs()
