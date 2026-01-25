from Config.const_values import CONST_PATH_PLUGIN_EXTENDEDNOTIFICATIONS
from Config.global_dict import GLOBAL_DICT
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_EXTENDEDNOTIFICATIONS}/ExtendedNotifications.rc", "utf-8", {
        "Processes": "进程",
        "You can configure processes for which notifications are displayed. Wildcards can be used, and ordering is considered.":
            "您可以配置要显示通知的进程。支持使用通配符，并支持配置顺序。",
        "Move up": "上移",
        "Move down": "下移",
        "Include": "包含",
        "Exclude": "排除",
        "Add/Update": "添加/更新",
        "Remove": "移除",
        r"Examples:\nnote*.exe\nC:\\Windows\\system32\\cmd.exe\nC:\\Windows\\*":
            r"示例:\nnote*.exe\nC:\\Windows\\system32\\cmd.exe\nC:\\Windows\\*",
        "Services": "服务",
        "You can configure services for which notifications are displayed. Wildcards can be used, and ordering is considered.":
            "您可以配置要显示通知的服务。支持使用通配符，并支持配置顺序。",
        r"Examples:\nWdi*\nseclogon": r"示例:\nWdi*\nseclogon",
        "Devices": "设备",
        "You can configure devices for which notifications are displayed. Wildcards can be used, and ordering is considered.":
            "您可以配置要显示通知的设备。支持使用通配符，并支持配置顺序。",
        r"Examples:\nUSB*\n*Keyboard*": r"示例:\nUSB*\n*Keyboard*",
        "Logging": "日志",
        "Log all events to this file (leave blank to disable this feature):": "将所有事件记录到此文件 (留空可禁用此功能):",
        "Browse...": "选择...",
        "Changes will require a restart of System Informer.": "更改需要重启 System Informer。",
    }, [
        ('"File",IDC_INFO', '"文件",IDC_INFO'),
    ]),
    (f"{CONST_PATH_PLUGIN_EXTENDEDNOTIFICATIONS}/main.c", "utf-8", {
        "Extended Notifications": "通知扩展",
        "Filters notifications.": "提供筛选通知事件功能。",
        "Notifications - Processes": "通知 - 进程",
        "Notifications - Services": "通知 - 服务",
        "Notifications - Devices": "通知 - 设备",
        "Notifications - Logging": "通知 - 日志",
        "[Include] ": "[包含] ",
        "[Exclude] ": "[排除] ",
        "Log files (*.txt;*.log)": "日志文件 (*.txt;*.log)",
        "All files (*.*)": "所有文件 (*.*)",
    }, []),
    (f"{CONST_PATH_PLUGIN_EXTENDEDNOTIFICATIONS}/version.rc", "utf-8", {
        "Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved.":
            GLOBAL_DICT["Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved."],
    }, []),
]