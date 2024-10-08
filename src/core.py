from colorful import printcl, printls
from colorful import color as cl

from logger import warn

from locales.zh_CN import lang    # 导入语言的方式先做这一个()
from locales.default import lang as dlang

from Commands_group import Cgp


class NeoPetCode(object):
    def __init__(self, argv: list[str], argc: int, baseapp: dict):
        self.argv = argv
        self.argc = argc

        self.count = 0
        self.arg = ""

        self.baseapp = baseapp

        self.app = {
            "name": "NeoPetCode",
            "version": "Dev Alpha v0.0.1"
        }

        self.cgp = Cgp(argv=argv, argc=argc, app=self.app, baseapp=baseapp)

    def CheckArgs(self):
        if self.argc > 1:
            RunCommand: bool = False  # 是否运行指令
            RunOption: bool = True   # 是否运行选项

            for i in range(1, self.argc):   # 遍历参整
                self.arg = self.argv[i]  # 获取当前参数
                self.count = i

                self.cgp.update_arg(self.arg)
                self.cgp.update_count(i)

                # 我知道下面这段代码你可能很懵 但你先别懵
                # 因为我更懵

                # 你不得看看是选项是指令啊(bushi)
                RunOption, RunCommand = (True, False) if (
                    RunOption and   # 如果要匹配选项
                    "-" in self.arg     # 选项里指定会包含 "-"
                ) else (False, True)  # 不然更改规则

                if RunOption:     # 如果运行选项
                    match self.arg:   # 匹配规则
                        case "-h" | "--help":
                            self.cgp.HelpDoc(IsCommand=False)

                            exit()

                        case "--icon":
                            self.cgp.icon()

                            # exit()
                            print()

                        case _:
                            warnmsg = lang["warn"]["optionwarn"]
                            warn("OptionWarn", warnmsg[0], warnmsg[1])

                            if "-" not in self.arg:
                                print()
                                printls(warnmsg[2])

                if RunCommand:    # 如果要运行命令
                    match self.arg:   # 匹配规则
                        case "h" | "help":
                            self.cgp.HelpDoc(IsCommand=True)

                            exit()

                        case _:
                            warnmsg = lang["warn"]["commandwarn"]
                            warn("CommandWarn", warnmsg[0], warnmsg[1])

            # 全是什么规则给我都干懵了

        else:
            warnmsg = lang["warn"]["argumentwarn"]
            warn("ArgumentWarn", warnmsg[0], warnmsg[1])

    def run(self):
        printcl(f"{cl.cyan}{self.app['name']}")
        printcl(f"{cl.purple}{self.app['version']}")
        print()

        self.CheckArgs()
