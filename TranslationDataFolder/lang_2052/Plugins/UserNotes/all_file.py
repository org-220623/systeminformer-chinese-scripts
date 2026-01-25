from Config.const_values import CONST_PATH_PLUGIN_USERNOTES
from Config.global_dict import GLOBAL_DICT
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_USERNOTES}/main.c", "utf-8", {
        "&User Notes": "用户备注(&U)",
        "Configure priority for executable...": "配置可执行文件优先级...",
        "Configure IO priority for executable...": "配置可执行文件 I/O 优先级...",
        "Configure page priority for executable...": "配置可执行文件页面优先级...",
        "Executable files (*.exe)": "可执行文件 (*.exe)",
        "All files (*.*)": "所有文件 (*.*)",
        "Unable to configure IFEO priority for this image.": "无法为此映像配置 IFEO 优先级。",
        "Unable to update the IFEO key for priority.": "无法更新 IFEO 优先级注册表键。",
        "Unknown": "未知", # PROCESS_PRIORITY_CLASS_UNKNOWN
        "Idle": "空闲", # PROCESS_PRIORITY_CLASS_IDLE
        "Normal": "正常", # PROCESS_PRIORITY_CLASS_NORMAL
        "High": "高", # PROCESS_PRIORITY_CLASS_HIGH
        "Realtime": "实时", # PROCESS_PRIORITY_CLASS_REALTIME
        "Below normal": "低于正常", # PROCESS_PRIORITY_CLASS_BELOW_NORMAL
        "Above normal": "高于正常", # PROCESS_PRIORITY_CLASS_ABOVE_NORMAL
        "Save": "保存",
        "Cancel": "取消",
        "Select the default process priority.": "选择默认进程优先级。",
        "The process priority will be applied by Windows even when System Informer isn't currently running. ": "即使 System Informer 当前未运行，Windows 也会应用进程优先级。",
        "Note: Realtime priority requires the User has the SeIncreaseBasePriorityPrivilege or the process running as Administrator.":
            "注意: 实时优先级要求用户拥有 SeIncreaseBasePriorityPrivilege 权限或进程以管理员身份运行。",
        "Very low": "非常低",
        "Very Low": "非常低",
        "Low": "低",
        "Medium": "中",
        "Select the default process IO priority.": "选择默认进程 I/O 优先级。",
        "The IO priority will be applied by Windows even when System Informer isn't currently running. ": "即使 System Informer 当前未运行，Windows 也会应用 I/O 优先级。",
        "Note: High IO priority requires the User has the SeIncreaseBasePriorityPrivilege or the process running as Administrator.":
            "注意：高 I/O 优先级要求用户拥有 SeIncreaseBasePriorityPrivilege 权限或进程以管理员身份运行。",
        "Select the default process page priority.": "选择默认进程页面优先级。",
        "The page priority will be applied by Windows even when System Informer isn't currently running.": "即使 System Informer 当前未运行，Windows 也会应用页面优先级。",
        "D3DKMT scheduling priority": "D3DKMT 调度优先级",
        "Select the graphics scheduling priority.": "选择图形调度优先级。",
        "Unable to update graphics scheduling priority": "无法更新图形调度优先级",
        "Unable to query graphics scheduling priority": "无法查询图形调度优先级",
        "Successfully deleted the IFEO key.": "已成功删除 IFEO 注册表项。",
        "Unable to update the IFEO for priority.": "无法更新优先级 IFEO 注册表项。",
        "Unable to update the IFEO for IO priority.": "无法更新 I/O 优先级 IFEO 注册表项。",
        "Unable to update the IFEO for page priority.": "无法更新页面优先级 IFEO 注册表项。",
        "Unable to query priority.": "无法查询优先级。",
        "Unable to query IO priority.": "无法查询 I/O 优先级。",
        "Unable to query the current affinity.": "无法查询当前处理器相关性信息。",
        "This process has multi-group affinity, %s": "该进程具有多处理器组的处理器相关性, %s",
        "you can only change affinity for individual threads.": "您只能更改单个线程的处理器相关性。",
        "Unable to query process affinity.": "无法查询进程处理器相关性。",
        "Unable to query page priority.": "无法查询页面优先级。",
        "Unable to query process boost.": "无法查询进程提升信息。",
        "Unable to query process efficiency mode.": "无法查询进程节能模式信息。",
        "&Affinity": "处理器相关性(&A)",
        "Set &affinity": "设置处理器相关性(&A)",
        "&Save for %s": "保存 %s 信息(&S)",
        "Save &for this command line": "保存此命令行信息(&F)",
        "&Boost": "提升(&B)",
        "Set &boost": "设置提升(&B)",
        "&Efficiency": "节能(&E)",
        "Set &efficiency mode": "设置节能模式(&E)",
        "&Save for %s (IFEO)": "保存 %s IFEO 信息(&S)",
        "Col&lapse by default": "默认折叠(&L)",
        "Highligh&t": "高亮显示(&T)",
        "Graphics priority...": "图形优先级...",
        "Comment": "注释",
        "Affinity": "相关性", # todo 确定宽度 是否能容纳 处理器相关性
        "User Notes": "用户备注",
        "Allows the user to add comments for processes and services,": "允许用户为进程和服务添加注释，",
        " save process priority and affinity, highlight individual processes and show processes collapsed by default.":
            "保存进程优先级和关联性，高亮显示单个进程，并默认折叠显示进程。",
    }, [
        ('''optionsEntry->CreateSection(
        L"UserNotes"''', '''optionsEntry->CreateSection(
        L"用户备注"'''),
    ]),
    (f"{CONST_PATH_PLUGIN_USERNOTES}/options.c", "utf-8", {
        "Service": "服务",
        "Commandline": "命令行",
        "True": "是",
        "False": "否",
        "Name": "名称",
        "Comment": "注释",
        "Priority": "优先级",
        "IO priority": "I/O 优先级",
        "BackColor": "背景色",
        "Collapse": "折叠",
        "Affinity": "相关性",
        "Page priority": "页面优先级",
        "Efficiency": "节能",
        "&Delete": "删除(&D)",
        "&Copy": "复制(&C)",
    }, [
        ('PhSetListViewSubItem(Context->ListViewHandle, lvItemIndex, 1, L"File"', 'PhSetListViewSubItem(Context->ListViewHandle, lvItemIndex, 1, L"文件"'),
        ('PhAddListViewColumn(listview, 1, 1, 1, LVCFMT_LEFT, 100, L"Type"', 'PhAddListViewColumn(listview, 1, 1, 1, LVCFMT_LEFT, 100, L"类型"'),
    ]),
    (f"{CONST_PATH_PLUGIN_USERNOTES}/prpcmpage.c", "utf-8", {
        "Comment": "注释",
    }, [
        (r'''L"Do you want to replace the comment for %s which is currently\n    \"%s\"\n"
                        L"with\n    \"%s\"?"''', r'''L"你是否要替换 %s 的注释?\n原注释:\n    \"%s\"\n"
                        L"新注释:\n    \"%s\"?"''')
    ]),
    (f"{CONST_PATH_PLUGIN_USERNOTES}/UserNotes.rc", "utf-8", {
        "Options": "选项",
        "Collapse services on start": "启动时折叠服务",
        "Current database configuration values:": "当前数据库配置值:",
        "Comment": "注释",
        "Revert": "还原",
        "Only for processes with the same command line": "仅用于命令行参数相同的进程",
    }, []),
    (f"{CONST_PATH_PLUGIN_USERNOTES}/version.rc", "utf-8", {
"Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved.":
            GLOBAL_DICT["Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved."],
    }, []),
]