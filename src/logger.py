from colorful import color as cl
from colorful import printcl


def log(msg):
    printcl(msg)


def warn(WarnType, msg, tip):
    printcl(
        f"{cl.cyan}[{cl.yellow}Warn!{cl.cyan}]",
        f"{cl.yellow}{WarnType}: {cl.purple}{msg}"
    )
    printcl(tip)


def error(ErrorType, msg, tip):
    printcl(
        f"{cl.cyan}[{cl.red}Error!{cl.cyan}]",
        f"{cl.yellow}{ErrorType}: {cl.purple}{msg}"
    )
    printcl(tip)
