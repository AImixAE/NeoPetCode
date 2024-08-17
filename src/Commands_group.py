from colorful import color as cl
from colorful import printls, printcl

from logger import warn

from locales.zh_CN import lang    # 导入语言的方式先做这一个()
from locales.default import lang as dlang


class Cgp(object):
    def __init__(self, argv: list, argc: int, app: dict, baseapp: dict):
        self.argv, self.argc = argv, argc

        self.app, self.baseapp = app, baseapp

        self.count, self.arg = 0, ""

    def update_count(self, c: int):
        self.count = c

    def update_arg(self, a: str):
        self.arg = a

    def HelpDoc(self):
        pass

    def icon(self):
        printls(dlang["icon"])

    def HelpDoc(
        self,
        IsCommand: bool = False  # 是否是指令(对查找有用)
    ):
        if IsCommand:
            if self.count + 1 < self.argc:
                match self.argv[self.count + 1]:
                    case "help":
                        pass

            else:
                printls(lang["help_doc"]["default"])

        else:
            if self.count + 1 < self.argc and "-" in self.argv[self.count + 1]:
                match self.argv[self.count + 1]:
                    case "-a" | "--all":
                        printls(lang["help_doc"]["default"])

                    case _:
                        warnmsg = lang["warn"]["invalidoptionwarn"]
                        warn("InvalidOptionWarn", warnmsg[0], warnmsg[1])

                        print()
                        printls(warnmsg[2])

            else:
                printls(lang["help_doc"]["default"])
