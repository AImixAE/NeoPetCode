from colorful import printcl
from colorful import color as cl

from locales import zh_CN as lang    # 导入语言的方式先做这一个()


class NeoPetCode(object):
    def __init__(self, argv: list[str], argc: int, baseapp: dict):
        self.argv = argv
        self.argc = argc

        self.baseapp = baseapp

        self.app = {
            "name": "NeoPetCode",
            "version": "Dev Alpha v0.0.1"
        }

    def Cgp_HelpDoc(self, count: int, ShowAll: bool = False, IsCommand: bool = False):
        if IsCommand and (count + 1 < self.argc):
            pass

        else:
            printcl(lang.help_doc)

    def CheckArgs(self):
        RunCommand: bool = False  # 是否运行指令
        RunOption : bool = True   # 是否运行选项

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
                        self.Cgp_HelpDoc(ShowAll=False, IsCommand=False, count=i)

            if RunCommand:    # 如果要运行命令
                match cnow:   # 匹配规则
                    case "help":
                        self.Cgp_HelpDoc(ShowAll=False, IsCommand=True, count=i)

        # 全是什么规则给我都干懵了

    def run(self):
        printcl(f"{cl.cyan}{self.app['name']}")
        printcl(f"{cl.purple}{self.app['version']}")
        print()

        self.CheckArgs()
