from Config.const_values import (
    CONST_PATH_SETUP_TOOL_SRC,
)
from Payload.misc_functions import pre_format_string
from Config.static_data_type import translation_data_type

DATA: translation_data_type = [
    (f"{CONST_PATH_SETUP_TOOL_SRC}/extract.c", "utf-8", {
        "Extracting: ": "正在复制: ",
        "Progress: ": "进度: ",
        " of ": "，总计: "
    }, []),
    (f"{CONST_PATH_SETUP_TOOL_SRC}/main.c", "utf-8", {
        # Config.pszContent = (
        "- Process Hacker was renamed System Informer.\n": "- Process Hacker 已更名为 System Informer\n",
        "- Process Hacker does not support Windows 10 or 11.\n": "- Process Hacker 不支持 Windows 10/11\n",
        "- Process Hacker will not be updated.\n": "- Process Hacker 不会获得最新更新\n",
        "- Process Hacker will not be uninstalled.\n\n": "- Process Hacker 将不会被卸载\n\n",
        "This update will now install System Informer.\n\nPlease remember to uninstall Process Hacker. Thanks <3":
            "本次更新将安装 System Informer。\n\n建议在安装完成后卸载 Process Hacker。",
        # )
        "Initializing...": "正在初始化...",
        # PhShowInformation2 (
        "Process Hacker was renamed System Informer.\n": "Process Hacker 已更名为 System Informer\n",
        "The legacy version of Process Hacker is no longer maintained and will not receive updates.\r\n\r\n":
            "Process Hacker 已停止维护，不会再收到最新更新。\r\n\r\n",
        "The updater is now installing System Informer. The Process Hacker installation must be manually uninstalled":
            "更新程序正在安装 System Informer，Process Hacker 需用户手动卸载",
        # )
        "System Informer - Setup": "System Informer 安装程序",
    }, []),
    (f"{CONST_PATH_SETUP_TOOL_SRC}/startpage.c", "utf-8", {
        "Setup failed with an error.": "安装程序出现错误。",
        "%s\r\n\r\nSelect Close to exit setup.": pre_format_string("%s\r\n\r\n点击\"关闭\"退出安装程序"),
        "Select Close to exit setup.": pre_format_string("点击 \"关闭\" 退出安装程序"),
        "Install": "安装",
        "A free, powerful, multi-purpose tool that helps you monitor system resources, "
        "debug software and detect malware.":
            "一款免费、开源、功能强大、用途广泛的工具，可帮助您监控系统资源、调试软件和检测恶意软件。",
        " complete.": " 已完成",
        "Start program when setup exits": "启动 System Informer",
        "Installation Folder:\r\n\r\n%s": "安装目录: \r\n\r\n%s",
        "Browse": "浏览",
        "Next": "下一步",
        "Setup Options": "安装选项",
        pre_format_string("Installation Folder:\r\n\r\nSelect \"Browse\" to continue."):
            pre_format_string("安装目录: \r\n\r\n选择 \"浏览\" 以继续。"),
        "Change directory": "更改目录",
        "Continue": "继续",
        "WARNING": "警告",
        "The selected installation directory already contains files and data. ":
            "选定的安装目录已包含文件和数据。",
        "If you continue this directory and files will be deleted.\r\n\r\nDo you want to change the directory?":
            "如果继续操作，此目录及其中的文件将被删除。\r\n\r\n您要更改目录吗?",
        "Preparing to install...": "准备安装...",
    }, []),
    (f"{CONST_PATH_SETUP_TOOL_SRC}/uninstall.c", "utf-8", {
        "System Informer has been uninstalled.": "已卸载 System Informer。",
        "A reboot is required to complete the uninstall.": "卸载完成后需重启计算机。",
        "Click close to exit setup.": pre_format_string("单击 \"关闭\" 退出卸载程序。"),
        "Uninstalling System Informer...": "正在卸载 System Informer...",
        "Uninstall failed with an error.": "卸载过程中出现错误。",
        "Click retry to try again or close to exit setup.":
            pre_format_string("单击 \"重试\" 重新尝试卸载，或单击 \"关闭\" 退出卸载程序。"),
        "Uninstall": "卸载",
        "Are you sure you want to uninstall System Informer?": "您确定要卸载 System Informer 吗?",
        "Remove application settings": "删除应用程序配置",
    }, []),
    (f"{CONST_PATH_SETUP_TOOL_SRC}/update.c", "utf-8", {
        "Updating to version %lu.%lu.%lu.%lu...": "正在更新到版本 %lu.%lu.%lu.%lu...",
        "Update complete.": "更新完毕。",
        "Select Close to exit.": pre_format_string("单击 \"关闭\" 退出安装程序。"),
        "Retry": "重试",
        "Close": "关闭",
        "Error updating to the latest version.": "更新到最新版本时出错。",
    }, []),
    (f"{CONST_PATH_SETUP_TOOL_SRC}/version.rc", "utf-8", {
        "System Informer - Setup": "System Informer 安装程序",
        "Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved.":
        # xref: "{CONST_PATH_SYSTEM_INFORMER_SRC}/version.rc" above
            "版权所有 (c) Winsider Seminars & Solutions, Inc. 保留所有权利。"
    }, []),
]