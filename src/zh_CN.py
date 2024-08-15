from .colors import color as cl


lang = {
    "help_doc": {
        "default": [
            f"- {cl.cyan}Help Doc{cl.reset} -",
            f"一款{cl.bold}项目部署{cl.reset}工具",
            "",
            f"{cl.green}使用: {cl.purple}npcode {cl.blue}[选项] [命令] [参数]",
            "",
            f"{cl.green}选项: ",
            f"  {cl.cyan}-h{cl.reset}, {cl.cyan}--help\t\t{cl.reset}查看帮助文档",
            f"      {cl.cyan}--icon\t\t{cl.reset}输出炫彩图标",
            "",
            f"{cl.green}指令:",
            f"  {cl.cyan}h{cl.reset}, {cl.cyan}help\t\t{cl.reset}查看某一指令的帮助文档"
        ]
    },

    "warn": {
        "commanderror": ["不支持的命令", f"尝试一下 {cl.purple}npcode {cl.blue}--help {cl.reset}?"]
    }
}
