#!python3
import sys
import core


argv: list[str] = sys.argv
argc: int = len(argv)


class BaseApp(object):
    def __init__(self, CoreClass):
        self.baseapp = {
            "base_version": "Dev Alpha v0.0.1"
        }

        self.CoreClass = CoreClass

    def run(self):
        corec = self.CoreClass(argv=argv, argc=argc, baseapp=self.baseapp)

        corec.run()


if __name__ == "__main__":
    baseapp = BaseApp(core.NeoPetCode)

    baseapp.run()
