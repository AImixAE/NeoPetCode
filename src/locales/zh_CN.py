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
        "commandwarn": [
            "不支持的命令",
            f"尝试一下 {cl.purple}npcode {cl.blue}--help {cl.reset}?"
        ],

        "argumentwarn": [
            "未输入参数",
            f"尝试一下 {cl.purple}npcode {cl.blue}--help {cl.reset}?"
        ],

        "optionwarn": [
            "选项错误",
            f"尝试一下 {cl.purple}npcode {cl.blue}--help {cl.reset}?",

            [
                "也有可能是程序错误",
                "如果你确认你输入的在程序的支持范围内, ",
                "请在 github 上提交 Issue"
            ]
        ],

        "invalidoptionwarn": [
            "无效的帮助选项",
            f"尝试一下 {cl.purple}npcode {cl.blue}help {cl.reset}?",

            [
                "一般使用help选项模式时不支持在后一参数输入其他内容",
                "如果真的需要, 请使用命令模式"
            ]
        ]
    }
}
