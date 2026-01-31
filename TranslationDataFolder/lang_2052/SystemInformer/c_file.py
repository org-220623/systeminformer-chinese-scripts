# 本文件存储 System Informer 源码汉化数据。
# 作者: anonymous9075 (anonymous9075331734@proton.me)

from Config.const_values import CONST_PATH_SYSTEM_INFORMER_SRC
from Config.global_dict import GLOBAL_DICT
from Config.static_data_type import TranslationDataType, EnumTranslateSecurityEditorMandatoryLevel
from Config.patch_options import OPTION_TRANSLATE_SECURITY_EDITOR_MANDATORY_LEVEL
from Payload.misc_functions import pre_format_string

DATA: TranslationDataType = [
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mdump.c", "utf-8", {       # File complete.
        "Dump files (*.dmp)": "转储文件 (*.dmp)", 
        "All files (*.*)": "所有文件 (*.*)", 
        "Unable to open the process": "无法打开进程", 
        "Unable to access the dump file": "无法访问转储文件", 
        "Processing module ": "正在处理模块 ", 
        "Processing thread ": "正在处理线程 ", 
        "Processing memory regions": "正在处理内存区域", 
        "Processing kernel minidump": "正在处理内核小型转储文件", 
        "The 32-bit version of System Informer could not be located.":
            "找不到 32 位版本的 System Informer。", 
        "A 64-bit dump will be created instead. Do you want to continue?":
            "将改为创建 64 位转储文件。是否继续?",
        "Unable to create kernel minidump.": 
            "无法创建内核小型转储文件。", 
        "Kernel minidump of processes require administrative privileges. ": 
            "进程内核小型转储文件需要管理员权限。", 
        "Make sure System Informer is running with administrative privileges.":
            "请确保 System Informer 以管理员权限运行。", 
        "Creating the dump file...": "正在创建转储文件...", 
        "Unable to create the minidump": "无法创建小型转储文件", 
        "Unable to create the minidump.": "无法创建小型转储文件。", 
        "Unknown error.": "未知错误。", 
        "Cancelling...": "正在取消...", 
        "Creating the minidump file...": "正在创建小型转储文件...", 
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/about.c", "utf-8", {
        "Thanks to:\n": "鸣谢: \n",
        pre_format_string("    <a href=\"https://github.com/winsiderss/systeminformer/graphs/contributors\">Contributors</a> - thank you for your additions!\n"):
            pre_format_string("    感谢各位<a href=\"https://github.com/winsiderss/systeminformer/graphs/contributors\">贡献者</a>对本项目的付出!\n"),
        "    Donors - thank you for your support!\n\n": "    感谢各位捐赠者对本项目的支持!\n\n",
        pre_format_string("    <a href=\"https://github.com/GameTechDev/PresentMon\">PresentMon</a> by Intel Corporation\n"):
            pre_format_string("    <a href=\"https://github.com/GameTechDev/PresentMon\">PresentMon</a> - Intel 公司\n"),
        pre_format_string("    <a href=\"https://github.com/michaelrsweet/mxml\">Mini-XML</a> by Michael Sweet\n"):
            pre_format_string("    <a href=\"https://github.com/michaelrsweet/mxml\">Mini-XML</a> - Michael Sweet\n"),
        pre_format_string("    <a href=\"https://github.com/PCRE2Project/pcre2\">PCRE2</a> by Philip Hazel\n"):
            pre_format_string("    <a href=\"https://github.com/PCRE2Project/pcre2\">PCRE2</a> - Philip Hazel\n"),
        pre_format_string("    <a href=\"https://github.com/json-c/json-c\">json-c</a> by Michael Clark\n"):
            pre_format_string("    <a href=\"https://github.com/json-c/json-c\">json-c</a> - Michael Clark\n"),
        "    MD5 code by Jouni Malinen\n": "    Jouni Malinen 编写的 MD5 编码\n",
        "    SHA1 code by Filip Navara, based on code by Steve Reid\n":
            "    Filip Navara 编写的 SHA1 编码，基于 Steve Reid 的代码\n",
        "System Informer uses the following components:\n":
            "System Informer 使用以下组件:\n",
        "OBJECT INFORMATION\r\n": "对象信息\r\n",           # todo: 为什么大写？
        ": %lu objects\r\n": ": %lu 个对象\r\n",
        "STATISTIC INFORMATION\r\n": "统计数据信息\r\n",      # todo: 为什么大写？
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/actions.c", "utf-8", {
        "Continue": "继续",
        "Do you want to ": "您确定要",
        "You will need to provide administrator permission. ": "您需要提供管理员权限。 ",
        "Click Continue to complete this operation.": pre_format_string("点击\"继续\"完成此操作。"),
        "Unable to lock the computer.": "无法锁定计算机。",
        "Unable to log off the computer.": "无法注销计算机。",
        "Unable to sleep the computer.": "无法使计算机进入睡眠状态。",
        "Unable to hibernate the computer.": "无法使计算机进入休眠状态。",
        "Unable to restart the computer.": "无法重启计算机。",
        "Unable to configure the advanced boot options.": "无法配置高级启动选项。",
        "Unable to restart to firmware options.": "无法重启进入固件选项。",
        "Make sure System Informer is running with administrative privileges.":
            "请确保 System Informer 以管理员权限运行。",
        "This machine does not have UEFI support.": "该计算机不支持 UEFI。",
        "Unable to shut down the computer.": "无法关闭计算机",
        "shut down": "关闭",
        "the computer": "计算机",
        "restart": "重启",
        "update and restart": "更新并重启",
        "the computer for Windows Defender Offline Scan": "计算机以进行 Windows Defender 离线扫描",
        "update and shutdown": "更新并关闭",
        "Restart to boot application": "重启至启动菜单程序",
        "Restart to firmware application": "重启至固件程序",
        "Unable to configure the boot application.": "无法配置启动程序。",
        "&Connect": "连接(&C)",
        "&Disconnect": "断开(&D)",
        "&Logoff": "注销(&L)",
        "Rem&ote control": "远程控制(&O)",
        "Send &message...": "发送消息(&M)...",
        "P&roperties": "属性(&R)",
        "Connect to session": "连接至会话",
        "Password:": "密码:",
        "Unable to connect to the session": "无法连接至会话",
        "Unable to disconnect the session": "无法断开与会话的连接",
        "logoff": "注销",
        "the user": "用户账户",
        "Unable to logoff the session": "无法注销会话",
        " and ": " 和 ",
        "the selected processes": "已选中的进程",
        "You are about to ": "您即将",
        " one or more system processes.": "一个或多个系统进程。",
        "terminate": "结束",
        " one or more critical processes. This will shut down the operating system immediately.":
            "一个或多个关键进程，这将立即关闭操作系统。",
        " one or more critical processes.": "一个或多个关键进程。",
        "Unable to %s %s (PID %lu)": "无法%s %s (PID %lu)",
        "Unable to %s %s": "无法%s %s",
        "Terminating a process will cause unsaved data to be lost.":
            "结束进程会导致未保存的数据丢失。",
        "Unable to terminate ": "无法结束 ",
        " and its descendants": " 及其子进程吗",
        "Terminating a process tree will cause the process and its descendants to be terminated.":
            "结束进程树将导致该进程及其所有子进程被终止。",
        "Unable to enumerate processes": "无法枚举进程",
        "suspend": "挂起",
        "Unable to suspend ": "无法挂起 ",
        "Suspending a process tree will cause the process and its descendants to be suspend.":
            "挂起进程树将导致该进程及其所有子进程都被挂起。",
        "resume": "恢复",
        "Unable to resume ": "无法恢复 ",
        "Resuming a process tree will cause the process and its descendants to be resumed.":
            "恢复进程树将导致该进程及其子进程恢复运行。",
        "freeze": "冻结",
        "Freezing does not persist after exiting System Informer.":
            "退出 System Informer 后，冻结过程会终止。",
        "thaw": "解冻",
        "debug": "调试",
        "Debugging a process may result in loss of data.": "调试进程可能会导致数据丢失。",
        # todo: line 2767
        "Unable to locate the debugger.": "无法定位调试器。",
        "reduce the working set of": "减少以下进程的工作集占用: ",
        "empty the working set of": "清空以下进程的工作集占用: ",
        # static CONST TASKDIALOG_BUTTON TaskDialogRadioButtonArray[] =
        # {
            # SystemActivityModerationStateSystemManaged
            "System managed": "系统托管",
            # SystemActivityModerationStateUserManagedAllowThrottling
            "Allow activity moderation throttling": "启用活动调节限制",
            # SystemActivityModerationStateUserManagedDisableThrottling
            "Disable activity moderation throttling": "禁用活动调节限制",
        # }
        # static CONST TASKDIALOG_BUTTON TaskDialogButtonArray[] =
        # {
            "Save": "保存",       # IDYES
            "Cancel": "取消",     # IDCANCEL
        # }
        "Select the process activity moderation throttling state.":
            "选择进程活动调节节流状态。",
        "System-managed activity moderation settings are automatically removed by Windows when the executable is "
            "deleted or was last executed more than 7 days ago.\r\n\r\n":
            "当可执行文件被删除或上次执行时间超过 7 天时，Windows 会自动移除系统管理的活动审核设置。\r\n\r\n",
        "Image: %s\r\nUpdated: %s": "映像: %s\r\n已更新: %s",
        "%s ago (%s)": "%s 以前 (%s)",
        "set background activity moderation for": "为以下进程设置后台活动调节: ",
        "set virtualization for": "为以下进程启用虚拟化: ",
        "set critical status for": "为以下进程启用关键状态: ",
        "set Eco mode for": "为以下进程启用节能模式: ",
        "create execution required state for": "为以下进程创建执行所需状态",
        "Unable to detach the debugger.": "无法断开与调试器的连接。",
        "The process is not being debugged.": "该进程未进行调试。",
        "detach debugger from": "断开调试器与以下进程的连接",
        "DLL files (*.dll)": "DLL 文件 (*.dll)",
        "All files (*.*)": "所有文件 (*.*)",
        "load the DLL into": "加载 DLL 至以下进程: ",
        "Unable to set the I/O priority of ": "无法为以下进程设置 I/O 优先级: ",
        "set the I/O priority of": "为以下进程设置 I/O 优先级: ",
        "set the page priority of": "为以下进程设置页面优先级: ",
        "Unable to set the priority class of ": "无法为以下进程设置优先级类: ",
        "set the priority class of": "为以下进程设置优先级类: ",
        "change boost priority of": "为以下进程更改优先级提升值: ",
        "set the boost priority of": "为以下进程设置优先级提升值: ",
        "the selected service": "已选中的服务",
        "the selected services": "已选中的服务",
        "Close": "关闭",
        "Unable to %s services:": "无法%s服务:",
        "Attempting to ": "正在尝试",
        " Are you sure you want to continue?": "您确定要继续吗?",
        "Initializing...": "初始化中...",
        "Unable to %s %s.": "无法%s %s。",
        "Unable to start ": "无法启动 ",
        "Unable to continue ": "无法继续运行 ",
        "Unable to pause ": "无法挂起 ",
        "Unable to stop ": "无法停止 ",
        "Unable to delete ": "无法删除 ",
        "Restarting a service might prevent the system from functioning properly.":
            "重启服务可能会导致系统无法正常运行。",
        "Unable to restart ": "无法重启 ",
        "Unable to close the TCP connection": "无法关闭 TCP 连接",
        "Unable to close the TCP connection.": "无法关闭 TCP 连接",
        "the selected thread": "已选中的线程",
        "the selected threads": "已选中的线程",
        "Unable to %s thread %lu": "无法%s线程 %lu",
        "Terminating a thread may cause the process to stop working.":
            "结束线程可能会导致进程停止运行。",
        "Unable to terminate thread %lu": "无法结束线程 %lu",
        "Unable to suspend thread %lu": "无法挂起线程 %lu",
        "Unable to resume thread %lu": "无法恢复线程 %lu",
        "Unable to set the I/O priority of thread %lu": "无法设置线程 %lu 的 I/O 优先级",
        "unload": "卸载",
        "Unloading a module may cause the process to crash.":
            "卸载模块可能会导致进程崩溃。",
        "Unloading a module may cause the process to crash. "
            "NOTE: This feature may not work correctly on your "
                "version of Windows and some programs may restrict "
                "access or ban your account.":
            "卸载模块可能会导致进程崩溃。注意: 此功能可能无法在您的 Windows "
            "版本上正常运行，某些程序可能会限制访问或封禁您的帐户。",
        "Unloading a driver may cause system instability.":
            "卸载驱动程序可能会导致系统不稳定。",
        "unmap": "取消映射",
        "Unmapping a section view may cause the process to crash.":
            "取消映射节区视图可能会导致进程崩溃。",
        "Unable to unload the module": "无法卸载模块",
        "Unable to unload ": "无法卸载 ",
        "Unable to unmap the section view at 0x%p": "无法取消映射 0x%p 处的节区视图",
        "Freeing memory regions may cause the process to crash.\r\n\r\n"
            "Some programs may also restrict access or ban your account when "
                "freeing the memory of the process.":
            "释放内存区域可能会导致进程崩溃。\r\n\r\n"
            "某些程序在释放进程内存时也可能会限制访问或封禁您的帐户。",
        "decommit": "撤销提交",
        "Decommitting memory regions may cause the process to crash.\r\n\r\n"
            "Some programs may also restrict access or ban your account when "
                "decommitting the memory of the process.":
            "撤销提交内存区域可能会导致进程崩溃。\r\n\r\n"
            "某些程序在撤销提交进程内存时也可能会限制访问或封禁您的帐户。",
        "Unmapping a section view may cause the process to crash.\r\n\r\n"
            "Some programs may also restrict access or ban your account when "
                "unmapping the memory of the process.":
            "取消映射节区视图可能会导致进程崩溃。\r\n\r\n"
            "某些程序在取消映射进程内存时也可能会限制访问或封禁您的帐户。",
        "the memory region": "内存区域",
        "Unable to free the memory region": "无法释放内存区域",
        "Unable to decommit the memory region": "无法撤销提交内存区域",
        "Unable to unmap the section view": "无法取消映射节区视图",
        "Unable to empty the region working set.": "无法清空内存区域工作集。",
        pre_format_string("Unable to %s handle \"%s\" (%s)%s"): pre_format_string("无法%s句柄 \"%s\" (%s)%s"),
        "Unable to %s handle %s%s": "无法%s句柄 %s%s",
        "close": "关闭",
        "the selected handle": "已选中的句柄",
        "the selected handles": "已选中的句柄",
        "Closing handles may cause system instability and data corruption.":
            "关闭句柄可能会导致系统不稳定和数据损坏。",
        "critical process handle(s)": "关键进程句柄",
        "You are about to close one or more handles for a critical process "
            "with strict handle checks enabled. This will shut down the operating "
                "system immediately.\r\n\r\n":
            "您即将关闭一个或多个启用了严格句柄检查的关键进程的句柄。这将立即关闭操作系统。\r\n\r\n",
        "Unable to open the process": "无法打开进程",
        "Setting handle attributes requires a connection to the kernel driver.":
            "设置句柄属性需要连接到内核驱动程序。",
        r"\U0001FA9F WinDbg\nGraphical debugger for both user-mode and kernel-mode debugging.": r"\U0001F4D8 WinDbg\n图形化调试器，支持用户模式和内核模式调试。", # 显示成方块？？
        r"\U0001FA9F WinDbg (Preview)\nModern graphical debugger for both user-mode and kernel-mode debugging.": r"\U0001F4D8 WinDbg (UWP)\n现代图形化调试器，支持用户模式和内核模式调试。",
        r"\U0001F4D8 Visual Studio 2026\nFull-featured IDE with integrated debugging.": r"\U0001F4D8 Visual Studio 2026\n功能齐全的集成开发环境，带有集成调试功能。",
        r"\U0001F4D8 Visual Studio 2022\nFull-featured IDE with integrated debugging.": r"\U0001F4D8 Visual Studio 2022\n功能齐全的集成开发环境，带有集成调试功能。",
        r"\U0001F4FA CDB\nCommand-line debugger for user-mode applications.": r"\U0001F4FA CDB\n用于用户模式应用程序的命令行调试器。",
        r"\U0001F4FA KD\nKernel debugger for low-level system debugging.": r"\U0001F4FA KD\n用于底层系统调试的内核调试器。",
        r"\U0001F4FA NTSD\nLegacy command-line debugger similar to CDB.": r"\U0001F4FA NTSD\n类似于 CDB 的传统命令行调试器。",
        r"\U00002699 (System Default)\n%s": r"\U00002699 (系统默认)\n%s",
        r"\U00002699 System Default\nNo debugger configured in AeDebug registry key.": r"\U00002699 系统默认\nAeDebug 注册表项中未配置调试器。",
        "Select a system debugger to use for this process:": "选择要用于此进程的系统调试器:",
        "You can choose from the installed debugging tools below.": "您可以从下方已安装的调试工具中进行选择。",
        "disable": "禁用",
        "Eco mode for this process": "进程节能模式",
        "Eco mode will lower process priority and improve power efficiency but may cause instability in some processes.":
            "节能模式会降低进程优先级并提高电源效率，但可能会导致某些进程不稳定。",
    },
                                                                    [
        (
            '                L"This option %s %s in a disorderly manner and may cause file corruption or system instability.",\n'
                '                L"performs a hard",\n'
                '                L"restart"',
            '                L"%s%s选项会以无序的方式执行，并可能导致文件损坏或系统不稳定。",\n'
                '                L"执行硬",\n'
                '                L"重启"'
        ), (
            '                L"This option %s %s in an disorderly manner and may cause corrupted files or instability in the system.",\n'
'                L"forces a critical",\n'
'                L"restart"',
            '                L"%s%s选项以无序的方式运行，可能会导致文件损坏或系统不稳定。"\n'
'                L"强制"\n'
'                L"重启"'
        ), (
            '                L"This option %s %s in an disorderly manner and may cause corrupted files or instability in the system.",\n'
'                L"performs a hard",\n'
'                L"shut down"',
            '                L"%s%s选项以无序的方式运行，可能会导致文件损坏或系统不稳定。"\n'
'                L"执行硬"\n'
'                L"关机"'
        ), (
            '                L"This option %s %s in an disorderly manner and may cause corrupted files or instability in the system.",\n'
'                L"forces a critical",\n'
'                L"shut down"',
            '                L"%s%s选项以无序的方式运行，可能会导致文件损坏或系统不稳定。"\n'
'                L"强制"\n'
'                L"关机"'
        ), (
            '''L"set",
            L"virtualization for the process",
            L"Enabling or disabling virtualization for a process may "
            L"alter its functionality and produce undesirable effects."''',
            '''L"设置",
            L"进程虚拟化选项",
            L"为进程启用或禁用虚拟化可能"
            L"改变其功能并产生不良影响。"'''
        ), ('''L"enable",
                L"critical status on the process",
                L"If the process ends, the operating system will shut down immediately."''',
            '''L"启用",
                L"进程关键状态",
                L"如果此类进程结束，操作系统将立即关闭。"'''
        ), ('''L"disable",
                L"critical status on the process"''',
            '''L"禁用",
                L"进程关键状态"'''
        ), (
            '''L"enable",
                    L"Eco mode for this process",
                    L"Eco mode will lower process priority and improve power efficiency but may cause instability in some processes."''',
            '''L"启用",
                    L"进程节能模式",
                    L"节能模式会降低进程优先级并提高电源效率，但可能会导致某些进程不稳定。"'''
        ), (
            '''L"change the execution required state",
            PhaConcatStrings2(L"of ", Process->ProcessName->Buffer)->Buffer,
            L"The process continues to run instead of being suspended or terminated by process lifetime management (PLM)."''',
            '''L"更改",
            PhaConcatStrings2(Process->ProcessName->Buffer, L" 进程的执行所需状态")->Buffer,
            L"该进程会继续运行，而不是被进程生命周期管理模块 (PLM) 挂起或终止。"'''
        ), (
            'Config.pszMainInstruction = PhaConcatStrings(3, L"Do you want to ", action->Buffer, L"?")->Buffer',
            'Config.pszMainInstruction = PhaConcatStrings(3, L"您确定要", action->Buffer, L"吗?")->Buffer'
        ), (
            '''L"start",
            L"Starting a service might prevent the system from functioning properly."''',
            '''L"启动",
            L"启动服务可能会导致系统无法正常运行。"'''
        ), (
            '''L"start",
        L"Starting a service might prevent the system from functioning properly."''',
            '''L"启动",
        L"启动服务可能会导致系统无法正常运行。"'''
        ), (
            'PhpShowErrorService(WindowHandle, L"start", Services[i], status, 0)',
            'PhpShowErrorService(WindowHandle, L"启动", Services[i], status, 0)'
        ), (
            'PhpShowErrorService(WindowHandle, L"start", Service, status, 0)',
            'PhpShowErrorService(WindowHandle, L"启动", Service, status, 0)'
        ), (
            '''L"continue",
            L"Continuing a service might prevent the system from functioning properly."''',
            '''L"继续运行",
            L"继续运行该服务可能会导致系统无法正常运行。"'''
        ), (
            '''L"continue",
        L"Continuing a service might prevent the system from functioning properly."''',
            '''L"继续运行",
        L"继续运行该服务可能会导致系统无法正常运行。"'''
        ), (
            'PhpShowErrorService(WindowHandle, L"continue", Services[i], status, 0)',
            'PhpShowErrorService(WindowHandle, L"继续运行", Services[i], status, 0)'
        ), (
            'PhpShowErrorService(WindowHandle, L"continue", Service, status, 0)',
            'PhpShowErrorService(WindowHandle, L"继续运行", Service, status, 0)'
        ), (
            '''L"pause",
            L"Pausing a service might prevent the system from functioning properly."''',
            '''L"挂起",
            L"挂起服务可能会导致系统无法正常运行。"'''
        ), (
            '''L"pause",
        L"Pausing a service might prevent the system from functioning properly."''',
            '''L"挂起",
        L"挂起服务可能会导致系统无法正常运行。"'''
        ), (
            'PhpShowErrorService(WindowHandle, L"pause", Services[i], status, 0)',
            'PhpShowErrorService(WindowHandle, L"挂起", Services[i], status, 0)'
        ), (
            'PhpShowErrorService(WindowHandle, L"pause", Service, status, 0)',
            'PhpShowErrorService(WindowHandle, L"挂起", Service, status, 0)'
        ), (
            '''L"stop",
            L"Stopping a service might prevent the system from functioning properly."''',
            '''L"停止",
            L"停止运行服务可能会导致系统无法正常运行。"'''
        ), (
            '''L"stop",
        L"Stopping a service might prevent the system from functioning properly."''',
            '''L"停止",
        L"停止运行服务可能会导致系统无法正常运行。"'''
        ), (
            'PhpShowErrorService(WindowHandle, L"stop", Services[i], status, 0)',
            'PhpShowErrorService(WindowHandle, L"停止", Services[i], status, 0)'
        ), (
            'PhpShowErrorService(WindowHandle, L"stop", Service, status, 0)',
            'PhpShowErrorService(WindowHandle, L"停止", Service, status, 0)'
        ), (
            '''L"delete",
        Service->Name->Buffer,
        L"Deleting a service can prevent the system from starting "
        L"or functioning properly."''',
            '''L"删除",
        Service->Name->Buffer,
        L"删除服务可能会导致系统无法启动或"
        L"无法正常运行。"'''
        ), (
            'PhpShowErrorService(WindowHandle, L"delete", Service, status, 0)',
            'PhpShowErrorService(WindowHandle, L"删除", Service, status, 0)'
        ), (
            'PhpShowErrorThread(WindowHandle, L"change priority of", Threads[i], status, 0)',
            'PhpShowErrorThread(WindowHandle, L"为以下线程更改优先级: ", Threads[i], status, 0)'
        ), (
            'PhpShowErrorThread(WindowHandle, L"set the priority of", Thread, status, 0)',
            'PhpShowErrorThread(WindowHandle, L"为以下线程设置优先级: ", Thread, status, 0)'
        ), (
            '''L". Make sure System Informer is running with "
                    L"administrative privileges."''',
            '''L"。请确保 System Informer "
                    L"以管理员权限运行。"'''
        ), (
            'verb = L"free"',
            'verb = L"释放"'
        ), (
            'PhpShowErrorHandle(WindowHandle, L"set attributes of", NULL, Handle, status, 0)',
            'PhpShowErrorHandle(WindowHandle, L"设置以下句柄的属性: ", NULL, Handle, status, 0)'
        ), (
            'PhpShowErrorProcess(WindowHandle, L"flush the process heap(s) of", Processes[i], status, 0)',
            'PhpShowErrorProcess(WindowHandle, L"刷新以下进程的堆: ", Processes[i], status, 0)'
        ), ('''L"The process will be restarted with the same command line, "
            L"working directory and privileges."''', 'L"该进程将使用相同的命令行、工作目录和权限重新启动。"')
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/admintask.c", "utf-8", {
        "Run as admin task": "以管理员身份运行任务",
        "Run as admin task: %!STATUS!": "以管理员身份运行任务: %!STATUS!",
        "Run as admin task UI access": "以管理员身份运行任务 UI 访问权限",
        "Run as admin task UI access: %!STATUS!": "以管理员身份运行任务 UI 访问权限: %!STATUS!",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/affinity.c", "utf-8", {
        "Unable to change affinity of process %lu": "无法更改进程 %lu 的处理器相关性",
        "Unable to change affinity of thread %lu": "无法更改线程 %lu 的处理器相关性",
        "An unknown error occurred.": "出现未知错误。",
        "Unable to update affinity for thread(s)": "无法为线程更新处理器相关性",
        "Unable to update affinity for thread(s):\r\n%s": "无法为线程更新处理器相关性: \r\n%s",
        "Group %hu": "组 %hu",
        "%s (%lu threads)": "%s (%lu 个线程)",
        "Unable to query the current affinity.": "无法查询当前处理器相关性。",
        "Unable to change affinity settings.": "无法更改处理器相关性设置。", 
        "You must select at least one CPU.": "您必须至少选择一个 CPU。", 
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/anawait.c", "utf-8", {
        "Unable to open the process.": "无法打开进程。",
        "Unable to open the thread.": "无法打开线程。",
        "Unable to analyze the thread.": "无法分析线程。",
        "The thread does not appear to be waiting.": "线程似乎没有处于等待状态。",
        "Unable to determine whether the thread is waiting.": "无法确定线程是否处于等待状态。",
        "Thread is waiting on system call: ": "线程正在等待系统调用: ",
        "Thread is waiting for:\r\n": "线程正在等待:\r\n",
        "Thread is waiting for multiple (%lu) objects.": "线程正在等待多个 (%lu) 个对象。",
        "Thread is waiting for file I/O:\r\n": "线程正在等待文件 I/O:\r\n",
        "Thread is sending a USER message:\r\n": "线程正在发送用户消息:\r\n",
        "Thread is waiting for an ALPC port:\r\n": "线程正在等待 ALPC 端口:\r\n",
        "Unable to determine why the thread is waiting.": "无法确定线程为何处于等待状态。",
        "Thread is sleeping. Timeout: %lu milliseconds.": "线程正在休眠。超时时间: %lu 毫秒。",
        "Thread is sleeping. Timeout: %llu milliseconds.": "线程正在休眠。超时时间: %llu 毫秒。",
        "Thread is sleeping.": "线程正在休眠。",
        "Thread is waiting for an I/O control request:\r\n": "线程正在等待 I/O 控制请求:\r\n",
        "Thread is waiting for a FS control request:\r\n": "线程正在等待文件系统控制请求:\r\n",
        "Thread is querying an object:\r\n": "线程正在查询对象\r\n",
        "Thread is waiting for an I/O completion port:\r\n": "线程正在等待 I/O 完成端口:\r\n",
        "Thread is waiting (%s) for an event pair:\r\n": "线程正在等待 (%s) 事件对:\r\n",
        "Thread is waiting for a USER message.\r\n": "线程正在等待用户消息。\r\n",
        "Unknown.": "未知。",
        "Thread is waiting for a debug event:\r\n": "线程正在等待调试事件:\r\n",
        "Thread is waiting (%s) for a keyed event (key 0x%Ix):\r\n": "线程正在等待 (%s) 键控事件 (键 0x%Ix):\r\n",
        "Thread is waiting (%s) for:\r\n": "线程正在等待 (%s):\r\n",
        "alertable": "可提醒",
        "non-alertable": "不可提醒",
        "Thread is waiting for work from a worker factory:\r\n": "线程正在等待工作者工厂:\r\n",
        "Handle 0x%lx (%s): %s": "句柄 0x%lx (%s): %s",
        "(unnamed object)": "(未命名对象)",
        "Handle 0x%lx: (error querying handle)": "句柄 0x%lx: (无法查询句柄)",
        "Thread is waiting (%s, %s) for:\r\n": "线程正在等待 (%s, %s):\r\n",
        "wait all": "等待全部",
        "wait any": "等待其中一个",
        "Thread is waiting for multiple objects.": "线程正在等待多个对象。",
        pre_format_string("Window 0x%Ix (%s): %s \"%s\""): pre_format_string("窗口 0x%Ix (%s): %s \"%s\""),
        "ALPC Port: %.*s (%s)": "ALPC 端口: %.*s (%s)",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/appsup.c", "utf-8", {
        # static CONST PH_KEY_VALUE_PAIR ProcessPriorityClassTypePairs[] =
        # {
            "Unknown": "未知", # PROCESS_PRIORITY_CLASS_UNKNOWN
            "Idle": "空闲", # PROCESS_PRIORITY_CLASS_IDLE
            "Normal": "正常", # PROCESS_PRIORITY_CLASS_NORMAL
            "High": "高", # PROCESS_PRIORITY_CLASS_HIGH
            "Real time": "实时", # PROCESS_PRIORITY_CLASS_REALTIME
            "Below normal": "低于正常", # PROCESS_PRIORITY_CLASS_BELOW_NORMAL
            "Above normal": "高于正常", # PROCESS_PRIORITY_CLASS_ABOVE_NORMAL
        # };
        # // switch ... case ...
        " (Audit)": " (审核)",
        "Secure (IUM)": "安全 (IUM)",
        "Unable to locate the application directory.": "无法找到应用程序目录。",
        "Unable to execute the command.": "无法执行命令。",
        "An unknown error occurred.": "发生未知错误。",
        " (64-bit)": " (64 位)",
        " (32-bit)": " (32 位)",
        # -------------------------------------------------------------------------------
        # Main Windows -> Processes Table -> Menu Items
        "Size column to fit": "调整列宽以适应屏幕", # sizeColumnToFitMenuItem
        "Size all columns to fit": "调整所有列宽以适应屏幕", # sizeAllColumnsToFitMenuItem
        "Hide column": "隐藏列", # hideColumnMenuItem
        "Choose columns...": "选择列...", # chooseColumnsMenuItem
        "Reset sort": "重置排序", # resetSortMenuItem
        # -------------------------------------------------------------------------------
        pre_format_string("Copy \""): pre_format_string("复制 \""),
        "Unable to execute the program.": "无法执行程序。",
        "None": "无",
    },
                                                                   [
        ('''static CONST PH_KEY_VALUE_PAIR PhProtectedTypeStrings[] =
{
    SIP(L"None", NULL), // PsProtectedTypeNone
    SIP(L"Light", PsProtectedTypeProtectedLight),
    SIP(L"Full", PsProtectedTypeProtected),
};''',
         '''static CONST PH_KEY_VALUE_PAIR PhProtectedTypeStrings[] =
{
    SIP(L"无", NULL), // PsProtectedTypeNone
    SIP(L"轻量", PsProtectedTypeProtectedLight),
    SIP(L"完全", PsProtectedTypeProtected),
};'''),
        ('PhpProtectionNoneString = PhCreateString(L"None");', 'PhpProtectionNoneString = PhCreateString(L"无");'),
        ('PhInitFormatS(&format[count++], L"Secure ");', 'PhInitFormatS(&format[count++], L"安全");'),
        (
            '''    switch (PhGetIntegerSetting(SETTING_RELEASE_CHANNEL))
    {
    case PhReleaseChannel:
        return L"Release";
    case PhPreviewChannel:
        return L"Preview";
    case PhCanaryChannel:
        return L"Canary";
    case PhDeveloperChannel:
        return L"Developer";
    }

    return L"Unknown";''',
            '''    switch (PhGetIntegerSetting(SETTING_RELEASE_CHANNEL))
    {
    case PhReleaseChannel:
        return L"正式版";
    case PhPreviewChannel:
        return L"预览版";
    case PhCanaryChannel:
        return L"测试版";
    case PhDeveloperChannel:
        return L"开发者版";
    }

    return L"未知版本";'''
        )
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/chcol.c", "utf-8", {
        "Inactive columns...": "隐藏的列...",
        "Active columns...": "显示的列...",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/chproc.c", "utf-8", {
        "Unable to enumerate processes": "无法枚举进程",
        # column head title
        "Name": "名称",
        "User name": "用户名",
        # "PID": "进程 ID",           # 貌似不太必要
        # column head title entries end
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/colsetmgr.c", "utf-8", {
        "Name": "名称",       # PhAddListViewColumn(context->ListViewHandle, ...)
    }, []),
    # dbgcon.c 翻译会导致控制台不显示输出。
    # (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/dbgcon.c", "utf-8", {
    #     "\tCount: %u": "\t计数: %u",
    #     "Type: %s\n": "类型: %s\n",
    #     "Reference count: %ld\n": "引用计数: %ld\n",
    #     "Flags: %x\n": "标志: %x\n",
    #     "Name: %s\n": "名称: %s\n",
    #     "Number of objects: %lu\n": "对象数量: %lu\n",
    #     "Flags: %u\n": "标志: %u\n",
    #     "Type index: %u\n": "类型索引: %u\n",
    #     "Free list count: %lu\n": "空闲列表计数: %lu\n",
    #     "Error.\n": "错误。\n",
    #     "Count: %u\n": "计数: %u\n",
    #     "Allocated buckets: %u\n": "已分配桶: %u\n",    # Windows 低碎片堆？
    #     "Allocated entries: %u\n": "已分配条目: %u\n",
    #     "Next free entry: %d\n": "下一个空闲条目: %d\n",
    #     "Next usable entry: %d\n": "下一个可用条目: %d\n",
    #     "Equal function: %s\n": "等价函数: %s\n",
    #     "Hash function: %s\n": "哈希函数: %s\n",
    #     "\nBuckets:\n": "\n桶:\n",
    #     "\nExpected lookup misses: %lu\n": "\n预期查找未命中: %lu\n",
    #     "Leak at 0x%Ix (%Iu bytes). Stack trace:\n": "泄漏发生在 0x%Ix (%Iu 字节)，堆栈跟踪:\n",
    #     "[fail]: writers active in read zone!\n": "[失败]: 读取区域中有处于活动状态的写入区域!\n",  # todo
    #     "[fail]: readers active in write zone!\n": "[失败]: 写入区域中有处于活动状态的读取区域!\n", # todo
    #     "[null] %s: %ums\n": "[空] %s: %ums\n", # and line 586: L"[strs] %s: %ums\n"
    #     pre_format_string("Press Ctrl+C or type \"exit\" to close the debug console. "
    #                       "Type \"help\" for a list of commands.\n"):
    #         pre_format_string("按 Ctrl+C 或输入 \"exit\" 关闭调试控制台。输入 \"help\" 查看命令列表。\n"),
    #     "This command is not available on non-debug builds.\n": "此命令在非调试版本中不可用。\n",
    #     "Commands:\n": "可用的命令:\n",
    #     "Referencing: %ums\n": "正在引用: %ums\n",
    #     "Critical section: %ums\n": "临界区: %ums\n",
    #     "Fast lock: %ums\n": "快速锁: %ums\n",
    #     "Queued lock: %ums\n": "队列锁: %ums\n",
    #     "Object small free list count: %u\n": "对象小型空闲列表计数:%u\n",
    #     "Statistics:\n": "统计数据:\n",
    #     "Total number: %lu\n": "总计: %lu\n",
    #     "Total overhead (header): %s\n": "总开销 (header): %s\n",
    #     "Missing object address.\n": "丢失对象地址。\n",
    #     "Error: %s\n": "错误: %s\n",
    #     "Invalid object address.\n": "对象地址无效。\n",
    #     "No snapshot.\n": "无快照。\n",
    #     "Static count: %u\n": "静态计数: %u\n",
    #     "Dynamic count: %u\n": "动态计数: %u\n",
    #     "Dynamic allocated: %u\n": "动态分配: %u\n",
    #     "Static objects:\n": "静态对象:\n",
    #     "Dynamic objects:\n": "动态对象:\n",
    #     "Thread %u\n": "线程 %u\n",
    #     "\tStart Address: %s\n": "\t起始地址: %s\n",
    #     "\tParameter: %Ix\n": "\t参数: %Ix\n",
    #     "\tCurrent auto-pool: %Ix\n": "\t当前 auto-pool: %Ix\n",
    #     "Thread not running\n": "线程未运行\n",
    #     "\tProvider registration at %Ix\n": "\t服务提供商注册 %Ix\n",
    #     "\t\tEnabled: %s\n": "\t\t已启用: %s\n",
    #     "Yes": "是",
    #     "No": "否",
    #     "\t\tFunction: %s\n": "\t\t函数: %s\n",
    #     "\t\tObject:\n": "\t\t对象:\n",
    #     "Work queue at %s\n": "工作队列 %s\n",
    #     "Maximum threads: %lu\n": "最大线程数: %lu\n",
    #     "Minimum threads: %lu\n": "最小线程数: %lu\n",
    #     "No work timeout: %lu\n": "无工作超时: %lu\n",
    #     "Current threads: %lu\n": "当前线程: %lu\n",
    #     "Busy count: %lu\n": "忙碌计数: %lu\n",
    #     "\tWork queue item at %Ix\n": "\t工作队列项 %Ix\n",
    #     "\t\tContext: %Ix\n": "\t\t上下文: %Ix\n",
    #     "Records for %s %s:\n": "%s %s 的记录:\n",
    #     "\tRecord at %Ix: %s (%lu) (refs: %ld)\n": "\t记录 %Ix: %s (%lu) (引用: %ld)\n",
    #     "Process item at %Ix: %s (%u)\n": "进程项 %Ix: %s (%u)\n",
    #     "\tRecord at %Ix\n": "\t记录 %Ix\n",
    #     "\tQuery handle %Ix\n": "\t队列句柄 %Ix\n",
    #     "\tFile name at %Ix: %s\n": "\t文件名 %Ix: %s\n",
    #     "\tCommand line at %Ix: %s\n": "\t命令行 %Ix: %s\n",
    #     "\tFlags: %u\n": "\t标志: %u\n",
    #     "\nTotal unique strings: %u\n": "\n唯一字符串总计: %u\n",
    #     "Unable to initialize heap debugging. Make sure that you are using Windows 7 or above.":
    #         "无法初始化堆调试。请确保您使用的是 Windows 7 或更高版本。",
    #     "Warning: user-mode stack trace database is not enabled. Stack traces will not be displayed.\n":
    #         "警告: 用户模式堆栈跟踪数据库未启用。堆栈跟踪将不会显示。\n",
    #     "\nNumber of leaks: %lu (%lu displayed)\n": "\n泄漏数量: %lu (%lu 已显示)\n",
    #     "Number of bytes must be 256 or smaller.\n": "字节数必须小于或等于 256。\n",
    #     "Error reading address near %Ix.\n": "读取地址 %Ix 附近时出错。\n",
    #     "Usage: mem address [numberOfBytes]\n": "语法: mem address [numberOfBytes]\n",
    #     "Example: mem 12345678 16\n": "示例: mem 12345678 16\n",
    #     "Unrecognized command.\n": "无法识别的命令。\n",
    # }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/delayhook.c", "utf-8", {
        "Unable to register window class.": "无法注册窗口类。",
        "Unable to commit detours transaction.": "无法提交绕行事务。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/devprv.c", "utf-8", {
        "Line based, ": "按行, ",
        "true": "是",
        "false": "否",
        "Wake from D0": "恢复自 D0",
        "Wake from D1": "恢复自 D1",
        "Wake from D2": "恢复自 D2",
        "Wake from D3": "恢复自 D3",
        "Warm eject": "热弹出",
        " D1 latency": " D1 延迟",
        " D2 latency": " D2 延迟",
        " D3 latency": " D3 延迟",
        ", Deepest wake ": ", 深度唤醒 ",
        # Function `PhpDevPropFillUInt32Flags`
        # static const PH_ACCESS_ENTRY deviceCapabilities[] =
        # {
            "Lock supported": "支持锁定",
            "Eject supported": "支持弹出",
            "Removable": "可移除",
            "Dock device": "扩展坞设备",
            "Unique ID": "唯一 ID",
            "Silent install": "静默安装",
            "Raw device ok": "原始设备正常",
            "Surprise removal ok": "意外移除正常",
            "Hardware disabled": "硬件已禁用",
            "No dynamic": "无动态",
            "Secure device": "安全设备",
        # };
        # static const PH_ACCESS_ENTRY devNodeStatus[] =
        # {
            "Enumerated": "已枚举",
            "Driver loaded": "驱动程序已加载",
            "Enumerator loaded": "枚举器已加载",
            "Started": "已启动",
            "Manually installed": "手动安装",
            "Needs enumerated": "需要枚举",
            "Driver blocked": "驱动程序已屏蔽",
            "Hardware enum": "硬件枚举",
            "Needs reboot": "需要重启",
            "Child with invalid ID": "无效 ID 子节点",
            "Has problem": "出现问题",
            "Filtered": "已筛选",
            "Legacy driver": "旧版驱动程序",
            "Disabled": "已禁用",
            "Query remove pending": "查询/移除挂起",
            "Query remove active": "查询/移除活动",
            "Being removed": "将被移除",
            "Received Config": "已接收配置",
            "To be freed": "待释放",
            "Rebalance candidate": "重平衡候选设备",
            "Bad partial": "局部错误",
            "NT enumerator": "NT 枚举器",
            "NT driver": "NT 驱动程序",
            "Disconnected": "已断开连接",
            "Wakeup device": "唤醒设备",
            "Advanced power enumerator": "高级电源枚举器",
            "Advanced power aware": "高级电源感知",
            "Hidden from device manager": "已从设备管理器隐藏",
            "Boot log problem": "启动日志问题",
        # };
        # static const PH_ACCESS_ENTRY characteristics[] =
        # {
            "Removable media": "可移除介质",
            "Read only device": "只读设备",
            "Floppy disk": "软盘",
            "Write once media": "一次性写入介质",
            "Remote device": "远程设备",
            "Mounted": "已挂载",
            "Virtual volume": "虚拟卷",
            "Autogenerated device name": "自动生成的设备名",
            "Secure open": "安全打开",
            "PnP device": "PnP 设备",
            "Terminal services device": "终端服务设备",
            "WebDAV device": "WebDAV 设备",
            "Cluster shared volume": "集群共享卷",
            "Allow app container traversal": "允许应用容器遍历",
            "Portable device": "便携设备",
            "Virtual SCSI device": "虚拟 SCSI 设备",
            "Require security check": "需要安全检查",
        # };
        # static const PH_ACCESS_ENTRY nameAttributes[] =
        # {
            "Retrieved from device": "已从设备中检索",
            "User assigned name": "用户分配的名称",
        # };
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/findobj.c", "utf-8", {
        "Name": "名称",
        "Object address": "对象地址",
        "Original name": "原始名称",
        "Granted access": "已授予访问权限",
        "Everything": "所有对象",
        "Mapped file": GLOBAL_DICT["Mapped file"],
        "Mapped image": GLOBAL_DICT["Mapped image"],
        "Unidentified third party object.": "不明第三方定义对象。",
        "Find Handles or DLLs": "查找句柄或 DLL",
        "Cancel": "取消",
        "C&lose\bDel": "关闭(&L)\bDel",
        "Go to &process...": "转到进程(&P)...",
        "Prope&rties": "属性(&R)",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        "close": "关闭",
        "the selected handle": "已选中的句柄",
        "the selected handles": "已选中的句柄",
        "Closing handles may cause system instability and data corruption.": "关闭句柄可能会导致系统不稳定和数据损坏。",
        "critical handle(s)": "关键进程句柄",
        "You are about to close one or more handles for a critical process with strict handle "
                "checks enabled. This will shut down the operating system immediately.\r\n\r\n":
            "您即将关闭一个或多个启用了严格句柄检查的关键进程的句柄。这将立即关闭操作系统。\r\n\r\n",
        pre_format_string("Unable to close \"%s\""): pre_format_string("无法关闭 \"%s\""),
        "The process does not exist.": "进程不存在。",
        "%s (%lu results)": "%s (%lu 个结果)",
        "Find": "查找",
        "Unable to search for handles because the total number of handles on the system is too large.":
            "由于系统上的句柄总数过大，无法搜索句柄。",
        "Please check if there are any processes with an extremely large number of handles open.":
            "请检查是否存在打开句柄数量异常庞大的进程。",
        "Unable to create the window.": "无法创建窗口。",
    },
                                                                    [
        (
            'PhAddTreeNewColumn(Context->TreeNewHandle, PH_OBJECT_SEARCH_TREE_COLUMN_PROCESS, TRUE, L"Process"',
            'PhAddTreeNewColumn(Context->TreeNewHandle, PH_OBJECT_SEARCH_TREE_COLUMN_PROCESS, TRUE, L"进程"'
        ), (
            'PhAddTreeNewColumn(Context->TreeNewHandle, PH_OBJECT_SEARCH_TREE_COLUMN_TYPE, TRUE, L"Type"',
            'PhAddTreeNewColumn(Context->TreeNewHandle, PH_OBJECT_SEARCH_TREE_COLUMN_TYPE, TRUE, L"类型"'
        ), (
            'PhAddTreeNewColumn(Context->TreeNewHandle, PH_OBJECT_SEARCH_TREE_COLUMN_HANDLE, TRUE, L"Handle"',
            'PhAddTreeNewColumn(Context->TreeNewHandle, PH_OBJECT_SEARCH_TREE_COLUMN_HANDLE, TRUE, L"句柄"'
        )
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/gdihndl.c", "utf-8", {
        # switch (GDI_CLIENT_TYPE_FROM_UNIQUE(Unique)) { case ... : ... , ......}
            "Alt. DC": "备用 DC", # GDI_CLIENT_ALTDC_TYPE
            "Bitmap": "位图", # GDI_CLIENT_BITMAP_TYPE
            "Brush": "画刷", # GDI_CLIENT_BRUSH_TYPE
            "Client Object": "客户端对象", # GDI_CLIENT_CLIENTOBJ_TYPE
            "DIB Section": "DIB 节区", # GDI_CLIENT_DIBSECTION_TYPE
            # ignore GDI_CLIENT_DC_TYPE
            # not ignore GDI_CLIENT_EXTPEN_TYPE (next line)
            "ExtPen": "扩展画笔", # GDI_CLIENT_EXTPEN_TYPE
            "Font": "字体", # GDI_CLIENT_FONT_TYPE
            "Metafile DC": "元文件 DC", # GDI_CLIENT_METADC16_TYPE
            "Enhanced Metafile": "增强元文件", # GDI_CLIENT_METAFILE_TYPE
            "Metafile": "元文件", # GDI_CLIENT_METAFILE16_TYPE
            "Palette": "调色板", # GDI_CLIENT_PALETTE_TYPE
            "Pen": "画笔", # GDI_CLIENT_PEN_TYPE
            "Region": "区域", # GDI_CLIENT_REGION_TYPE
        # switch ... case ... end.
        "Width: %u, Height: %u, Depth: %u": "宽度: %u, 高度: %u, 深度: %u",
        "Style: %u, Color: 0x%08x, Hatch: 0x%Ix": "样式: %u, 颜色: 0x%08x, 阴影: 0x%Ix",
        "Style: 0x%x, Width: %u, Color: 0x%08x": "样式: 0x%x, 宽度: %u, 颜色: 0x%08x",
        "Face: %s, Height: %d": "表面: %s, 高度: %d",
        "Entries: %u": "条目数: %u",
        "Style: %u, Width: %u, Color: 0x%08x": "样式: %u, 宽度: %u, 颜色: 0x%08x",
        "Object": "对象",
        "Information": "信息",
        "&Copy": "复制(&C)",
    },
                                                                    [
         (
             'PhAddListViewColumn(context->ListViewHandle, 0, 0, 0, LVCFMT_LEFT, 100, L"Type")',
             'PhAddListViewColumn(context->ListViewHandle, 0, 0, 0, LVCFMT_LEFT, 100, L"类型")'
         ), (
         'PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 80, L"Handle")',
         'PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 80, L"句柄")'
     ),
     ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/heapinfo.c", "utf-8", {
        # PPH_STRING PhGetProcessHeapFlagsText(
        #     _In_ ULONG Flags
        #     )
        # {
        "No serialize, ": "未序列化, ", # HEAP_NO_SERIALIZE
        "Growable, ": "可增长, ", # HEAP_GROWABLE
        "Generate exceptions, ": "生成异常, ", # HEAP_GENERATE_EXCEPTIONS
        "Zero memory, ": "零化内存, ", # HEAP_ZERO_MEMORY
        "Realloc in-place, ": "原地重分配, ", # HEAP_REALLOC_IN_PLACE_ONLY
        "Tail checking, ": "尾部检查, ", # HEAP_TAIL_CHECKING_ENABLED
        "Free checking, ": "空闲检查, ", # HEAP_FREE_CHECKING_ENABLED
        "Coalesce on free, ": "释放时合并, ", # HEAP_DISABLE_COALESCE_ON_FREE
        "Align 16, ": "对齐 16 位, ", # HEAP_CREATE_ALIGN_16
        "Traceable, ": "可跟踪, ", # HEAP_CREATE_ENABLE_TRACING
        "Executable, ": "可执行, ", # HEAP_CREATE_ENABLE_EXECUTE
        "Segment heap, ": "段堆, ", # HEAP_CREATE_SEGMENT_HEAP
        "Segment hardened, ": "堆硬化, ", # HEAP_CREATE_HARDENED
        # }
        # PCWSTR PhGetProcessHeapClassText(
        #     _In_ ULONG HeapClass
        #     )
        # {
        "Process Heap": "进程堆",
        "Private Heap": "私有堆",
        "Kernel Heap": "内核堆",
        "GDI Heap": "GDI 堆",
        "User Heap": "用户堆",
        "Console Heap": "控制台堆",
        "Desktop Heap": "桌面堆",
        "CSRSS Shared Heap": "CSRSS 共享堆",
        "CSRSS Port Heap": "CSRSS 端口堆",
        "Unknown Heap": "未知堆", # ...
        # }
        "Unable to query heap information.": "无法查询堆信息。",
        "NT Heap (Lookaside)": "NT 堆 (旁视列表)",
        "NT Heap (LFH)": "NT 堆 (LFH)",
        "NT Heap": "NT 堆",
        "Segment Heap (Lookaside)": "段堆 (旁视列表)",
        "Segment Heap (LFH)": "段堆 (LFH)",
        "Segment Heap": "段堆",
        "Unable to query 32bit heap information.": "无法查询 32 位堆信息。",
        "The 32-bit version of System Informer could not be located.": "找不到 32 位版本的 System Informer。",
        "Heaps - ": "堆 - ",
        "Address": "地址",
        "Used": "已使用",
        "Committed": "已提交",
        "Entries": "条目",
        "Flags": "标志",
        "Class": "类",
        "Copy\bCtrl+C": "复制\bCtrl+C",
        "Segment Heap\n": "段堆\n",
        "NT-%lu - 0x%I64x - committed: %lu - allocated: %lu - count: %lu\n":
            "NT-%lu - 0x%I64x - 已提交: %lu - 已分配: %lu - 计数: %lu\n",
        "destroy": "销毁",
        "the selected heap": "已选中的堆",
        "Destroying heaps may cause the process to crash.": "销毁堆可能会导致进程崩溃。",
        "Unable to destroy the heap": "无法销毁堆",
        "\nHeap ID: %lu\n": "\n堆 ID: %lu\n",
        "Block size: %lu\n": "块大小: %lu\n",
        "Critical section": "临界区",
        "Resource": "资源",
        "Unable to query lock information.": "无法查询锁信息。",
        "Locks - ": "锁 - ",
        "Filename": "文件名",
        "Lock count": "锁计数",
        "Entry count": "条目计数",
        "Recursion count": "递归计数",
        "Waiting shared count": "等待共享计数",
        "Waiting exclusive count": "等待递归计数",
    },
                                                                     [
         (
             'PhAddListViewColumn(context->ListViewHandle, 7, 7, 7, LVCFMT_LEFT, 80, L"Type")',
             'PhAddListViewColumn(context->ListViewHandle, 7, 7, 7, LVCFMT_LEFT, 80, L"类型")'
         ), (
         'PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 50, L"Type")',
         'PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 50, L"类型")'
     ), (
         'PhAddListViewColumn(context->ListViewHandle, 4, 4, 4, LVCFMT_LEFT, 120, L"Thread")',
         'PhAddListViewColumn(context->ListViewHandle, 4, 4, 4, LVCFMT_LEFT, 120, L"线程")'
     )
     ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/hndllist.c", "utf-8", {
        "Name": "名称",
        "Granted access (symbolic)": "已授予访问权限 (符号)",
        "Object address": "对象地址",
        "Attributes": "属性",
        "Granted access": "已授予访问权限",
        "Original name": "原始名称",
        "File share access": "文件共享访问权限",
        "Handle value": "句柄值",
        "Handle count": "句柄计数",
        "Reference count": "引用计数",
        "Paged size": "分页大小",
        "Nonpaged size": "非分页大小",
        "Protected": "受保护",
        "Inherit": "继承",
        "Protected, Inherit": "受保护, 继承",
    },
                                                                     [
        (
            'PhAddTreeNewColumn(hwnd, PHHNTLC_TYPE, TRUE, L"Type"',
            'PhAddTreeNewColumn(hwnd, PHHNTLC_TYPE, TRUE, L"类型"'
        ), (
        'PhAddTreeNewColumn(hwnd, PHHNTLC_HANDLE, FALSE, L"Handle"',
        'PhAddTreeNewColumn(hwnd, PHHNTLC_HANDLE, FALSE, L"句柄"'
    ),
    #     (
    #         'TypeName, L"File", TRUE', # 有争议
    #         'TypeName, L"文件", TRUE'
    # ),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/hidnproc.c", "utf-8", {
        "%u zombie process(es), %u terminated process(es).": "%u 个僵尸进程, %u 个已终止进程。",
        "Brute force": "强制扫描",
        "CSR handles": "CSR 句柄",
        "ETW handles": "ETW 句柄",
        "Process handles": "进程句柄",
        "Registry handles": "注册表句柄",
        "Ntdll handles": "NTDLL 句柄",
        "terminate": "结束",
        "the selected process(es)": "已选中进程",
        "Unable to terminate the process": "无法结束进程",
        "Text files (*.txt)": "文本文档 (*.txt)",
        "All files (*.*)": "所有文件 (*.*)",
        "Zombie Processes.txt": "僵尸进程.txt",
        "Method: ": "方法: ",
        "Brute Force\r\n": "强制扫描\r\n",
        "CSR Handles\r\n": "CSR 句柄\r\n",
        "Zombie: %u\r\nTerminated: %u\r\n\r\n": "僵尸进程: %u\r\n已结束进程: %u\r\n\r\n",
        "[Zombie] ": "[僵尸进程] ",
        "[Terminated] ": "[已终止] ",
        "Unable to create the file": "无法创建文件",
        "Unable to create a process structure for the selected process.": "无法为所选进程创建进程结构。",
        "&Copy": "复制(&C)",
        "Unable to perform the scan": "无法执行扫描",
        "(unknown)": "(未知)",
    },
                                                                     [
        (
            'PhAddListViewColumn(lvHandle, 0, 0, 0, LVCFMT_LEFT, 320, L"Process")',
            'PhAddListViewColumn(lvHandle, 0, 0, 0, LVCFMT_LEFT, 320, L"进程")'
        ), (
            '''L"Terminating a Zombie process may cause the system to become unstable "
                            L"or crash."''',
            '''L"终止僵尸进程可能会导致系统不稳定或崩溃。"'''
        )
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/hndlmenu.c", "utf-8", {
        "Mapped file": GLOBAL_DICT["Mapped file"],
        "Mapped image": GLOBAL_DICT["Mapped image"],
        "File propert&ies": "文件属性(&I)",
        "Open &file location": "打开文件所在位置(&F)",
        "Open &key": "打开键(&K)",
        "Go to process...": "转到进程...",
        "Process propert&ies": "进程属性(&I)",
        "Read/Write &memory": "读取/写入内存",
        "Go to t&hread...": "转到线程(&H)...",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "Unable to open the file location.": "无法打开文件所在位置。",
        "The object is unnamed.": "对象未命名。",
        "Unable to open key.": "无法打开注册表键。",
        "Unable to show the process properties.": "无法显示进程属性。",
        "The process does not exist.": "进程不存在。",
        "Unable to map a view of the section.": "无法映射节区视图。",
        "The section size is greater than 32 MB. Only the first 32 MB will be available.":
            "该节区大小超过 32 MB，仅可用前 32 MB。",
        "Unable to query the section.": "无法查询节区。",
        "Unable to open the file properties.": "无法打开文件属性。",
    },
                                                                     [
        ('showMemoryEditor->Title = sectionName ? PhConcatStrings2(L"Section - ", sectionName->Buffer) : PhCreateString(L"Section");',
        'showMemoryEditor->Title = sectionName ? PhConcatStrings2(L"节区 - ", sectionName->Buffer) : PhCreateString(L"节区");')
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/hndlprp.c", "utf-8", {
        "Asynchronous": "异步",
        "Write through": "直写",
        "Sequential": "顺序",
        "No buffering": "无缓冲",
        "Synchronous alert": "同步警报",
        "Synchronous non-alert": "同步非警报",
        "LPC mode": "LPC 模式",
        "Allow impersonation": "允许模拟",
        "Allow LPC requests": "允许 LPC 请求",
        "Waitable": "可等待",
        "Allow object duplication": "允许对象复制",
        "System process only": "仅系统线程",
        "Wake policy (1)": "唤醒策略 (1)",
        "Wake policy (2)": "唤醒策略 (2)",
        "Wake policy (3)": "唤醒策略 (3)",
        "No shared section (direct)": "无共享节区 (直接)",
        "Allow multi-handle attributes": "允许多句柄属性",
        "N/A (snapshot)": "N/A (快照)",
        "Basic information": "基本信息",
        "Security information": "安全信息",
        "References": "引用",
        "Quota charges": "配额用量",
        "Name": "名称",
        "Object address": "对象地址",
        "FullPath": "完整路径",
        "Granted access": "已授予访问权限",
        "Granted access (generic)": "已授予访问权限 (通用)",
        "Granted access (mask)": "已授予访问权限 (掩码)",
        "Handles": "句柄",
        "Paged": "分页",
        "Virtual size": "虚拟大小",
        "Flags": "标志",
        "Sequence Number": "序列号",
        "Port Context": "端口上下文",
        "Connection": "连接",
        "Server": "服务端",
        "Client": "客户端",
        "Owner": "所有者",
        "Event trace information": "事件跟踪信息",
        "File information": "文件信息",
        "Mode": "模式",
        "Position": "位置",
        "Size": "大小",
        "Priority": "优先级",
        "Driver Image": "驱动映像",
        "Section information": "节区信息",
        "Mutant information": "互斥体信息",
        "Count": "计数",
        "Abandoned": "废弃",
        "Process information": "进程信息",
        "Created": "创建于",
        "Exited": "退出于",
        "Exit status": "退出代码",
        "Thread information": "线程信息",
        "Symbolic Link information": "符号链接信息",
        "Link target": "链接目标",
        "Read, ": "读取, ",
        "Write, ": "写入, ",
        "Execute, ": "执行, ",
        "All, ": "所有, ",
        "Network": "网络",
        "File or directory": "文件或目录",
        "Console": "控制台",
        "Other": "其他",
        "Very Low": "非常低",
        "Low": "低",
        "Normal": "正常",
        "High": "高",
        "Critical": "关键",
        "Unknown": "未知",
        "Commit": "提交",
        "Image": "映像",
        "Reserve": "保留",
        "Value": "值",
        "&Copy": "复制(&C)",
        " (User)": " (用户)",
        " (Group)": " (组)",
        " (Computer)": " (计算机)",
        "Allow": "允许",
        "Group": "组",
        "Integrity": "完整性",
        "Auditing information": "审核信息",
        "Access": "访问权限",
        "Principal": "主要",
        "Integrity level": "完整性级别",
        "Unable to disable the integrity level.": "无法禁用完整性级别。",
        "Inherited from": "继承自",
        "Source": "源",
    },
                                                                    [
        ('propSheetHeader.pszCaption = L"Handle"', 'propSheetHeader.pszCaption = L"句柄"'),
        ('PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_BASICINFO, PH_HANDLE_GENERAL_INDEX_TYPE, L"Type")',
            'PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_BASICINFO, PH_HANDLE_GENERAL_INDEX_TYPE, L"类型")'),
        ('PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_FILE, PH_HANDLE_GENERAL_INDEX_FILETYPE, L"Type")',
            'PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_FILE, PH_HANDLE_GENERAL_INDEX_FILETYPE, L"类型")'),
        ('PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_FILE, PH_HANDLE_GENERAL_INDEX_FILEDRIVER, L"Driver")',
            'PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_FILE, PH_HANDLE_GENERAL_INDEX_FILEDRIVER, L"驱动程序")'),
        ('PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_SECTION, PH_HANDLE_GENERAL_INDEX_SECTIONTYPE, L"Type")',
            'PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_SECTION, PH_HANDLE_GENERAL_INDEX_SECTIONTYPE, L"类型")'),
        ('PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_SECTION, PH_HANDLE_GENERAL_INDEX_SECTIONFILE, L"File")',
            'PhAddHandleListViewItem(Context->ListViewClass, PH_HANDLE_GENERAL_CATEGORY_SECTION, PH_HANDLE_GENERAL_INDEX_SECTIONFILE, L"文件")'),
        ('PhSetHandleListViewItem(Context, PH_HANDLE_GENERAL_INDEX_FILETYPE, 1, L"Pipe")',
            'PhSetHandleListViewItem(Context, PH_HANDLE_GENERAL_INDEX_FILETYPE, 1, L"管道")'),
        ('PhSetHandleListViewItem(Context, PH_HANDLE_GENERAL_INDEX_FILETYPE, 1, fileStandardInfo.Directory ? L"Directory" : L"File")',
            'PhSetHandleListViewItem(Context, PH_HANDLE_GENERAL_INDEX_FILETYPE, 1, fileStandardInfo.Directory ? L"目录" : L"文件")'),
        ('sectionType = L"File"', 'sectionType = L"文件"'),
        ('PhSetHandleListViewItem(Context, PH_HANDLE_GENERAL_INDEX_MUTANTABANDONED, 1, basicInfo.AbandonedState ? L"True" : L"False")',
            'PhSetHandleListViewItem(Context, PH_HANDLE_GENERAL_INDEX_MUTANTABANDONED, 1, basicInfo.AbandonedState ? L"是" : L"否")'),
        ('PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 50, L"Type")',
            'PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 50, L"类型")'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/hndlstat.c", "utf-8", {
        "Unable to open the process": "无法打开进程",
        "Unable to enumerate process handles": "无法枚举进程句柄",
        "Count": "计数",
        "(unknown: %lu)": "(未知: %lu)",
    },
                                                                    [
         ('PhAddListViewColumn(context->ListViewHandle, 0, 0, 0, LVCFMT_LEFT, 140, L"Type")',
            'PhAddListViewColumn(context->ListViewHandle, 0, 0, 0, LVCFMT_LEFT, 140, L"类型")'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/infodlg.c", "utf-8", {
        "Text files (*.txt)": "文本文档 (*.txt)",
        "All files (*.*)": "所有文件 (*.*)",
        "Information.txt": "信息.txt",
        "Unable to create the file": "无法创建文件",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/itemtips.c", "utf-8", {
        "File:\n": "文件:\n",
        "Service group name:\n    ": "服务组名称:\n    ",
        "Service group name:\n": "服务组名称:\n",
        "Run DLL target file:\n": "运行 DLL 目标文件:\n",
        "COM target:\n": "COM 目标:\n",
        "COM target file:\n": "COM 目标文件:\n",
        "Services:\n": "服务:\n",
        "Tasks:\n": "任务:\n",
        "Drivers:\n": "驱动程序:\n",
        "Edge:\n": "边缘:\n",
        "WMI Providers:\n": "WMI 提供程序:\n",
        "    Signer: %s\n": "    签名方: %s\n",
        "    Signed.\n": "    已签名。\n",
        "    Signature invalid.\n": "    签名无效。\n",
        "    Image is probably packed (%lu %ls over %lu %ls).\n": "    映像可能已打包 (%lu %ls 覆盖 %lu %ls)。\n",
        "import": "导入项",
        "imports": "导入项",
        "module": "模块",
        "modules": "模块",
        "    Low image coherency: %.2f%%\n": "    低级映像一致性: %.2f%%\n",
        "Console application": "控制台应用程序",
        "Console host": "控制台宿主程序",
        "    Package name: %s\n": "    包名称: %s\n",
        "Notes:\n": "备注:\n",
        "    Process is a system process (TCB).\n": "    该进程是系统级进程 (WinTcb)。\n",
        "    Process is being debugged.\n": "    该进程正在被调试。\n",
        "    Process is suspended.\n": "    该进程已被挂起。\n",
        "    Process is in deep freeze (suspended).\n": "    该进程正处于深度睡眠 (挂起) 状态。\n",
        "    Process is managed (.NET).\n": "    该进程已被托管 (.NET 进程)。\n",
        "Unknown Device": "未知设备",
        "Unknown path": "未知路径",
        "Unknown action": "未知操作",
        "    Process is default elevated.\n": "    进程优先级已以默认策略提升。\n",
        "    Process is full elevated.\n": "    进程优先级已以完全策略提升。\n",
        "    Process is limited elevated.\n": "    进程优先级已以受限策略提升。\n",
        "    Process is elevated.\n": "    进程优先级已被提升。\n",
        "    Process is UIAccess.\n": "    进程是 UIAccess。\n",
        "    Process is a Modern UI app.\n": "    进程是现代 UI 应用程序。\n",
        "    Process is in a job.\n": "    进程位于作业中。\n",
        "    Process is 32-bit (WOW64).\n": "    进程为 32 位 (WOW64) 进程。\n",
        "    Process is a protected process (PP/PPL).\n": "    进程是受保护进程 (PP/PPL)。\n",
        "    Process is a secure isolated process (IUM).\n": "    进程是隔离用户模式 (IUM) 进程。\n",
        "    Process is a secure virtualization process (HVCI).\n": "    进程是安全虚拟化进程 (HVCI)。\n",
        "    Process is a subsystem process.\n": "    进程是子系统进程。\n",
        "    Process is a packaged process.\n": "    进程是打包的应用程序。\n",
        "    Process is a background process.\n": "    进程是后台进程。\n",
        "    Process is a cross session process.\n": "    进程是多会话进程。\n",
        "    Process is a reflected process.\n": "    进程是反射进程。\n",
        "    Process is a cloned process.\n": "    进程是克隆进程。\n",
        "    Process is a snapshot process.\n": "    进程是快照进程。\n",
        "    Process is power throttling (efficiency).\n": "    进程正在进行效率优化。\n",
        "Flags:\n": "标志:\n",
        "Description:\n    ": "描述:\n    ",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/jobprp.c", "utf-8", {
        "Name": "名称",
        "Value": "值",
        "Unknown": "未知",
        "(unnamed job)": "(未命名作业)",
        "Active processes": "活动的进程",
        "Affinity": "处理器相关性",
        "Breakaway OK": "断开连接",
        "Enabled": "启用",
        "Die on unhandled exception": "遇到未处理异常时终止",
        "Job memory": "作业内存",
        "Job time": "作业时间",
        "Kill on job close": "作业关闭时终止",
        "Priority class": "优先级类",
        "Process memory": "进程内存",
        "Process time": "进程时间",
        "Scheduling class": "任务计划类",
        "Silent breakaway OK": "静默断开连接",
        "Working set minimum": "工作集最小值",
        "Working set maximum": "工作集最大值",
        "Limited": "受限",
        "Display settings": "显示设置",
        "Exit windows": "退出窗口",
        "Global atoms": "全局原子表",
        "Handles": "句柄",
        "Read clipboard": "读取剪贴板",
        "System parameters": "系统参数",
        "Write clipboard": "写入剪贴板",
        "terminate": "终止",
        "the job": "作业",
        "Terminating a job will terminate all processes assigned to it.": "终止作业将终止分配给该作业的所有进程。",
        "Unable to terminate the job": "无法终止作业",
        "Select a process to add to the job permanently.": "选择要永久添加到该作业的进程。",
        "Unable to add the process to the job": "无法向作业添加进程",
        "&Copy": "复制(&C)",

    },
     [
        ('propSheetHeader.pszCaption = Title ? Title : L"Job"', 'propSheetHeader.pszCaption = Title ? Title : L"作业"'),
        ('PhpAddLimit(limitsLv, L"Desktop"', 'PhpAddLimit(limitsLv, L"桌面"'),
        ('propSheetHeader.pszCaption = L"Job"', 'propSheetHeader.pszCaption = L"作业"'),
        ('''pages[1] = PhCreateSecurityPage(
        L"Job",
        L"Job",
        Context->OpenObject,
        NULL,
        Context->Context
        );''', '''pages[1] = PhCreateSecurityPage(
        L"作业",
        L"作业",
        Context->OpenObject,
        NULL,
        Context->Context
        );''')
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/kdump.c", "utf-8", {
        "Size: ": "大小: ",
        "Initializing...": "初始化中...",
        "Live kernel dump has been created.": "已创建活动内核转储。",
        "Unable to save the live kernel dump.": "无法保存活动内核转储。",
        "Processing live kernel dump...": "正在处理活动内核转储...",
        "Dump files (*.dmp)": "转储文件 (*.dmp)",
        "All files (*.*)": "所有文件 (*.*)",
        "kerneldump": "内核转储",
        "Unable to create live kernel dump.": "无法创建活动内核转储",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/logwnd.c", "utf-8", {
        "Time": "时间",
        "Message": "消息",
        "Text files (*.txt)": "文本文档 (*.txt)",
        "All files (*.*)": "所有文件 (*.*)",
        "System Informer Log.txt": "System Informer 日志文件.txt",
        "Unable to create the file": "无法创建文件",
        "&Copy": "复制(&C)",
    }, [
        ('PhListView_AddColumn(ListViewContext, 1, 1, 1, LVCFMT_LEFT, 140, L"Type"',
         'PhListView_AddColumn(ListViewContext, 1, 1, 1, LVCFMT_LEFT, 140, L"类型"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/main.c", "utf-8", {
        "Warning.": "警告",
        "You are attempting to run the 32-bit version of System Informer on 64-bit Windows. ":
            "您尝试在 64 位 Windows 系统上运行 32 位版本的 System Informer。",
        "Most features will not work correctly.\n\n": "大多数功能将无法正常工作。\n\n",
        "Please run the 64-bit version of System Informer instead.": "请改用 64 位版本的 System Informer。",
        "Unable to create the window.": "无法创建窗口。",
        "Found previous instance window: %ls (%p)": "找到之前的实例窗口: %ls (%p)",
        "Foreground previous instance: %lu": "前一个实例: %lu",
        "Foreground previous instance: %lu (%lu attempts)": "前一个实例: %lu (尝试次数: %lu)",
        "Activate previous instance": "激活前一个实例",
        "Activate previous instance: %!STATUS!": "激活前一个实例: %!STATUS!",
        "Full\nA complete dump of the process, rarely needed most of the time.":
            "完全\n完整的进程转储，大多数情况下很少需要。",
        "Normal\nFor most purposes, this dump file is the most useful.": "正常\n在大多数情况下，此转储文件最为有用。",
        "Minimal\nA very limited dump with limited data.": "小型\n数据非常有限的转储文件。",
        "Restart\nRestart the application.": "重启\n重新启动应用程序。",
        "Ignore": "忽略",
        "Exit": "退出",
        "System Informer has crashed :(": "System Informer 已崩溃 :(",
        "System Informer has crashed :(\r\n\r\n%s": "System Informer 已崩溃 :(\r\n\r\n%s",
        "Do you want to create a minidump on the Desktop?": "是否要在桌面上创建小型转储文件?",
        "Unable to initialize desktop policy.": "无法初始化桌面策略。",
        "Unable to configure termination policy.": "无法配置终止策略。",
        "System Informer's settings file is corrupt. Do you want to reset it?":
            "System Informer 的设置文件已损坏。是否要重置设置?",
        "If you select No, the settings system will not function properly.":
            "如果选择“否”，设置系统将无法正常运行。",
        "Command line options:": "命令行选项:",
        "Unable to load the settings file.": "无法加载设置文件。",
        "Unable to convert settings to json format.": "无法将设置文件转换为 JSON 格式。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mainwnd.c", "utf-8", {
        "&Priority": "优先级(&P)",
        " (Administrator)": " (管理员)",
        "Processes": "进程",
        "Services": "服务",
        "Network": "网络",
        "Text files (*.txt;*.log)": "文本文件 (*.txt;*.log)",
        "Comma-separated values (*.csv)": "CSV 文件 (*.csv)",
        "All files (*.*)": "所有文件 (*.*)",
        "Unable to create the file": "无法创建文件",
        "Executable files (*.exe;*.dll;*.com;*.ocx;*.sys;*.scr;*.cpl;*.ax;*.acm;*.lib;*.winmd;*.mui;*.mun;*.efi;*.pdb)":
            "可执行文件 (*.exe;*.dll;*.com;*.ocx;*.sys;*.scr;*.cpl;*.ax;*.acm;*.lib;*.winmd;*.mui;*.mun;*.efi;*.pdb)",
        "Make sure the PE Viewer executable file is present.":
            "请确保 PE Viewer 可执行文件存在。",
        "Unable to shutdown WSL instances.": "无法终止 WSL 实例。",
        # todo: line 1543
        # todo: line 1555
        # todo: line 1567
        # todo: line 1579 ...... 1651
        "Unable to locate the file.": "无法定位文件。",
        "Unable to close the window.": "无法关闭窗口。",
        "Make sure the Explorer executable file is present.":
            "请确保资源管理器可执行文件存在。",
        "The process does not exist.": "进程不存在。",
        "The service does not exist.": "服务不存在。",
        "Unable to save application settings.": "无法保存应用程序设置。",
        "&Computer": "计算机(&C)",
        "&Lock": "锁定(&L)",
        "Log o&ff": "注销(&F)",
        "&Sleep": "睡眠(&S)",
        "&Hibernate": "休眠(&H)",
        "Update and restart": "更新并重启",
        "Update and shut down": "更新并关机",
        "R&estart": "重启(&E)",
        "Restart to advanced options": "重启至高级选项",
        "Restart to boot options": "重启至启动选项",
        "Restart to firmware options": "重启至固件选项",
        "Windows Defender Offline Scan": "Windows Defender 离线扫描",
        "Shu&t down": "关机(&T)",
        "H&ybrid shut down": "混合关机(&Y)",
        "R&estart (Native)": "重启 (本机) (&E)",
        "Shu&t down (Native)": "关机 (本机) (&T)",
        "R&estart (Critical)": "重启 (关键) (&E)",
        "Shu&t down (Critical)": "关机 (关键) (&T)",
        "&Run...\bCtrl+R": "运行(&R)...\bCtrl+R",
        "Run &as...\bCtrl+Shift+R": "以指定用户身份运行(&A)...\bCtrl+Shift+R",
        "Run as &package...\bCtrl+Shift+P": "以指定 UWP 应用包名运行(&P)...\bCtrl+Shift+P",
        "Show &details for all processes": "显示所有进程详细信息(&D)",
        "&Save...\bCtrl+S": "保存(&S)...\bCtrl+S",
        "&Find handles or DLLs...\bCtrl+F": "查找句柄或 DLL(&F)...\bCtrl+F",
        "&Options...": "选项(&O)...",
        "E&xit": "退出(&X)",
        "System &information\bCtrl+I": "系统信息(&I)\bCtrl+I",
        "&Tray icons": "托盘图标(&T)",
        "<section placeholder>": "<节占位符>",
        "&Always on top": "始终置顶(&A)",
        "&Opacity": "透明度(&O)",
        "&Opaque": "不透明(&O)",
        "&Refresh\bF5": "刷新(&R)\bF5",
        "Refresh i&nterval": "刷新间隔(&N)",
        "&Fast (0.5s)": "快 (0.5s) (&F)",
        "&Normal (1s)": "正常 (1s) (&N)",
        "&Below normal (2s)": "低于正常 (2s) (&B)",
        "&Slow (5s)": "慢 (5s) (&S)",
        "&Very slow (10s)": "非常慢 (10s) (&V)",
        "Refresh a&utomatically\bF6": "自动刷新(&U)\bF6",
        "&Create service...": "创建服务(&C)...",
        "&Create live dump...": "创建活动转储(&C)...",
        "Inspect e&xecutable file...": "检查可执行文件(&X)...",
        "&Search thread stacks": "搜索线程栈(&S)",
        "&Zombie processes": "僵尸进程(&Z)",
        "&Pagefiles": "页面文件(&P)",
        "Start &Task Manager": "启动任务管理器(&T)",
        "Start &Resource Monitor": "启动资源监视器(&R)",
        "T&erminate WSL processes": "终止 WSL 进程(&E)",
        "&Permissions": "权限(&P)",
        "Current Power Scheme": "当前电源方案",
        "Service Control Manager": "服务控制管理器",
        "Terminal Server Listener": "终端服务器监听器",
        "WMI Root Namespace": "WMI 根名称空间",
        "COM Access Permissions": "COM 访问权限",
        "COM Access Restrictions": "COM 访问限制",
        "COM Launch Permissions": "COM 启动权限",
        "COM Launch Restrictions": "COM 启动限制",
        "Current Window Desktop": "当前窗口所在桌面",
        "Current Window Station": "当前窗口站",  # haha, 当前窗口站的高级安全设置！
        "User list...": "用户列表...",
        "&Log\bCtrl+L": "日志(&L)\bCtrl+L",
        "Debu&g console": "调试控制台(&G)",
        "&About": "关于(&A)",
        "&System": "系统(&S)",
        "&View": "查看(&V)",
        "&Tools": "工具(&T)",
        "&Users": "用户(&U)",
        "&Help": "帮助(&H)",
        "Column Set Name": "列集名称",
        "Enter a name for this column set:": "输入该列集的名称:",
        "N&otifications": "通知(&O)",
        "&Enable all": "全部启用(&E)",
        "&Disable all": "全部禁用(&D)",
        "New &processes": "新进程(&P)",
        "T&erminated processes": "已终止进程(&E)",
        "New &services": "新服务(&S)",
        "St&arted services": "已启动服务(&A)",
        "St&opped services": "已停止服务(&O)",
        "&Deleted services": "已删除服务(&D)",
        "&Modified services": "已修改服务(&M)",
        "&Arrived devices": "已就绪设备(&A)",
        "&Removed devices": "已移除设备(&R)",
        "Settings": "设置",
        "Enable initialization delay": "启用延迟初始化",
        "Enable persistent layout": "启用持久布局",
        "Enable transparent icons": "启用透明图标",
        "Enable single click icons": "启用单击图标",
        "Reset persistent layout": "重置持久布局",
        "&Show/Hide System Informer": "显示/隐藏 System Informer(&S)",
        "System &information": "系统信息(&I)",
        "&Processes": "进程(&P)",
        " (Unavailable)": " (不可用)",
        "&Priority class": "优先级类(&P)",
        "&Real time": "实时(&R)",
        "&High": "高(&H)",
        "&Above normal": "高于正常(&A)",
        "&Normal": "正常(&N)",
        "&Below normal": "低于正常(&B)",
        "&Idle": "空闲(&I)",
        "&I/O priority": "I/O 优先级(&I)",
        "&Low": "低(&L)",
        "&Very low": "非常低(&V)",
        "T&erminate": "终止(&E)",
        "&Suspend": "挂起(&S)",
        "Res&tart": "重新启动(&T)",
        "Res&ume": "恢复(&U)",
        "P&roperties": "属性(&R)",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memedit.c", "utf-8", {
        "Unable to edit the memory region.": "无法编辑内存区域。",
        "Unable to read memory": "无法读取内存",
        "Unable to open the process": "无法打开进程",
        "%u bytes per row": "%u 字节每行",  # 此处的翻译有点别扭，但是必须保持 %u 第一位，否则更改选项会失效（源码设计问题，典型的前后端不分）
                                            # https://github.com/org-220623/systeminformer-chinese-scripts/issues/24
        "Binary files (*.bin)": "二进制文件 (*.bin)",
        "All files (*.*)": "所有文件 (*.*)",
        "Unable to create the file": "无法创建文件",
        "Go to Offset": "转到",
        "Enter an offset:": "输入偏移量:",
        "write": "写入",
        "process memory": "进程内存",
        "Some programs may restrict access or ban your account when editing the memory of the process.":
            "某些程序在编辑进程内存时可能会限制访问或封禁您的帐户。",
        "Unable to write memory": "无法写入内存",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memlist.c", "utf-8", {
        "Base address": "基址",
        "Size": "大小",
        "Protection": "保护",
        "Use": "用量",
        "Total WS": "工作集总计",
        "Private WS": "私有工作集",
        "Shareable WS": "可共享工作集",
        "Shared WS": "已共享工作集",
        "Locked WS": "已锁定工作集",
        "Committed": "已提交",
        "Private": "私有",
        "Signing level": "签名级别",
        "Original protection": "原始保护级别",
        "Original pages": "原始页面",
        "Region type": "区域类型",
        "Priority": "优先级",
        "32-bit": "32 位",
        "TEB%s (thread %lu)": "TEB%s (线程 %lu)",
        " 32-bit": " (32 位)",
        "Stack%s (thread %lu)": "栈%s (线程 %lu)",
        "Heap": "堆",
        "%s Segment%s (ID %lu)": "%s 段%s (ID %lu)",
        "CFG Bitmap%s": "CFG 位图%s",
        "ApiSetMap": "API 集映射",
        "CSR shared memory": "CSR 共享内存",
        "CodePage data": "代码页数据",
        "GDI shared handle table": "GDI 共享句柄表",
        "Shim data": "填充码数据",
        "Process activation context data": "进程激活上下文数据",
        "System activation context data": "系统激活上下文数据",
        "Activation context data": "激活上下文数据",
        "WER registration data": "WER 注册数据",
        "Silo shared data": "Silo 共享数据",
        "Telemetry coverage map": "遥测覆盖映射",
        "Free (Unusable)": "空闲 (不可用)",
        "Free": "空闲",
    }, [
        ('PhAddTreeNewColumn(TreeNewHandle, PHMMTLC_TYPE, TRUE, L"Type"',
         'PhAddTreeNewColumn(TreeNewHandle, PHMMTLC_TYPE, TRUE, L"类型"')
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memlists.c", "utf-8", {
        "Unknown": "未知",
        "Working sets emptied.": "工作集已清空。",
        "Unable to empty working sets.": "无法清空工作集。",
        "Modified page lists emptied.": "已修改页面列表已清空。",
        "Unable to empty modified page lists.": "无法清空已修改页面列表。",
        "Standby lists emptied.": "待命列表已清空。",
        "Unable to empty standby lists.": "无法清空待命列表。",
        "Priority 0 standby list emptied.": "优先级 0 待命列表已清空。",
        "Unable to empty priority 0 standby list.": "无法清空优先级 0 待命列表。",
        "Memory pages combined: ": "已合并内存页面: ",
        " pages)": " 页面)",
        "Unable to combine memory pages.": "无法合并内存页面。",
        "Emptying the compression store requires a connection to the kernel driver.":
            "清空压缩存储需要连接到内核驱动程序。",
        "Compression stores emptied.": "压缩缓存数据已清空。",
        "Unable to empty compression stores.": "无法清空压缩缓存数据。",
        "Registry cache emptied.": "注册表缓存已清空。",
        "Unable to empty registry cache.": "无法清空注册表缓存。",
        "System file cache emptied: ": "已清空系统文件缓存: ",
        "Unable to empty system file cache.": "无法清空系统文件缓存。",
        "Volume file cache flushed to disk.": "卷文件缓存已刷新到磁盘。",
        "Unable to flush volume file cache.": "无法刷新卷文件缓存。",
        "Combining memory pages...": "正在合并内存页面...",
        "Combining memory pages ...": "正在合并内存页面...",
        "Emptying compression store...": "正在清空压缩缓存数据...",
        "Emptying compression store ...": "正在清空压缩缓存数据...",
        "Emptying system file cache ...": "正在清空系统文件缓存...",
        "Emptying system file cache...": "正在清空系统文件缓存...",
        "Emptying registry cache...": "正在清空注册表缓存...",
        "Emptying registry cache ...": "正在清空注册表缓存...",
        "Emptying working sets...": "正在清空工作集...",
        "Emptying working sets ...": "正在清空工作集...",
        "Emptying modified page list...": "正在清空已修改页面列表...",
        "Emptying modified page list ...": "正在清空已修改页面列表...",
        "Emptying modified file cache...": "正在清空已修改文件缓存...",
        "Emptying modified file cache ...": "正在清空已修改文件缓存...",
        "Emptying standby list...": "正在清空待命列表...",
        "Emptying standby list ...": "正在清空待命列表...",
        "Emptying priority 0 standby list...": "正在清空优先级 0 待命列表...",
        "Emptying priority 0 standby list ...": "正在清空优先级 0 待命列表...",
        "Unable to create the window.": "无法创建窗口。",
        "Executing memory commands...": "正在执行内存命令...",
        "Executing memory commands ...": "正在执行内存命令...",
        "Executing memory command...": "正在执行内存命令...",
        "Executing memory command ...": "正在执行内存命令...",
        "&Combine memory pages": "合并内存页面",
        "Empty &compression cache": "清空压缩缓存数据",
        "Empty system &file cache": "清空系统文件缓存",
        "Empty &registry cache": "清空注册表缓存",
        "Empty &working sets": "清空工作集",
        "Empty &modified page list": "清空已修改页面列表",
        "Empty &modified file cache": "清空已修改文件缓存",
        "Empty &standby list": "清空待命列表",
        "Empty &priority 0 standby list": "清空优先级 0 待命列表",
        "Empty &all": "清空全部",
        "Unable to empty the memory list.": "无法清空内存列表。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memmod.c", "utf-8", {
        "Resolving symbols...": "正在解析符号...",
        "Index": "索引",
        "ImageBase": "映像基址",
        "Offset": "偏移",
        "Address": "地址",
        "Symbol": "符号",
        "Unable to perform the scan": "无法执行扫描",
        "&Copy": "复制(&C)",
        "Unable to open the process.": "无法打开进程。",

    }, [
        ('PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 100, L"File")',
         'PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 100, L"文件")'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memprot.c", "utf-8", {
        "Possible values:\r\n": "可能的值:\r\n",
        "Modifiers:\r\n": "修改器:\r\n",
        "Unable to change memory protection": "无法更改内存保护选项",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memprv.c", "utf-8", {
        "Unknown": "未知",
        "Private": "私有",
        "Mapped": "已映射",
        "Image": "映像",
        "Commit": "提交",
        "Reserved": "保留",
        "Free": "空闲",
        "Unchecked": "未检查",
        "Unsigned": "未签名",
        # todo 137 - 150
        "Lowest": "最低",
        "Very low": "非常低",
        "Low": "低",
        "Medium": "中",
        "Below normal": "低于正常",
        "Normal": "正常",
        "Above normal": "高于正常",
        "High": "高",
        "Private, ":            "私有, ",
        "MappedDataFile, ":     "已映射数据文件, ",
        "MappedImage, ":        "已映射映像, ",
        "MappedPageFile, ":     "已映射页面文件, ",
        "MappedPhysical, ":     "已映射物理内存, ",
        "DirectMapped, ":       "直接映射, ",
        "Software enclave, ":   "软件飞地, ",
        "PageSize64K, ":        "64KiB 页面, ",
        "Placeholder, ":        "占位符, ",
        "Mapped AWE, ":         "已映射 AWE, ",
        "MappedWriteWatch, ":   "已映射写入视图, ",
        "PageSizeLarge, ":      "大页面, ",
        "PageSizeHuge, ":       "巨型页面, ",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memrslt.c", "utf-8", {
        "Filter": "筛选器",
        "Enter the filter pattern:": "输入筛选规则:",
        "Unable to compile the regular expression.": "无法编译正则表达式。",
        pre_format_string("\"%s\" at position %zu."): pre_format_string("\"%s\" 位于 %zu。"),
        "Unknown error": "未知错误",
        "Results - %s (%u)": "结果 - %s (%u)",
        "Address": "地址",
        "Base Address": "基址",
        "Length": "长度",
        "Result": "结果",
        "%s results.": "%s 个结果。",
        "Text files (*.txt)": "文本文档 (*.txt)",
        "All files (*.*)": "所有文件 (*.*)",
        "Search results.txt": "搜索结果.txt",
        "Unable to create the file": "无法创建文件",
        "Contains...": "包含...",
        "Contains (case-insensitive)...": "包含 (不区分大小写)...",
        "Regex...": "正则表达式...",
        "Regex (case-insensitive)...": "正则表达式 (不区分大小写)...",
        "Unable to edit memory": "无法编辑内存",
        "Read/Write memory": "读取/写入内存",
        "Copy": "复制",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memsrch.c", "utf-8", {
        "Unable to open the process": "无法打开进程",
        "Unable to search for strings.": "无法搜索字符串。",
        "The minimum length must be at least 4.": "最小长度必须至少为 4。",
        "%s strings found...": "已找到 %s 个字符串...",
        "Searching memory strings...": "正在搜索内存中的字符串...",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/memsrcht.c", "utf-8", {
        "There are no strings to display.": "没有要显示的字符串。",
        "Loading strings...": "正在加载字符串...",
        "Unable to clone the process": "无法克隆进程",
        "Base address": "基址",
        "Address": "地址",
        "Length": "长度",
        "String": "字符串",
        "Protection": "保护",
        "Memory type": "内存类型",
        "Unable to update the length.": "无法更新长度。",
        "The minimum length is invalid.": "最小长度无效。",
        " Strings": " 个字符串",
        "Unable to edit memory": "无法编辑内存",
        "Search Strings (Ctrl+K)": "搜索字符串 (Ctrl+K)",
        "Searching... ": "正在搜索... ",
        " strings": " 个字符串",
        "Read/Write memory": "读取/写入内存",
        "Copy": "复制",
        "Extended character set": "扩展字符集",
        "Private": "私有",
        "Image": "映像",
        "Mapped": "已映射",
        "Minimum length...": "最小长度...",
        "Zero pad addresses": "地址补零",
        "Refresh\bF5": "刷新\bF5",
        "Unable to open the process": "无法打开进程",
        "Unable to create the window.": "无法创建窗口。",
    }, [
        ('PhAddTreeNewColumnEx2(TreeNewHandle, PH_MEMSTRINGS_TREE_COLUMN_ITEM_TYPE, TRUE, L"Type"',
         'PhAddTreeNewColumnEx2(TreeNewHandle, PH_MEMSTRINGS_TREE_COLUMN_ITEM_TYPE, TRUE, L"类型"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/miniinfo.c", "utf-8", {
        "Commit charge": "提交用量",
        "Physical memory": "物理内存",
        "&Opacity": "透明度(&O)",
        "Opaque": "不透明",
        "&Refresh\bF5": "刷新(&R)\bF5",
        "Refresh a&utomatically\bF6": "自动刷新(&U)\bF6",
        "%s (%u processes)": "%s (%u 个进程)",
        "(Not responding) ": "(未响应) ",
        "(Terminated) ": "(已终止) ",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "&Go to process": "转到进程(&G)",
        "&Go to processes": "转到进程(&G)",
        "The process does not exist.": "进程不存在。",
        "Commit    ": "提交    ",
        "Private bytes": "私有字节",
        "Physical    ": "物理内存    ",
        "Working set": "工作集",
    }, [
        ('PhAddTreeNewColumnEx2(listSection->TreeNewHandle, MIP_SINGLE_COLUMN_ID, TRUE, L"Process"',
         'PhAddTreeNewColumnEx2(listSection->TreeNewHandle, MIP_SINGLE_COLUMN_ID, TRUE, L"进程"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/modlist.c", "utf-8", {
        "Name": "名称",
        "Base address": "基址",
        "Size": "大小",
        "Description": "描述",
        "Company name": "发行商名称",
        "Version": "版本",
        "File name": "文件名",
        "Load count": "加载计数",
        "Verification status": "验证状态",
        "Verified signer": "已验证的签名方",
        "Time stamp": "时间戳",
        "CF Guard": "CFG",
        "Load time": "加载时间",
        "Load reason": "加载原因",
        "File modified time": "文件修改时间",
        "File size": "文件大小",
        "Entry point": "入口点",
        "Parent base address": "父进程基址",
        "Image coherency": "映像一致性",
        "Timeline": "时间线",
        "Original name": "原始名称",
        "Service": "服务",
        "Enclave type": "飞地类型",
        "Enclave base address": "飞地基址",
        "Enclave size": "飞地大小",
        "Architecture": "架构",
        "Static": "静态",
        "Image digital signature support disabled.": "映像数字签名支持已禁用。",
        "XF Guard": "XFG",
        "Dynamic": "动态",
        "Image coherency support is disabled.": "映像一致性支持已禁用。",
        "Scanning....": "正在扫描...",
    }, [
        ('PhAddTreeNewColumn(Context->TreeNewHandle, PHMOTLC_TYPE, FALSE, L"Type"',
         'PhAddTreeNewColumn(Context->TreeNewHandle, PHMOTLC_TYPE, FALSE, L"类型"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/modprv.c", "utf-8", {
        "Unknown": "未知",
        "Mapped file": "映射文件",
        "Kernel module": "内核模块",
        "Mapped image": "映射映像",
        "Enclave module": "飞地模块",
        "Static dependency": "静态依赖项",
        "Static forwarder dependency": "静态转发器依赖项",
        "Dynamic forwarder dependency": "动态转发器依赖项",
        "Delay load dependency": "延迟加载依赖项",
        "Dynamic": "动态",
        "As image": "作为映像",
        "As data": "作为数据",
        "Enclave primary": "飞地安全区",
        "Enclave dependency": "飞地依赖项",
        "Patch image": "补丁映像",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mtgndlg.c", "utf-8", {
        "Unable to open the process.": "无法打开进程。",
        "Policy": "策略",
        "Loader Integrity": "加载器完整性",
        "OS signing levels for dependent module loads are enabled.": "已启用依赖模块加载的操作系统签名级别。",
        "Module Tampering": "模块防篡改",
        "Module Tampering protection is enabled.": "模块防篡改保护已启用。",
        "Indirect branch prediction": "间接分支预测",
        "Protects against sibling hardware threads (hyperthreads) from interfering with indirect branch predictions.":
            "防止同级硬件线程 (超线程) 干扰间接分支预测。",
        "Dynamic code (downgrade)": "动态代码 (降级)",
        "Allows a broker to downgrade the dynamic code policy for a process.": "允许代理降低进程的动态代码策略。",
        "Speculative store bypass": "推测性存储绕过",
        "Disables spectre mitigations for the process.": "禁用该进程的 Spectre 缓解措施。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mwpgdev.c", "utf-8", {
        "Unclassified": "未分类",
        "Unnamed": "未命名",
        " Device Removed": " 设备已移除",
        " Device Arrived": " 设备已就绪",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mwpgnet.c", "utf-8", {
        "Network": "网络",
        "&Hide waiting connections": "隐藏正在等待的连接(&H)",
        "&Go to process\bEnter": "转到进程(&G)\bEnter",
        "Go to service": "转到服务",
        "C&lose": "关闭(&L)",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mwpgproc.c", "utf-8", {
        "&Priority": "优先级(&P)",
        "Processes": "进程",
        "&Collapse all": "全部收起(&C)",
        "&Expand all": "全部展开(&E)",
        "&Hide processes from other users": "隐藏其他用户进程(&H)",
        "Hide si&gned processes": "隐藏已签名进程(&G)",
        "Hide &system processes": "隐藏系统进程(&S)",
        "Scrol&l to new processes": "滚动到新进程(&L)",
        "Sort &child processes": "排序子进程(&C)",
        "Sort &root processes": "排序根进程(&R)",
        "Show CPU &below 0.01": "显示 CPU 使用率低于 0.01% 的记录(&B)",
        "Organi&ze column sets...": "组织列集(&Z)...",
        "Sa&ve column set...": "保存列集(&V)...",
        "Loa&d column set": "加载列集(&D)",
        "This filter cannot function because digital signature checking is not enabled.\r\n%s":
            "由于未启用数字签名检查，此筛选器无法正常工作。\r\n%s",
        "Enable it in Options > General and restart System Informer.":
            "请在“选项”>“常规”中启用此功能，然后重启 System Informer。",
        "T&erminate\bDel": "结束进程(&E)\bDel",
        "Terminate tree\bShift+Del": "结束进程树\bShift+Del",
        "&Suspend": "挂起进程(&S)",
        "Suspend tree": "挂起进程树",
        "Res&ume": "恢复进程(&U)",
        "Resume tree": "恢复进程树",
        "Freeze": "深度冻结进程",
        "Thaw": "解冻进程",
        "Res&tart": "重新启动(&T)",
        "Create live kernel dump fi&le": "创建活动内核转储文件(&L)",
        "&Minimal...": "小型(&M)...",
        "&Normal...": "正常(&N)...",
        "&Full...": "完整(&F)...",
        "&Custom...": "自定义(&C)...",
        "Create dump fi&le": "创建转储文件(&L)",
        "&Limited...": "受限(&L)...",
        "De&bug": "调试(&B)",
        "&Affinity": "处理器相关性(&A)",
        "&Priority class": "优先级类(&P)",
        "&Real time": "实时(&R)",
        "&High": "高(&H)",
        "&Above normal": "高于正常(&A)",
        "&Normal": "正常(&N)",
        "&Below normal": "低于正常(&B)",
        "&Idle": "空闲(&I)",
        "&I/O priority": "I/O 优先级(&I)",
        "&Low": "低(&L)",
        "&Very low": "非常低(&V)",
        "Pa&ge priority": "页面优先级(&G)",
        "&Medium": "中(&M)",
        "&Miscellaneous": "其他选项(&M)",
        "Activity moderation": "活动审核",
        "&Critical": "关键(&C)",
        "&Detach from debugger": "断开与调试器的连接(&D)",
        "Efficiency mode": "节能模式",
        "Execution required": "执行所需状态",
        "GDI &handles...": "GDI 句柄(&H)...",
        "Heaps...": "堆...",
        "Locks...": "锁...",
        "Flush heaps": "刷新堆",
        "Modified pages...": "已修改页面...",
        "Reduce working &set": "减小工作集(&S)",
        "&Run as...": "以指定用户身份运行(&R)...",
        "Run &as this user...": "以当前用户身份运行(&A)...",
        "Virtuali&zation": "虚拟化(&Z)",
        "&Window": "窗口(&W)",
        "Bring to &front": "置于顶层(&F)",
        "&Restore": "恢复(&R)",
        "M&inimize": "最小化(&I)",
        "M&aximize": "最大化(&A)",
        "&Close": "关闭(&C)",
        "Search &online\bCtrl+M": "在线搜索(&O)\bCtrl+M",
        "Open &file location\bCtrl+Enter": "打开文件所在位置(&F)\bCtrl+Enter",
        "P&roperties\bEnter": "属性(&R)\bEnter",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        "The process ": "进程 ",
        ") was created by ": ") 已被以下进程创建: ",
        "Unknown process": "未知进程",
        "Process Created": "进程已创建",
        ") was terminated with status 0x": ") 已被终止，退出代码 0x",
        "Process Terminated": "进程已终止",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mwpgsrv.c", "utf-8", {
        "Services": "服务",
        "Hide default services": "隐藏默认服务",
        "&Hide driver services": "隐藏驱动程序服务(&H)",
        "&Start": "启动(&S)",
        "C&ontinue": "继续运行(&O)",
        "&Pause": "暂停(&P)",
        "S&top": "停止(&T)",
        "&Delete\bDel": "删除(&D)\bDel",
        "&Go to process": "转到进程(&G)",
        "Open &key": "打开注册表键(&K)",
        "Open &file location\bCtrl+Enter": "打开文件所在位置(&F)\bCtrl+Enter",
        "P&roperties\bEnter": "属性(&R)\bEnter",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        "The service ": "服务 ",
        ") was created": ") 已创建",
        "Service Created": "服务已创建",
        ") was started": ") 已启动",
        "Service Started": "服务已启动",
        ") was stopped": ") 已停止",
        "Service Stopped": "服务已停止",
        ") was modified": ") 已修改",
        "Service Modified": "服务已修改",
        ") was deleted": ") 已删除",
        "Service Deleted": "服务已删除",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/netlist.c", "utf-8", {
        "Name": "名称",
        "Local address": "本地地址",
        "Local port": "本地端口",
        "Remote address": "远程地址",
        "Remote port": "远程端口",
        "Protocol": "协议",
        "State": "状态",
        "Owner": "所有者",
        "Time stamp": "时间戳",
        "Local hostname": "本地宿主机名称",
        "Remote hostname": "远程宿主机名称",
        "Timeline": "时间线",
        "Hyper-V service": "Hyper-V 服务",
        "Resolving....": "正在解析...",
        "Connected": "已连接",
        "Listen": "监听",
        "Unknown process": "未知进程",
        "Waiting connections": "等待连接",
        "Unable to perform the operation.": "无法执行此操作。",
        "This node cannot be displayed because it is currently hidden by your active filter settings or preferences.":
            "此节点无法显示，因为它当前已被您启用的筛选器设置或偏好设置隐藏。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/netprv.c", "utf-8", {
        "Network provider run count: %lu": "网络提供程序运行次数: %lu",
        "Failed to get network connections: %lu": "获取网络连接失败: %lu",
        "Unknown": "未知",
        "Closed": "已关闭",
        "Listen": "监听",
        "SYN sent": "SYN 已发送",
        "SYN received": "SYN 已接收",
        "Established": "已建立连接",
        "FIN wait 1": "FIN 等待状态 1",
        "FIN wait 2": "FIN 等待状态 2",
        "Close wait": "关闭等待",
        "Closing": "正在关闭",
        "Last ACK": "最后 ACK",
        "Time wait": "时间等待",
        "Delete TCB": "删除 TCB",
        "Bound": "已绑定",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/netstk.c", "utf-8", {
        "Unable to open the process.": "无法打开进程。",
        "Name": "名称",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/notifico.c", "utf-8", {
        "CPU &usage": "CPU 使用量(&U)",
        "CPU &history": "CPU 历史(&H)",
        "&I/O history": "I/O 历史(&I)",
        "&Commit charge history": "提交用量历史(&C)",
        "&Physical memory history": "物理内存历史(&P)",
        "CPU usage (text)": "CPU 使用量 (文本)",
        "IO usage (text)": "I/O 用量 (文本)",
        "Commit usage (text)": "提交用量 (文本)",
        "Physical usage (text)": "物理内存用量 (文本)",
        "System Informer icon (static)": "System Informer 图标 (静态)",
        "CPU history: ": "CPU 历史: ",
        "Commit: ": "提交: ",
        "Physical memory: ": "物理内存: ",
        "CPU usage: ": "CPU 使用量: ",
        "CPU usage: %.2f%%%s": "CPU 使用量: %.2f%%%s",
        "Commit charge": "提交用量",
        "Physical memory": "物理内存",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/ntobjprp.c", "utf-8", {
        "Unknown": "未知",
        "Notification": "通知"
                        "对象",
        "Synchronization": "同步"
                           "对象",
        "True": "是",
        "False": "否",
        "Unable to open the event": "无法打开事件对象",
        "Unable to open the event pair": "无法打开事件对",
        "Unable to open the semaphore": "无法打开信号量",
        "Unable to open the timer": "无法打开计时器",
        "Viewing active mappings requires a connection to the kernel driver.":
            "查看活动映射需要连接到内核驱动程序。",
        "The process does not exist.": "进程不存在。",
        "View": "查看",
        "Start": "开始",
        "End": "结束",
        "Size": "大小",
        "&Go to process": "转到进程(&G)",
        "&Copy": "复制(&C)",
        "None": "无",
        "%s ago (%s)": "%s 以前 (%s)",
        "Unlimited": "未限制",
        "N/A (not connected)": "N/A (未连接)",
        "Name": "名称",
        "Value": "值",
        "Shared Winsock context": "共享 Winsock 上下文",
        "Socket state": "套接字状态",
        "Socket type": "套接字类型",
        "Address family": "地址家族",
        "Protocol": "协议",
        "Catalog entry ID": "目录条目 ID",
        "Provider ID": "提供者 ID",
        "Provider flags": "提供者标志",
        "Service flags": "服务标志",
        "Send timeout": "发送超时",
        "Receive timeout": "接收超时",
        "Send buffer size": "发送缓冲区大小",
        "Receive buffer size": "接收缓冲区大小",
        "Creation flags": "创建标志",
        "Flags": "标志",
        "Addresses": "地址",
        "Local address": "本地地址",
        "Remote address": "远程地址",
        "AFD info classes": "AFD 信息类",
        "Connect time": "连接时间",
        "Delivery available": "可交付",
        "Pending receive requests": "挂起的接收请求",
        "Pending sends": "挂起的发送",
        "Receive window size": "接收窗口大小",
        "Send window size": "发送窗口大小",
        "Maximum send size": "最大发送大小",
        "Group ID": "组 ID",
        "Group type": "组类型",
        "TDI devices": "TDI 设备",
        "TDI address device": "TDI 地址设备",
        "TDI connection device": "TDI 连接设备",
        "Socket-level options": "套接字级别选项",
        "Reuse address": "重用地址",
        "Keep alive": "保持活动",
        "Don't route": "不路由",
        "Broadcast": "广播",
        "OOB in line": "带外路由",
        "Maximum message size": "最大消息长度",
        "Pause accept": "暂停接收",
        "Compartment ID": "区间 ID",
        "Randomize port": "随机端口",
        "Port scalability": "端口可扩展性",
        "Reuse unicast port": "重用单播端口",
        "Exclusive address use": "独占地址使用",
        "IP-level options": "IP 级别选项",
        "Header included": "包含的头部",
        "Type-of-service": "服务类型",
        "Unicast TTL": "单播 TTL",
        "Multicast interface": "多播接口",
        "Multicast TTL": "多播 TTL",
        "Multicast loopback": "多播环回",
        "Don't fragment": "不分片",
        "Receive packet info": "接收数据包信息",
        "Receive TTL": "接收 TTL",
        "Broadcast reception": "广播接收",
        "IPv6 protection level": "IPv6 保护级别",
        "Receive arrival interface": "接收到达接口",
        "Receive dest. address": "接收目标地址",
        "IPv6-only": "仅 IPv6",
        "Interface list": "接口列表",
        "Unicast interface": "单播接口",
        "Receive routing header": "接收路由报头",
        "Receive type-of-service": "接收服务类型",
        "Original arrival interface": "原始到达接口",
        "Receive ECN": "接收 ECN",
        "Recveive ext. packet info": "接收扩展数据包信息",
        "WFP redirect records": "WFP 重定向记录",
        "WFP redirect context": "WFP 重定向上下文",
        "MTU discovery": "MTU 发现",
        "Path MTU": "路径 MTU",
        "Receive ICMP errors": "接收 ICMP 错误",
        "Upper MTU bound": "MTU 上限",
        "TCP-level options": "TCP 级别选项",
        "No delay": "无延迟",
        "Expedited data": "加速数据",
        "Maximum segment size": "最大段大小",
        "Retry timeout": "重试超时",
        "URG interpretation": "URG 解释",
        "No URG": "无 URG",
        "At mark": "标记位置",
        "No SYN retries": "无 SYN 重试",
        "Timestamps": "时间戳",
        "Congestion algorithm": "拥塞算法",
        "Delay FIN ACK": "延迟 FIN ACK",
        "Retry timeout (precise)": "重试超时 (精确)",
        "Fast open": "快速打开",
        "Keep alive count": "保持活动计数",
        "Keep alive interval": "保持活动间隔",
        "Fail on ICMP error": "遇到 ICMP 错误时失败",
        "TCP information": "TCP 信息",
        "TCP state": "TCP 状态",
        "Connection time": "连接时间",
        "Timestamps enabled": "已启用时间戳",
        "Estimated round-trip": "预计往返时间",
        "Minimal round-trip": "最小往返时间",
        "Bytes in flight": "传输中的字节数",
        "Congestion window": "拥塞窗口",
        "Send window": "发送窗口",
        "Receive window": "接收窗口",
        "Receive buffer": "接收缓冲区",
        "Bytes sent": "发送字节",
        "Bytes received": "接收字节",
        "Bytes reordered": "字节重排序",
        "Bytes retransmitted": "重传字节",
        "Fast retransmits": "快速重传",
        "Duplicate ACKs": "重复 ACK",
        "Timeout episodes": "超时次数",
        "SYN retransmits": "SYN 重传",
        "Receiver-limited episodes": "接收方限制次数",
        "Receiver-limited time": "接收方限制时间",
        "Receiver-limited bytes": "接收方限制字节",
        "Congestion-limited episodes": "受拥塞限制次数",
        "Congestion-limited time": "受拥塞限制时间",
        "Congestion-limited bytes": "受拥塞限制字节",
        "Sender-limited episodes": "发送方限制次数",
        "Sender-limited time": "发送方限制时间",
        "Sender-limited bytes": "发送方限制字节",
        "Out-of-order packets": "乱序数据包",
        "ECN negotiated": "ECN 协商",
        "ECE ACKs": "ECE ACK",
        "Probe timeout episodes": "探测超时次数",
        "UDP-level options": "UDP 级别选项",
        "No checksum": "无校验和",
        "Maximum coalesced size": "最大合并大小",
        "Hyper-V-level options": "Hyper-V 级别选项",
        "Connect timeout": "连接超时",
        "Container passthru": "容器直通",
        "Connected suspend": "连接挂起",
        "High VTL": "高 VTL",
    }, [
        ('PhAddListViewItem(Context->ListViewHandle, MAXINT, L"Session", info)',
         'PhAddListViewItem(Context->ListViewHandle, MAXINT, L"会话", info)'),
        ('PhAddListViewItem(Context->ListViewHandle, MAXINT, L"System", info)',
         'PhAddListViewItem(Context->ListViewHandle, MAXINT, L"系统", info)'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/options.c", "utf-8", {
        # Debugger 是 IFEO 选项，不能翻译！
        "General": "常规",
        "Advanced": "高级",
        "Highlighting": "高亮显示",
        "Graphs": "图像",
        "Plugins": "插件",
        "Do you want to reset all settings and restart System Informer?":
            "是否要重置所有设置并重新启动 System Informer?",
        "Do you want to clean up unused settings?":
            "是否要清理未使用的设置?",
        "Do you want to restore the default Windows Task Manager?":
            "是否要恢复默认的 Windows 任务管理器?",
        "Do you want to make System Informer the default Windows Task Manager?":
            "是否要将 System Informer 设置为默认的 Windows 任务管理器?",
        "Changing the default Task Manager": "更改默认任务管理器",
        "Unable to replace Task Manager": "无法替换任务管理器",
        "System Informer is the default Task Manager:": "System Informer 已是默认任务管理器:",
        "Restore default...": "恢复默认设置...",
        "System Informer is not the default Task Manager:": "System Informer 不是默认任务管理器:",
        "Make default...": "设置为默认...",
        "Allow only one instance": "仅允许单一实例",
        "Hide when closed": "关闭窗口时隐藏",
        "Hide when minimized": "最小化窗口时隐藏",
        "Start when I log on": "用户登录时自动启动",
        "Start hidden": "启动时隐藏",
        "Enable warnings": "启用警告",
        "Enable kernel-mode driver": "启用内核模式驱动程序",
        "Enable monospace fonts": "启用等宽字体",
        "Enable Plugins": "启用插件",
        "Enable undecorated symbols": "启用未修饰符号",
        "Enable AVX extensions (experimental)": "启用 AVX 扩展 (实验性功能)",
        "Enable AVX extensions": "启用 AVX 扩展",
        "Enable AVX extensions ": "启用 AVX 扩展 ",
        "Enable column header totals (experimental)": "启用列标题总计 (实验性功能)",
        "Enable column header totals ": "启用列标题总计 ",
        "Enable column header totals": "启用列标题总计",
        "Enable cycle-based CPU usage": "启用基于周期的 CPU 使用率",
        "Enable fixed graph scaling (experimental)": "启用固定图形缩放 (实验性功能)",
        "Enable fixed graph scaling ": "启用固定图形缩放 ",
        "Enable fixed graph scaling": "启用固定图形缩放",
        "Enable tray information window": "启用托盘信息窗口",
        "Enable new memory strings dialog": "启用新内存字符串对话框",
        "Remember last selected window": "记住上次选择的窗口",
        "Enable theme support (experimental)": "启用主题支持 (实验性功能)",
        "Enable theme support ": "启用主题支持 ",
        "Enable theme support": "启用主题支持",
        "Enable start as admin (experimental)": "启用以管理员身份运行选项 (实验性功能)",
        "Enable start as admin ": "启用以管理员身份运行选项 ",
        "Enable start as admin": "启用以管理员身份运行选项",
        "Enable streamer mode (disable window capture) (experimental)":
            "启用串流模式 (禁用窗口捕获) (实验性功能)",
        "Enable Windows subsystem for Linux support": "启用适用于 Linux 的 Windows 子系统支持",
        "Resolve network addresses": "解析网络地址",
        "Resolve DNS over HTTPS (DoH)": "解析 DNS over HTTPS (DoH)",  # DNS over HTTPS 是专有名词
        "Show tooltips instantly": "显示工具提示文本框",
        "Check images for coherency": "检查映像一致性",
        "Check images for digital signatures": "检查映像数字签名",
        "Check services for digital signatures": "检查服务数字签名",
        "Single-click tray icons": "启用单击托盘图标",
        "Icon click toggles visibility": "点击图标切换显示/隐藏",
        "Include usage of collapsed processes": "包含已折叠进程资源使用情况",
        "Show advanced options": "显示高级选项",
        "One or more options you have changed requires a restart of System Informer.":
            "您更改的一个或多个选项需要重启 System Informer。",
        "Do you want to restart System Informer now?":
            "是否立即重启 System Informer?",
        "WARNING: You have not installed System Informer into a secure location.":
            "警告: 您尚未将 System Informer 安装到安全的文件系统位置。",
        "%s is not recommended when running System Informer from outside a secure location (e.g. Program Files).\r\n\r\nAre you sure you want to continue?":
            "从非安全位置 (例如 Program Files 文件夹) 运行 System Informer 时，不建议%s。\r\n\r\n确定要继续吗?",
        "Name": "名称",
        "Unable to configure this option.": "无法配置此选项。",
        "You need to enable at minimum one tray icon (View menu > Tray Icons) before enabling the hide option.":
            "您必须至少启用一个托盘图标 (“查看”菜单 > “托盘图标”)，然后才能启用隐藏选项。",
        "Unable to enable option start as admin.": r"无法启用\"以管理员身份运行\"选项。",
        "You need to enable this option with administrative privileges.":
            "您需要使用管理员权限启用此选项。",
        "Enabling the 'start as admin' option": r"正在启用\"以管理员身份启动\"选项",
        "Unable to enable start as admin.": r"无法启用\"以管理员身份运行\"选项。",
        "Setting Editor": "设置编辑器",
        "Value": "值",
        "Default": "默认",
        "Search settings...": "搜索设置...",
        "Hide modified": "隐藏已修改",
        "Hide default": "隐藏默认",
        "Highlight modified": "高亮显示已修改",
        "Highlight default": "高亮显示默认",
        "&Reset": "重置(&R)",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        # "Use": "使用", # 该条目不能更改，否则会导致空指针引用。
                        # https://github.com/org-220623/systeminformer-chinese-scripts/issues/4
        "Own processes": "当前用户进程",
        "GUI threads": "GUI 线程",
        "Relocated DLLs": "重定位 DLL",
        "Protected handles": "受保护句柄",
        "Protected processes": "受保护进程",
        "Inheritable handles": "可继承句柄",
        "Filtered processes": "已筛选进程",
        "Untrusted DLLs and Services": "不受信任的 DLL 和服务",
        "Disabled Services": "已禁用的服务",
        "Stopped Services": "已停止的服务",
        "Power efficiency": "电源节能",
        "System processes": "系统进程",
        "Service processes": "服务进程",
        "Background processes": "后台进程",
        "Job processes": "作业进程",
        "32-bit processes": "32 位进程",
        "Debugged processes": "被调试进程",
        "Elevated processes": "提升进程",
        "UIAccess processes": "UIAccess 进程",
        "Pico processes": "Pico 进程",
        "Immersive processes and DLLs": "UWP 进程和 DLL",
        "Suspended processes and threads": "已挂起的进程和线程",
        "Partially suspended processes and threads": "部分挂起的进程和线程",
        ".NET processes and DLLs": ".NET 进程和 DLL",
        "Packed processes": "打包的进程",
        "Low process image coherency": "低映像一致性进程",
        "Processes running under the same user account as System Informer.":
            "与 System Informer 使用同一用户帐户运行的进程。",
        r"Processes running under the NT AUTHORITY\\SYSTEM user account.":
            r"以 NT AUTHORITY\\SYSTEM 用户帐户运行的进程。",
        "Processes which host one or more services.": "承载一个或多个服务的进程。",
        "Processes with a background scheduling priority.": "具有后台调度优先级的进程。",
        "Processes associated with a job.": "与作业关联的进程。",
        "Processes running under WOW64, i.e. 32-bit.": "在 WOW64 (即 32 位) 下运行的进程。",
        "Processes that are currently being debugged.": "当前正在调试的进程。",
        "Processes with full privileges on a system with UAC enabled.":
            "在启用了 UAC 的系统上具有完全权限的进程。",
        "Processes with UIAccess privileges.": "具有 UIAccess 权限的进程。",
        "Processes that belong to the Windows subsystem for Linux.":
            "属于适用于 Linux 的 Windows 子系统 (WSL) 的进程。",
        "Processes and DLLs that belong to a Modern UI app.":
            "属于 Modern UI 应用的进程和 DLL。",
        "Processes and threads that are suspended from execution.":
            "已暂停执行的进程和线程。",
        "Processes and threads that are partially suspended from execution.":
            "部分暂停执行的进程和线程。",
        ".NET (i.e. managed) processes and DLLs.": ".NET (托管) 进程和 DLL。",
        "The image file backing the process has low coherency when compared to the mapped image.":
            "与映射映像相比，支持进程的映像文件一致性较低。",
        "Threads that have made at least one GUI-related system call.": "至少进行过一次与 GUI 相关的系统调用的线程。",
        "DLLs that were not loaded at their preferred image bases.": "未加载到其首选映像基础的 DLL。",
        "Handles that are protected from being closed.": "受保护无法关闭的句柄。",
        "Processes with built-in protection levels.": "具有内置保护级别的进程。",
        "Handles that can be inherited by child processes.": "可被子进程继承的句柄。",
        "Processes that are protected by handle object callbacks.": "受句柄对象回调保护的进程。",
        "Services and DLLs which are not digitally signed.": "未进行数字签名的服务和 DLL。",
        "Services which have been disabled.": "已禁用的服务。",
        "Services that are not running.": "未运行的服务。",
        "Processes and threads with power efficiency.": "设置节能模式的进程和线程。",
        "CPU kernel": "CPU 内核模式",
        "CPU user": "CPU 用户模式",
        "Private bytes": "私有字节",
        "Physical memory": "物理内存",
        "Power usage": "电源用量",
        "Temperature": "温度",
        "Fan RPM": "风扇转速 (转每分)",
        "Enable plugins": "启用插件",
    }, [
        ('PhAddTreeNewColumnEx(Context->TreeNewHandle, PH_OPTIONS_ADVANCED_COLUMN_ITEM_TYPE, TRUE, L"Type"',
         'PhAddTreeNewColumnEx(Context->TreeNewHandle, PH_OPTIONS_ADVANCED_COLUMN_ITEM_TYPE, TRUE, L"类型"'),
        (r'"Executables are sometimes \"packed\" to reduce their size."',
         r'"可执行文件有时会被 \"打包\" 以减小其大小。"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/pagfiles.c", "utf-8", {
        "File name": "文件名",
        "Usage": "用量",
        "Peak usage": "用量峰值",
        "Total": "总计",
        "Minimum": "最小值",
        "Maximum": "最大值",
        "Unable to query pagefile information.": "无法查询页面文件信息。",
        "&Copy": "复制(&C)",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/plugin.c", "utf-8", {
        "An unknown error occurred.": "出现未知错误。",
        "Unable to load the following plugin(s)": "无法加载以下插件",
        "%ls plugin registering": "已注册 %ls 个插件",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/plugman.c", "utf-8", {
        "Plugin": "插件",
        "Author": "作者",
        "Version": "版本",
        "Disabled Plugins (%lu)": "已禁用插件 (%lu)",
        "Uninstall": "卸载",
        "Disable": "禁用",
        "Properties": "属性",
        "Changes may require a restart to take effect...":
            "需要重启以应用更改...",
        "Unable to create the window.": "无法创建窗口。",
        "Plugins are not enabled.": "插件未启用。",
        "To use Plugins enable them in Options and restart System Informer.":
            "要使用插件，请在“选项”中启用它们并重启 System Informer。",
        "(unnamed)": "(未命名)",
        "Unknown": "未知",
        "Property": "属性",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/procmtgn.c", "utf-8", {
        " (permanent)": " (永久)",
        "Data Execution Prevention (DEP) is%s enabled for this process.\r\n":
            "此进程已%s启用数据执行保护 (DEP)。\r\n",
        " permanently": "永久",
        "ATL thunk emulation is disabled.\r\n": "ATL 形式转换模拟已禁用。\r\n",
        "high entropy, ": "高熵, ",
        "force relocate, ": "强制重定位, ",
        "disallow stripped, ": "禁止剥离, ",
        "Address Space Layout Randomization is enabled for this process.\r\n":
            "此进程已启用地址空间布局随机化。\r\n",
        "High entropy randomization is enabled.\r\n":
            "已启用高熵随机化。\r\n",
        "All images are being forcibly relocated (regardless of whether they support ASLR).\r\n":
            "所有映像都将被强制重新定位 (无论它们是否支持 ASLR)。\r\n",
        "Images with stripped relocation data are disallowed.\r\n":
            "不允许使用剥离重定位数据的映像。\r\n",
        "Dynamic code prohibited": "禁止使用动态代码",
        "Dynamically loaded code is not allowed to execute.\r\n":
            "不允许执行动态加载的代码。\r\n",
        "Dynamic code prohibited (per-thread)":
            "禁止动态代码 (按线程)",
        "Allows individual threads to opt out of the restrictions on dynamic code generation.\r\n":
            "允许各个线程选择退出动态代码生成的限制。\r\n",
        "Dynamic code downgradable": "动态代码可降级",
        "Allow non-AppContainer processes to modify all of the dynamic code settings for the calling process, including relaxing dynamic code restrictions after they have been set.\r\n":
            "允许非 AppContainer 进程修改调用进程的所有动态代码设置，包括放宽已设置的动态代码限制。\r\n",
        "Strict handle checks": "严格句柄检查",
        "An exception is raised when an invalid handle is used by the process.\r\n":
            "当进程使用无效句柄时，将引发异常。\r\n",
        "Win32k system calls disabled": "禁用 Win32k 系统调用",
        "Win32k (GDI/USER) system calls are not allowed.\r\n":
            "不允许使用 Win32k (GDI/USER) 系统调用。\r\n",
        "Win32k system calls (Audit)": "Win32k 系统调用 (审核)",
        "Win32k (GDI/USER) system calls will trigger an ETW event.\r\n":
            "Win32k (GDI/USER) 系统调用将触发 ETW 事件。\r\n",
        "Extension points disabled": "禁用扩展点",
        "Legacy extension point DLLs cannot be loaded into the process. NOTE: Processes with uiAccess=true will automatically bypass this policy and inject legacy extension point DLLs regardless.\r\n":
            "旧版扩展点 DLL 无法加载到此进程中。注意: uiAccess=true 的进程将自动绕过此策略并注入旧版扩展点 DLL。\r\n",
        "Strict ": "严格 ",
        "Audit ": "审核 ",
        "XF Guard": "XFG",
        "CF Guard": "CFG",
        "Extended Control Flow Guard (XFG) is enabled for the process.\r\n":
            "旧版扩展点 DLL 无法加载到此进程中。注意: 此进程已启用扩展控制流防护 (XFG)。\r\n",
        "Audit XFG : XFG is running in audit mode.\r\n":
            "审计 XFG: XFG 正在以审计模式运行。\r\n",
        "Strict XFG : only XFG modules can be loaded.\r\n":
            "严格 XFG: 仅可加载 XFG 模块。\r\n",
        "Dll Exports can be marked as XFG invalid targets.\r\n":
            "DLL 导出可能被标记为 XFG 无效目标。\r\n",
        "Control Flow Guard (CFG) is enabled for the process.\r\n":
            "此进程已启用控制流防护 (CFG)。\r\n",
        "Strict CFG : only CFG modules can be loaded.\r\n":
            "严格 CFG: 仅可加载 CFG 模块。\r\n",
        "Dll Exports can be marked as CFG invalid targets.\r\n":
            "DLL 导出可以标记为无效的 CFG 目标。\r\n",
        "Signatures restricted (": "限制签名 (",
        "Microsoft only, ": "仅 Microsoft, ",
        "Store only, ": "仅 MS Store, ",
        "Image signature restrictions are enabled for this process.\r\n":
            "此进程已启用映像签名限制。\r\n",
        "Only Microsoft signatures are allowed.\r\n":
            "仅允许 Microsoft 签名。\r\n",
        "Only Windows Store signatures are allowed.\r\n":
            "仅允许 Windows 应用商店签名。\r\n",
        "This is an opt-in restriction.\r\n":
            "这是一项可选的限制。\r\n",
        "Non-system fonts disabled": "禁用非系统字体",
        "Non-system fonts cannot be used in this process.\r\n": "此进程中无法使用非系统字体。\r\n",
        "Loading a non-system font in this process will trigger an ETW event.\r\n":
            "在此进程中加载非系统字体将触发 ETW 事件。\r\n",
        "Images restricted (": "映像受限 (",
        "remote images, ": "远程映像, ",
        "low mandatory label images, ": "低完整性标签映像, ",
        "Remotely located images cannot be loaded into the process.\r\n":
            "远程映像无法加载到进程中。\r\n",
        "Images with a Low mandatory label cannot be loaded into the process.\r\n":
            "带有“低强制”标签的映像无法加载到进程中。\r\n",
        "Forces images to load from the System32 folder in which Windows is installed first, then from the application directory before the standard DLL search order.\r\n":
            "强制映像首先从 Windows 安装所在的 System32 文件夹加载，然后从应用程序目录加载，最后才按照标准的 DLL 搜索顺序加载。\r\n",
        "Prefer system32 images": "优先选择 System32 映像",
        "System call filtering": "系统调用筛选",
        "System call filtering is active.\r\n": "系统调用筛选已启用。\r\n",
        "Payload restrictions": "载荷限制",
        "Payload restrictions are enabled for this process.\r\n":
            "此进程已启用有效负载限制。\r\n",
        "Export Address Filtering is enabled.\r\n": "已启用导出地址筛选。\r\n",
        "Export Address Filtering (Plus) is enabled.\r\n": "已启用导出地址筛选 (增强版)。\r\n",
        "Import Address Filtering is enabled.\r\n": "已启用导入地址筛选。\r\n",
        "StackPivot is enabled.\r\n": "已启用 StackPivot。\r\n",
        "CallerCheck is enabled.\r\n": "已启用 CallerCheck。\r\n",
        "SimExec is enabled.\r\n": "已启用 SimExec。\r\n",
        "Child process creation disabled": "禁用子进程创建",
        "Child processes cannot be created by this process.\r\n": "此进程无法创建子进程。\r\n",
        "SMT-thread branch target isolation": "SMT 线程分支目标隔离",
        "Branch target pollution cross-SMT-thread in user mode is enabled.\r\n":
            "已启用用户模式下的跨 SMT 线程分支目标污染。\r\n",
        "Distinct security domain": "不同的安全域",
        "Isolated security domain is enabled.\r\n": "已启用隔离安全域。\r\n",
        "Restricted page combining": "限制页面合并",
        "Disables all page combining for this process.\r\n": "禁用此进程的所有页面合并操作。\r\n",
        "Memory disambiguation (SSBD)": "内存消歧 (SSBD)",
        "Memory disambiguation is enabled for this process.\r\n": "此进程已启用内存消歧。\r\n",
        "Stack protection": "栈保护",
        "The CPU verifies function return addresses at runtime by employing a hardware-enforced shadow stack.\r\n":
            "CPU 通过使用硬件强制执行的影子堆栈，在运行时验证函数返回地址。\r\n",
        "Audit Stack protection : log ROP failures to event log.\r\n":
            "审计堆栈保护: 将 ROP 失败记录到事件日志中。\r\n",
        "Strict Stack protection : any detected ROP will cause the process to terminate.\r\n":
            "严格的堆栈保护: 任何检测到的 ROP 操作都会导致进程终止。\r\n",
        "Audit Set Context IP validation : log modifications of context IP to event log.\r\n":
            "审核集上下文 IP 验证: 将上下文 IP 的修改记录到事件日志中。\r\n",
        "Set Context IP validation : any detected modification of context IP will cause the process to terminate.\r\n":
            "设置上下文 IP 验证: 任何检测到的上下文 IP 修改都将导致进程终止。\r\n",
        "Audit Block non CET binaries : log attempts to load binaries without CET support.\r\n":
            "审核阻止非 CET 二进制文件: 记录尝试加载不支持 CET 的二进制文件的尝试。\r\n",
        "Block binaries without CET support\r\n": "阻止不支持 CET 的二进制文件。\r\n",
        "Block binaries without CET support or without EH continuation metadata.\r\n":
            "阻止不支持 CET 或缺少 异常处理延续元数据的二进制文件。\r\n",
        "Junction redirection protection / Audit": "连接重定向保护/审核",
        "Prevents the process from following filesystem junctions created by non-admin users and logs the attempt.\r\nLogs attempts by the process to follow filesystem junctions created by non-admin users.\r\n":
            "阻止进程跟随非管理员用户创建的文件系统连接点，并记录此尝试。\r\n记录进程跟随非管理员用户创建的文件系统连接点的尝试。\r\n",
        "Junction redirection protection": "连接重定向保护",
        "Prevents the process from following filesystem junctions created by non-admin users and logs the attempt.\r\n":
            "阻止进程跟踪非管理员用户创建的文件系统连接点，并记录此尝试。\r\n",
        "Junction redirection protection (Audit)": "连接重定向保护 (审核)",
        "Logs attempts by the process to follow filesystem junctions created by non-admin users.\r\n":
            "记录进程尝试跟随非管理员用户创建的文件系统连接点的操作。\r\n",
        "ARM pointer authentication": "ARM 指针身份验证",
        "Pointer authentication (PAC) prevents unexpected changes to pointers.\r\n":
            "指针认证 (PAC) 可防止指针发生意外更改。\r\n",
        "Structured exception handling overwrite protection (SEHOP)": "结构化异常处理覆盖保护 (SEHOP)",
        "SEHOP prevents Structured Exception Handler (SEH) overwrites.\r\n":
            "SEHOP 可防止结构化异常处理程序 (SEH) 被覆盖。\r\n",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/procprp.c", "utf-8", {
        "Loading...": "加载中...",
        "Close": "关闭",
        ") exited with ": ") 已退出，退出信息: ",
        ") exited with 0x": ") 已退出，退出代码: 0x",
        "Threads": "线程",
        "T&erminate\bDel": "结束进程(&E)\bDel",
        "Terminate tree\bShift+Del": "结束进程树\bShift+Del",
        "&Suspend": "挂起进程(&S)",
        "Suspend tree": "挂起进程树",
        "Res&ume": "恢复进程(&U)",
        "Resume tree": "恢复进程树",
        "Freeze": "冻结",
        "Thaw": "解冻",
        "Res&tart": "重新启动(&T)",
        "Create live kernel dump fi&le": "创建活动内核转储文件(&L)",
        "&Minimal...": "小型(&M)...",
        "&Normal...": "正常(&N)...",
        "&Full...": "完全(&F)...",
        "&Custom...": "自定义(&C)...",
        "Create dump fi&le": "创建转储文件(&L)",
        "&Limited...": "受限(&L)...",
        "De&bug": "调试(&B)",
        "&Affinity": "处理器相关性(&A)",
        "&Priority": "优先级(&P)",
        "&Real time": "实时(&R)",
        "&High": "高(&H)",
        "&Above normal": "高于正常(&A)",
        "&Normal": "正常(&N)",
        "&Below normal": "低于正常(&B)",
        "&Idle": "空闲(&I)",
        "&I/O priority": "I/O 优先级(&I)",
        "&Low": "低(&L)",
        "&Very low": "非常低(&V)",
        "Pa&ge priority": "页面优先级(&G)",
        "&Medium": "中(&M)",
        "&Miscellaneous": "其他(&M)",
        "Activity moderation": "活动审核",
        "&Critical": "关键(&C)",
        "&Detach from debugger": "断开与调试器的连接(&D)",
        "Efficiency mode": "节能模式",
        "Execution required": "执行所需状态",
        "GDI &handles...": "GDI 对象句柄(&H)...",
        "Heaps...": "堆...",
        "Locks...": "锁...",
        "Flush heaps": "刷新堆",
        "Modified pages...": "已修改页面...",
        "Reduce working &set": "减小工作集(&S)",
        "&Run as...": "以特定用户身份运行(&R)...",
        "Run &as this user...": "以当前用户身份运行(&A)...",
        "Virtuali&zation": "虚拟化(&Z)",
        "Search &online\bCtrl+M": "在线搜索(&O)\bCtrl+M",
        "Open &file location\bCtrl+Enter": "打开文件所在位置(&F)\bCtrl+Enter",
        "Security": "安全",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "Unable to locate the file.": "无法定位文件。",
        # todo line 721
        #     PhEditSecurity(
        #                                 PhCsForceNoParent ? NULL : pageWindow,
        #                                 PhGetStringOrEmpty(propContext->ProcessItem->ProcessName),
        #                                 L"Process",                                                   <- HERE
        #                                 PhOptionsButtonGeneralOpenProcess,
        #                                 PhOptionsButtonGeneralCloseHandle,
        #                                 propContext->ProcessItem->ProcessId
        #                                 );
        "Protection": "保护",
        "Options": "选项",
        "Permissions": "权限",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/procprv.c", "utf-8", {
        "DPCs": "DPC",
        # "Interrupts": "中断",
        # 中断是进程名称，不能翻译。
        "Adding process item: %ls (%lu)": "正在添加进程项: %ls (%lu)",
        "Removing process item: %ls (%lu)": "正在移除进程项: %ls (%lu)",
        "Process query stage 1: %ls (%lu)": "进程查询阶段 1: %ls (%lu)",
        "Interrupts and DPCs": "中断和 DPC",
        "Process query stage 2: %ls (%lu)": "进程查询阶段 2: %ls (%lu)",
        "Unknown time": "未知时间",
        "Process provider run count: %lu": "进程提供程序运行计数: %lu",
        "Failed to enumerate processes: %lu %!STATUS!":
            "枚举进程失败: %lu %!STATUS!",
        "Unknown": "未知",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/procrec.c", "utf-8", {
        "%s ago (%s)": "%s 以前 (%s)",
        "Non-existent process (%u)": "不存在的进程 (%u)",
        "Unknown process (%u)": "未知进程 (%u)",
        "Make sure the Explorer executable file is present.":
            "请确保资源管理器可执行文件存在。",
        "Unable to show the process properties.": "无法显示进程属性。",
        "The process has already terminated; only the process record is available.":
            "进程已终止；仅进程记录可用。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/proctree.c", "utf-8", {
        "Name": "名称",
        "I/O total rate": "I/O 总速率",
        "Private bytes": "私有字节",
        "User name": "用户名",
        "Description": "描述",
        "Company name": "发行商名称",
        "Version": "版本",
        "File name": "文件名",
        "Command line": "命令行",
        "Peak private bytes": "私有字节峰值",
        "Working set": "工作集",
        "Peak working set": "工作集峰值",
        "Private WS": "私有工作集",
        "Shared WS": "已共享工作集",
        "Shareable WS": "可共享工作集",
        "Virtual size": "虚拟大小",
        "Peak virtual size": "虚拟大小峰值",
        "Page faults": "页面错误",
        "Session ID": "会话 ID",
        "Priority class": "优先级类",
        "Base priority": "基本优先级",
        "Threads": "线程",
        "Handles": "句柄",
        "GDI handles": "GDI 对象句柄",
        "USER handles": "用户对象句柄",
        "I/O read+other rate": "I/O 读取+其他速率",
        "I/O write rate": "I/O 写入速率",
        "Integrity": "完整性",
        "I/O priority": "I/O 优先级",
        "Page priority": "页面优先级",
        "Start time": "启动时间",
        "Total CPU time": "CPU 时间总计",
        "Kernel CPU time": "CPU 内核时间",
        "User CPU time": "CPU 用户时间",
        "Verification status": "验证状态",
        "Verified signer": "已验证的签名方",
        "Relative start time": "相对启动时间",
        "Bits": "比特",
        "Elevation": "提升",
        "Window title": "窗口标题",
        "Window status": "窗口状态",
        "Cycles": "周期",
        "Cycles delta": "周期增量",
        "CPU history": "CPU 历史",
        "Private bytes history": "私有字节历史",
        "I/O history": "I/O 历史",
        "Virtualized": "虚拟化",
        "Context switches": "上下文切换",
        "Context switches delta": "上下文切换增量",
        "Page faults delta": "页面错误增量",
        "I/O reads": "I/O 读取",
        "I/O writes": "I/O 写入",
        "I/O other": "I/O 其他",
        "I/O read bytes": "I/O 读取字节",
        "I/O write bytes": "I/O 写入字节",
        "I/O other bytes": "I/O 其他字节",
        "I/O reads delta": "I/O 读取增量",
        "I/O writes delta": "I/O 写入增量",
        "I/O other delta": "I/O 其他增量",
        "OS context": "操作系统上下文",
        "Paged pool": "分页池",
        "Peak paged pool": "分页池峰值",
        "Non-paged pool": "非分页池",
        "Peak non-paged pool": "非分页池峰值",
        "Minimum working set": "最小工作集",
        "Maximum working set": "最大工作集",
        "Private bytes delta": "私有字节增量",
        "Subsystem": "子系统",
        "Package name": "包名称",
        "App ID": "应用 ID",
        "DPI awareness": "DPI 感知",
        "CF Guard": "控制流防护",
        "Time stamp": "时间戳",
        "File modified time": "文件修改时间",
        "File size": "文件大小",
        "Subprocesses": "子进程",
        "Job Object ID": "作业对象 ID",
        "Protection": "保护",
        "Critical": "关键进程",
        "PID (Hex)": "PID (十六进制)",
        "CPU (relative)": "CPU (相对)",
        "Image coherency": "映像一致性",
        "Error mode": "错误模式",
        "Code page": "代码页",
        "Timeline": "时间线",
        "Power throttling": "电源限制",
        "Architecture": "架构",
        "Parent PID": "父 PID",
        "Parent console PID": "父控制台 PID",
        "Shared commit": "已共享提交",
        "Priority boost": "优先级提升",
        "CPU (average)": "CPU (均值)",
        "CPU (kernel)": "CPU (内核)",
        "CPU (user)": "CPU (用户)",
        "Granted access (symbolic)": "已授予访问权限 (符号)",
        "Thread local storage": "线程本地存储",
        "References": "引用",
        "Start key": "起始键",
        "Mitigation policies": "缓解策略",
        "Services": "服务",
        "Fail critical, ": "失败 (关键), ",
        "GP faults, ": "一般保护错误, ",
        "Alignment faults, ": "对齐错误, ",
        "Openfile faults, ": "打开文件错误, ",
        # todo 1672
        "Image digital signature support disabled.": "映像数字签名支持已禁用。",
        " ago": " 以前",
        "Not responding": "未响应",
        "Running": "正在运行",
        "DEP (permanent), ": "DEP (强制), ",
        "ATL emulation, ": "ATL 模拟, ",
        "Execute enabled, ": "已对执行启用, ",
        "Image enabled, ": "已对映像启用, ",
        "Chain disabled, ": "已禁用异常链, ",
        # todo 4134 Subsystem
        "Unknown": "未知",
        "Unaware": "未感知",
        "System aware": "系统感知",
        "Per-monitor aware": "每显示器感知",
        "Per-monitor V2": "每显示器感知 V2",
        "Unaware (GDI scaled)": "未感知 (GDI 缩放)",
        "XF Guard": "扩展控制流防护",
        "XF Guard (audit)": "扩展控制流防护 (审核)",
        "Image coherency support is disabled.":
            "映像一致性支持已禁用。",
        "Scanning....": "正在扫描...",
        "Yes": "是",
        "Unable to perform the operation.": "无法执行操作。",
        "This node cannot be displayed because it is currently hidden by your active filter settings or preferences.":
            "此节点无法显示，因为它当前已被您活动的筛选器设置或首选项隐藏。",
    }, [
        ('PhAddTreeNewColumnEx(hwnd, PHPRTLC_DESKTOP, FALSE, L"Desktop"',
         'PhAddTreeNewColumnEx(hwnd, PHPRTLC_DESKTOP, FALSE, L"桌面"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpgenv.c", "utf-8", {
        "There are no environment variables to display.": "没有要显示的环境变量。",
        "Unable to query environment information:\n": "无法查询环境信息:\n",
        "Unknown error.": "未知错误。",
        "edit": "编辑",
        "the selected environment variable": "已选中的环境变量",
        "Some programs may restrict access or ban your account when editing the environment variable(s) of the process.": "某些程序在编辑进程的环境变量时可能会限制访问或封禁您的帐户。",
        "Unable to set the environment variable.": "无法设置环境变量。",
        "Unable to delete the environment variable.": "无法删除环境变量。",
        "Edit": "编辑",
        "Delete": "删除",
        "&Copy": "复制(&C)",
        "Name": "名称",
        "Value": "值",
        "Search Environment (Ctrl+K)": "搜索环境信息 (Ctrl+K)",
        "Hide process": "隐藏进程",
        "Hide user": "隐藏用户",
        "Hide system": "隐藏系统",
        "Hide cmd": "隐藏 CMD",
        "Highlight process": "高亮显示进程",
        "Highlight user": "高亮显示用户",
        "Highlight system": "高亮显示系统",
        "Highlight cmd": "高亮显示 CMD",
        "New variable...": "新建环境变量...",
        "delete": "删除",
    }, [
        ('PhpAddEnvironmentNode(Context, NULL, PROCESS_ENVIRONMENT_TREENODE_TYPE_GROUP | PROCESS_ENVIRONMENT_TREENODE_TYPE_PROCESS, PhaCreateString(L"Process")',
         'PhpAddEnvironmentNode(Context, NULL, PROCESS_ENVIRONMENT_TREENODE_TYPE_GROUP | PROCESS_ENVIRONMENT_TREENODE_TYPE_PROCESS, PhaCreateString(L"进程")'),
        ('PhpAddEnvironmentNode(Context, NULL, PROCESS_ENVIRONMENT_TREENODE_TYPE_GROUP | PROCESS_ENVIRONMENT_TREENODE_TYPE_USER, PhaCreateString(L"User")',
         'PhpAddEnvironmentNode(Context, NULL, PROCESS_ENVIRONMENT_TREENODE_TYPE_GROUP | PROCESS_ENVIRONMENT_TREENODE_TYPE_USER, PhaCreateString(L"用户")'),
        ('PhpAddEnvironmentNode(Context, NULL, PROCESS_ENVIRONMENT_TREENODE_TYPE_GROUP | PROCESS_ENVIRONMENT_TREENODE_TYPE_SYSTEM, PhaCreateString(L"System")',
         'PhpAddEnvironmentNode(Context, NULL, PROCESS_ENVIRONMENT_TREENODE_TYPE_GROUP | PROCESS_ENVIRONMENT_TREENODE_TYPE_SYSTEM, PhaCreateString(L"系统")'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpggen.c", "utf-8", {
        "None": "无",
        "Light": "轻型",  # PPL
        "Full": "完整",   # PP
        # todo PhProtectedSignerStrings line 37
        "Unknown": "未知",
        "Secure (IUM)": "安全进程 (IUM)",
        "Yes": "是",
        "(32-bit)": "(32 位)",
        "(64-bit)": "(64 位)",
        "<a>(Verified) %s</a>": "<a>(已验证) %s</a>",
        "(Verified) ": "(已验证) ",
        "(UNVERIFIED) ": "(未验证) ",
        "%s ago (%s)": "%s 以前 (%s)",
        "Non-existent process (%lu)": "不存在的进程 (%lu)",
        "Make sure the PE Viewer executable file is present.": "请确保 PE Viewer 可执行文件存在。",
        "Unable to locate the file.": "无法定位文件。",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "[FULL] %s\r\n": "[完整] %s\r\n",
        "The process does not exist.": "进程不存在。",
        # todo Line 747
        #                   PhEditSecurity(
        #                         PhCsForceNoParent ? NULL : hwndDlg,
        #                         PhGetStringOrEmpty(processItem->ProcessName),
        #                         L"Process",
        #                         PhpProcessGeneralOpenProcess,
        #                         PhpProcessGeneralCloseHandle,
        #                         processItem->ProcessId
        #                         );
        # todo No-Write-Up 767
        # todo No-Read-Up
        # todo No-Execute-Up
        "update": "更新",
        "the integrity label": "完整性标签",
        "Altering the integrity label for a process may produce undesirable results, instability or data corruption.": "更改进程的完整性标签可能会产生不良后果、不稳定或数据损坏。",
        "Unable to set the integrity label": "无法设置完整性标签",
        "Unable to perform the operation.": "无法执行操作。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpghndl.c", "utf-8", {
        "There are no handles to display.": "没有要显示的句柄。",
        "C&lose\bDel": "关闭(&L)\bDel",
        "&Protected": "保护(&P)",
        "&Inherit": "继承(&I)",
        "Secu&rity": "安全(&R)",
        "Prope&rties\bEnter": "属性(&T)\bEnter",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        # todo 288, 292 'Protected' 'Inherit'
        "Search Handles (Ctrl+K)": "搜索句柄 (Ctrl+K)",
        "The process does not exist.": "进程不存在。",
        "Unable to query the process.": "无法查询进程。",
        "Hide protected handles": "隐藏受保护句柄",
        "Hide inherit handles": "隐藏继承句柄",
        "Hide unnamed handles": "隐藏未命名句柄",
        "Hide etw handles": "隐藏 ETW 句柄",
        "Highlight protected handles": "高亮显示受保护句柄",
        "Highlight inherit handles": "高亮显示继承句柄",
        "Statistics": "统计数据",
        "Unable to query handle information:\n%s": "无法查询句柄信息:\n%s",
        "Unknown error.": "未知错误。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpgmem.c", "utf-8", {
        "There are no memory regions to display.": "没有要显示的内存区域。",
        "&Read/Write memory...": "读取/写入内存(&R)...",
        "Change &protection...": "更改保护选项(&P)...",
        "&Empty working set...": "清空工作集(&E)...",
        "&Free": "释放(&F)",
        "&Decommit": "撤销提交(&D)",
        "&Save...": "保存(&S)...",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        "Text files (*.txt;*.log)": "文本文件 (*.txt;*.log)",
        "Comma-separated values (*.csv)": "CSV 文件 (*.csv)",
        "All files (*.*)": "所有文件 (*.*)",
        "Unknown process": "未知进程",
        ") Memory": ") 内存",
        "Unable to create the file": "无法创建文件",
        "Search Memory (Ctrl+K)": "搜索内存 (Ctrl+K)",
        "Unable to open the process": "无法打开进程",
        "Binary files (*.bin)": "二进制文件 (*.bin)",
        "Hide free pages": "隐藏空闲页面",
        "Hide reserved pages": "隐藏保留页面",
        "Hide guard pages": "隐藏防护页面",
        "Highlight private pages": "高亮显示私有页面",
        "Highlight system pages": "高亮显示系统页面",
        "Highlight CFG pages": "高亮显示 CFG 页面",
        "Highlight executable pages": "高亮显示可执行页面",
        "Zero pad addresses": "地址补零",
        "Read/Write &address...": "读取/写入地址(&A)...",
        "Heaps...": "堆...",
        "Modified...": "已修改...",
        "Strings...": "字符串...",
        "Save...": "保存...",
        "Read/Write Address": "读取/写入地址",
        "Enter an address:": "输入地址:",
        "Unable to find the memory region for the selected address.": "无法找到所选地址的内存区域。",
        "Unable to query memory information:\n%s": "无法查询内存信息:\n%s",
        "Unknown error.": "未知错误。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpgmod.c", "UTF-8", {
        "There are no modules to display.": "没有要显示的模块。",
        "&Unload\bDel": "卸载(&U)\bDel",
        "Open &file location\bCtrl+Enter": "打开文件所在位置(&F)\bCtrl+Enter",
        "P&roperties": "属性(&R)",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        "Static dependency": "静态依赖项",
        "Static forwarder dependency": "静态转发器依赖项",
        "Dynamic forwarder dependency": "动态转发器依赖项",
        "Delay load dependency": "延迟加载依赖项",
        "Dynamic": "动态",
        "Image": "映像",
        "Data": "数据",
        "No Signature": "未签名",
        "Expired": "已过期",
        "Revoked": "已撤销",
        "Trusted": "受信任",
        "Bad": "损坏",
        "Text files (*.txt;*.log)": "文本文件 (*.txt;*.log)",
        "Comma-separated values (*.csv)": "CSV 文件 (*.csv)",
        "All files (*.*)": "所有文件 (*.*)",
        "Unknown process": "未知进程",
        ") Modules": ") 模块",
        "Unable to create the file": "无法创建文件",
        "Search Modules (Ctrl+K)": "搜索模块 (Ctrl+K)",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "Make sure the PE Viewer executable file is present.": "请确保 PE Viewer 可执行文件存在。",
        "Hide dynamic": "隐藏动态模块",
        "Hide mapped": "隐藏映射模块",
        "Hide static": "隐藏静态模块",
        "Hide verified": "隐藏已验证模块",
        "Hide system": "隐藏系统模块",
        "Hide low image coherency": "隐藏低映像一致性模块",
        "Hide knowndlls images": r"隐藏 \\KnownDlls 模块",
        "Highlight .NET modules": "高亮显示 .NET 模块",
        "Highlight immersive modules": "高亮显示 Immersive 模块",
        "Highlight relocated modules": "高亮显示重定位模块",
        "Highlight untrusted modules": "高亮显示不受信任的模块",
        "Highlight system modules": "高亮显示系统模块",
        "Highlight low image coherency": "高亮显示低映像一致性模块",
        "Highlight knowndlls images": r"高亮显示 \\KnownDlls 模块",
        "Zero pad addresses": "地址补零",
        "Load module...": "加载模块...",
        "Strings...": "字符串...",
        "Save...": "保存...",
        "load": "加载",
        "a module": "模块",
        "Some programs may restrict access or ban your account when loading modules into the process.": "某些程序在将模块加载到进程中时可能会限制访问或封禁您的帐户。",
        "Unable to query module information:\n%s": "无法查询模块信息:\n%s",
        "Unknown error.": "未知错误。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpgstat.c", "utf-8", {
        "Memory": "内存",
        "Other": "其他",
        "CPU (user)": "CPU (用户)",
        "CPU (kernel)": "CPU (内核)",
        "CPU (average)": "CPU (均值)",
        "CPU (relative)": "CPU (相对)",
        "Cycles": "周期",
        "Cycles delta": "周期增量",
        "Context switches": "上下文切换",
        "Context switches delta": "上下文切换增量",
        "Kernel time": "内核时间",
        "Kernel delta": "内核时间增量",
        "User time": "用户时间",
        "User delta": "用户时间增量",
        "Total time": "时间总计",
        "Total delta": "时间总计增量",
        "Priority": "优先级",
        "Private bytes": "私有字节",
        "Private bytes delta": "私有字节增量",
        "Peak private bytes": "私有字节峰值",
        "Virtual size": "虚拟大小",
        "Peak virtual size": "虚拟大小峰值",
        "Page faults": "页面错误",
        "Page faults delta": "页面错误增量",
        "Hard faults": "硬错误",
        "Hard faults delta": "硬错误增量",
        "Working set": "工作集",
        "Peak working set": "工作集峰值",
        "Private WS": "私有工作集",
        "Shareable WS": "可共享工作集",
        "Shared WS": "已共享工作集",
        "Paged pool bytes": "分页池字节",
        "Peak paged pool bytes": "分页池字节峰值",
        "Nonpaged pool bytes": "非分页池字节",
        "Peak nonpaged pool bytes": "非分页池字节峰值",
        "Shared commit": "已共享提交",
        "Private commit": "私有提交",
        "Peak private commit": "私有提交峰值",
        "Private commit limit": "私有提交限制",
        "Total commit limit": "提交限制总计",
        "Page priority": "页面优先级",
        "Reads": "读取",
        "Reads delta": "读取增量",
        "Read bytes": "读取字节",
        "Read bytes delta": "读取字节增量",
        "Writes": "写入",
        "Writes delta": "写入增量",
        "Write bytes": "写入字节",
        "Write bytes delta": "写入字节增量",
        "Other delta": "其他增量",
        "Other bytes": "其他字节",
        "Other bytes delta": "其他字节增量",
        "Total bytes": "总计字节",
        "Total bytes delta": "总计字节增量",
        "Total bytes (average)": "总计字节 (均值)",
        "I/O priority": "I/O 优先级",
        "Handles": "句柄",
        "Peak handles": "句柄峰值",
        "GDI handles": "GDI 对象句柄",
        "Peak GDI handles": "GDI 对象句柄峰值",
        "USER handles": "用户对象句柄",
        "Peak USER handles": "用户对象句柄峰值",
        "Running time": "运行时间",
        "Suspended time": "挂起时间",
        "Hang count": "挂起计数",
        "Ghost count": "幽灵计数",
        "Property": "属性",
        "Value": "值",
        "Min": "最小",
        "Max": "最大",
        "Difference": "差值",
        "&Copy": "复制(&C)",
    }, [
        ('PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKREAD, L"BytesRead"',
         'PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKREAD, L"读取字节"'),
        ('PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKWRITE, L"BytesWritten"',
         'PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKWRITE, L"写入字节"'),
        ('PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_NETWORKTXRXBYTES, L"NetworkTxRxBytes"',
         'PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_NETWORKTXRXBYTES, L"网络发送/接收字节"'),
        ('PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_MBBTXRXBYTES, L"MBBTxRxBytes"', # Mobile Broadband Transmit/Receive Bytes
         # More info: https://chat.deepseek.com/share/7acotmbol2tqvd3zgc
         'PhAddIListViewGroupItem(Context->ListView, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_MBBTXRXBYTES, L"移动宽带发送/接收字节"'),
        ('PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKREAD, L"BytesRead", NULL)',
         'PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKREAD, L"读取字节", NULL)'),
        ('PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKWRITE, L"BytesWritten", NULL)',
         'PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_DISKWRITE, L"写入字节", NULL)'),
        ('PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_NETWORKTXRXBYTES, L"NetworkTxRxBytes"',
         'PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_NETWORKTXRXBYTES, L"网络发送/接收字节"'),
        ('PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_MBBTXRXBYTES, L"MBBTxRxBytes"',
         'PhListView_AddGroupItem(Context->ListViewContext, PH_PROCESS_STATISTICS_CATEGORY_OTHER, PH_PROCESS_STATISTICS_INDEX_MBBTXRXBYTES, L"移动宽带发送/接收字节"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpgthrd.c", "utf-8", {
        "There are no threads to display.": "没有要显示的线程。",
        "&Priority": "优先级(&P)",
        "&Inspect\bEnter": "检查(&I)\bEnter",
        "T&erminate\bDel": "终止(&E)\bDel",
        "&Suspend": "挂起(&S)",
        "Res&ume": "恢复(&U)",
        "Analy&ze": "分析(&Z)",
        "&Affinity": "处理器相关性(&A)",
        "&Boost": "提升(&B)",
        "Critical": "关键",
        "Per&missions": "权限(&M)",
        "&Token": "令牌(&T)",
        "Time &critical": "时间关键(&C)",
        "&Highest": "最高(&H)",
        "&Above normal": "高于正常(&A)",
        "&Normal": "正常(&N)",
        "&Below normal": "低于正常(&B)",
        "&Lowest": "最低(&L)",
        "&Idle": "空闲(&I)",
        "&I/O priority": "I/O 优先级(&I)",
        "&High": "高(&H)",
        "&Low": "低(&L)",
        "&Very low": "非常低(&V)",
        "Pa&ge priority": "页面优先级(&G)",
        "&Medium": "中(&M)",
        "&Copy\bCtrl+C": "复制(&C)\bCtrl+C",
        "Text files (*.txt;*.log)": "文本文件 (*.txt;*.log)",
        "Comma-separated values (*.csv)": "CSV 文件 (*.csv)",
        "All files (*.*)": "所有文件 (*.*)",
        "Unknown process": "未知进程",
        ") Threads": ") 线程",
        "Unable to create the file": "无法创建文件",
        "Search Threads (Ctrl+K)": "搜索线程 (Ctrl+K)",
        "Unable to %s thread %lu": "无法%s线程 %lu",
        "set the boost priority of": "设置以下对象的提升优先级: ",
        "enable": "启用",
        "critical status on the thread": "线程关健状态",
        "If the process ends, the operating system will shut down immediately.": "如果此类进程结束，操作系统将立即关闭。",
        "disable": "禁用",
        "Unable to change the thread critical status.": "无法更改线程关健状态。",
        "Thread %u": "线程 %u",
        # todo: line 1343 'Thread'
        "Unable to open the thread": "无法打开线程",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "Hide suspended": "隐藏已挂起线程",
        "Hide gui": "隐藏 GUI 线程",
        "Highlight suspended": "高亮显示已挂起线程",
        "Highlight gui": "高亮显示 GUI 线程",
        "Save...": "保存...",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpgvdm.c", "utf-8", {
        "Module name": "模块名",
        "File name": "文件名",
        "Thread Id": "线程 ID",
        "Task Id": "任务 ID",
        "Terminate": "终止",
        "Open &file location": "打开文件所在位置(&F)",
        "&Inspect": "检查(&I)",
        "&Copy": "复制(&C)",
        "Unable to terminate the task.": "无法结束任务。",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "Make sure the PE Viewer executable file is present.": "请确保 PE Viewer 可执行文件存在。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/prpgwmi.c", "utf-8", {
        # todo line 199
        #     querySelectString = PhFormatString(
        #             L"%s %s %s %s %s %s = %s",
        #             L"SELECT",
        #             L"Namespace,Provider,User,__RELPATH",
        #             L"FROM",
        #             L"Msft_Providers",
        #             L"WHERE",
        #             L"HostProcessIdentifier",
        #             ProcessIdString
        #             );
        #   and more...
        "Statistics for %s: \r\n\r\n": "%s 的统计数据: \r\n\r\n",
        "Default Namespace": "默认名称空间",
        "Unable to query provider information:\n": "无法查询提供程序信息:\n",
        "Unknown error.": "未知错误。",
        "Unable to perform the operation.": "无法执行操作。",
        "&Suspend": "挂起(&S)",
        "Res&ume": "恢复(&U)",
        "Un&load": "卸载(&L)",
        "&Inspect": "检查(&I)",
        "S&tatistics": "统计数据(&T)",
        "Open &file location": "打开文件所在位置(&F)",
        "&Copy": "复制(&C)",
        # todo 1076 Suspend
        #      1088 Resume
        #      1100 Unload
        "Make sure the PE Viewer executable file is present.": "请确保 PE Viewer 可执行文件存在。",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "File name": "文件名",
        "Search WMI Providers (Ctrl+K)": "搜索 WMI 提供程序 (Ctrl+K)",
        "There are no providers to display.": "没有要显示的提供程序。",
        "Hide default namespace": "隐藏默认名称空间",
        "Highlight default namespace": "高亮显示默认名称空间",
    }, [
        ('PhAddTreeNewColumn(Context->TreeNewHandle, PROCESS_WMI_COLUMN_ITEM_PROVIDER, TRUE, L"Provider"',
         'PhAddTreeNewColumn(Context->TreeNewHandle, PROCESS_WMI_COLUMN_ITEM_PROVIDER, TRUE, L"提供程序"'),
        ('PhAddTreeNewColumn(Context->TreeNewHandle, PROCESS_WMI_COLUMN_ITEM_NAMESPACE, TRUE, L"Namespace"',
         'PhAddTreeNewColumn(Context->TreeNewHandle, PROCESS_WMI_COLUMN_ITEM_NAMESPACE, TRUE, L"名称空间"'),
        ('PhAddTreeNewColumn(Context->TreeNewHandle, PROCESS_WMI_COLUMN_ITEM_USER, TRUE, L"User"',
         'PhAddTreeNewColumn(Context->TreeNewHandle, PROCESS_WMI_COLUMN_ITEM_USER, TRUE, L"用户"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/runas.c", "utf-8", {
        "Batch": "批处理",
        "Interactive": "交互式",
        "Network": "网络",
        "New credentials": "新凭据",
        "Service": "服务",
        "Unable to start the program.": "无法启动程序。",
        "Unable to start the execution alias with a process token.": "无法使用进程令牌启动执行别名。",
        "Programs (*.exe;*.pif;*.com;*.bat)": "应用程序 (*.exe;*.pif;*.com;*.bat)",
        "All files (*.*)": "所有文件 (*.*)",
        "WARNING: This will grant Everyone access to the current window station and desktop.": "警告: 这将授予 Everyone (任何用户) 对当前窗口工作站和桌面的访问权限。",
        "Are you sure you want to continue?": "您确定要继续吗?",
        "Unable to execute the command.": "无法执行命令。",
        "Executable files (*.exe;*.pif;*.com;*.bat;*.cmd)": "可执行文件 (*.exe;*.pif;*.com;*.bat;*.cmd)",
        "Loading package information...": "正在加载软件包信息...",
        "Package": "包",
        "Version": "版本",
        "Search Packages": "搜索软件包",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/sessmsg.c", "utf-8", {
        "None": "无",
        "Information": "信息",
        "Warning": "警告",
        "Error": "错误",
        "Question": "问题",
        "Message from %s": "来自 %s 的消息",
        "Unable to send the message": "无法发送消息",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/sessprp.c", "utf-8", {
        "Active": "活动",
        "Connected": "已连接",
        "ConnectQuery": "连接查询",
        "Shadow": "跟踪",
        "Disconnected": "已断开连接",
        "Idle": "空闲",
        "Listen": "监听",
        "Reset": "重置",
        "Down": "不活动",
        "Init": "初始化",
        "Name": "名称",
        "Value": "值",
        "User": "用户",
        "User name": "用户名",
        "Session ID": "会话 ID",
        "State": "状态",
        "Logon time": "登录时间",
        "Connect time": "连接时间",
        "Disconnect time": "断开连接时间",
        "Last input time": "最后输入时间",
        "Client name": "客户端时间",
        "Client address": "客户端地址",
        "Client display": "客户端显示",
        "LastLogon": "最后登录时间",
        "LastLogoff": "最后登出时间",
        "Home directory": "主目录",
        "Profile directory": "配置文件目录",
        "&Copy": "复制(&C)",
    }, [
        ('PhAddListViewGroup(context->ListViewHandle, 1, L"Profile"',
         'PhAddListViewGroup(context->ListViewHandle, 1, L"配置文件"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/sessshad.c", "utf-8", {
        "Unable to shadow session.": "无法进行会话跟踪。",
        "You cannot remote control the current session.": "您无法远程控制当前会话。",
        "Unable to remote control the session": "无法远程控制会话",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/settings.c", "utf-8", {
        # todo line 207
        #      PhpAddStringSetting(SETTING_PROC_PROP_PAGE, L"General");
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/srvcr.c", "utf-8", {
        "Own Process": "当前用户进程",
        "Demand Start": "请求启动",
        "Ignore": "忽略",
        "Unable to create the service.": "无法创建服务。",
        "The binary path is empty.": "可执行文件路径为空。",
        "Executable files (*.exe;*.sys)": "可执行文件 (*.exe;*.sys)",
        "All files (*.*)": "所有文件 (*.*)",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/srvctl.c", "utf-8", {
        "S&top": "停止(&T)",
        "&Pause": "暂停(&P)",
        "C&ontinue": "继续(&O)",
        "&Start": "启动(&S)",
        "Name": "名称",
        "Display name": "显示名称",
        "File name": "文件名",
        "Go to service": "转到服务",
        "&Copy": "复制(&C)",
        "The process does not exist.": "进程不存在。",
        "The service does not exist.": "服务不存在。",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "Unable to locate the file.": "无法定位文件。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/srvlist.c", "utf-8", {
        "Name": "名称",
        "Display name": "显示名称",
        "Status": "状态",
        "Start type": "启动类型",
        "Binary path": "文件路径",
        "Error control": "错误控制",
        "Group": "组",
        "Description": "描述",
        "Key modified time": "键修改时间",
        "Verification status": "验证状态",
        "Verified signer": "已验证的签名方",
        "File name": "文件名",
        "Timeline": "时间线",
        "Exit code": "退出代码",
        " (delayed, trigger)": " (延迟, 触发)",
        " (delayed)": " (延迟)",
        " (trigger)": " (触发)",
        "Service digital signature support disabled.": "服务数字签名支持已禁用。",
        "Unable to perform the operation.": "无法执行操作。",
        "This node cannot be displayed because it is currently hidden by your active filter settings or preferences.": "此节点无法显示，因为它当前已被您启用的筛选器设置或首选项隐藏。",
    }, [
        ('PhAddTreeNewColumn(hwnd, PHSVTLC_TYPE, TRUE, L"Type"',
         'PhAddTreeNewColumn(hwnd, PHSVTLC_TYPE, TRUE, L"类型"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/srvprp.c", "utf-8", {
        # todo 321, 326, 327
        #      需解决 phlib ...?
        "password": "密码",
        "Executable files (*.exe;*.sys)": "可执行文件 (*.exe;*.sys)",
        "All files (*.*)": "所有文件",
        # todo 553 L"Service",
        "Unable to change service configuration.": "无法更改服务配置。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/srvprv.c", "utf-8", {
        "Service query stage 1: %ls": "服务查询阶段 1: %ls",
        "Service query stage 2: %ls": "服务查询阶段 2: %ls",
        "Service provider run count: %lu": "服务提供程序运行计数: %lu",
        "Failed to enumerate services: %lu %!STATUS!": "无法枚举服务: %lu %!STATUS!",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/sysinfo.c", "utf-8", {
        "Unable to create the window.": "无法创建窗口。",
        "Memory": "内存",
        "Back": "返回",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/syssccpu.c", "utf-8", {
        ", Core ": ", 核心 ",
        ", Socket ": ", 插槽 ",
        ", Group ": ", 组 ",
        ", Node ": ", 节点 ",
        "Parked\n": "已停用\n",
        "Unknown": "未知",
        "Virtual machine": "虚拟机",
        "Enabled": "已启用",
        "Disabled / Hyper-V": "已禁用 / Hyper-V",
        "Disabled": "已禁用",
        "Not capable": "不支持",  # todo 不支持 or 无(额外)功能
        # todo 1987 E-Core
        # todo 1992 P-Core
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/sysscmem.c", "utf-8", {
        "Other": "其他",
        "Unknown": "未知",
        "Chip": "芯片",
        "Row of chips": "芯片组",
        "Proprietary": "专用",
        "Local non-volatile": "本地非易失",
        "Memory": "内存",
        " installed": " 已安装",
        " total": " 总计",
        "Physical memory: ": "物理内存: ",
        "Compressed memory: ": "已压缩内存: ",
        "Total compressed: ": "已压缩总计: ",
        "Total memory saved: ": "已节省内存: ",
        "Undefined": "未定义",
        " of ": ", 总计: ",
        "no symbols": "无符号",
        "no driver": "无驱动",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/thrdlist.c", "utf-8", {
        "Cycles delta": "周期增量",
        "Start address (Win32)": "起始地址 (Win32)",
        "Priority (symbolic)": "优先级 (符号)",
        "Service": "服务",
        "Name": "名称",
        "Created": "创建自",
        "Start module": "启动模块",
        "Context switches": "上下文切换",
        "Context switches delta": "上下文切换增量",
        "Priority": "优先级",
        "Base priority": "基本优先级",
        "Page priority": "页面优先级",
        "I/O priority": "I/O 优先级",
        "Cycles": "周期",
        "State": "状态",
        "Kernel time": "内核时间",
        "User time": "用户时间",
        "Ideal processor": "理想处理器",
        "Critical": "关键",
        "TID (hex)": "TID (十六进制)",
        "CPU (relative)": "CPU (相对)",
        "Impersonation": "模拟",
        "Pending IRP": "挂起 IRP",
        "Last system call": "最后一次系统调用",
        "Last status code": "最后一次状态代码",
        "Timeline": "时间线",
        "COM apartment": "COM Apartment", # 这里有不同的、非官方的翻译: “公寓”和“套间”
        # 详细信息参见: 
        # 1. https://learn.microsoft.com/en-us/windows/win32/com/processes--threads--and-apartments
        # 2. https://chat.deepseek.com/share/4zmsdgm7um8q2wl0ct
        # 3. https://zhuanlan.zhihu.com/p/135313476
        "COM flags": "COM 标志",
        "Fiber": "纤程",
        "Priority boost": "优先级提升",
        "CPU (user)": "CPU (用户)",
        "CPU (kernel)": "CPU (内核)",
        "CPU history": "CPU 历史",
        "Stack usage": "栈用量",
        "Wait time": "等待时间",
        "I/O reads": "I/O 读取",
        "I/O writes": "I/O 写入",
        "I/O other": "I/O 其他",
        "I/O read bytes": "I/O 读取字节",
        "I/O write bytes": "I/O 写入字节",
        "I/O other bytes": "I/O 其他字节",
        "Power throttling": "电源限制",
        "Container ID": "容器 ID",
        "Start address (Native)": "起始地址 (本机)",
        "RPC usage": "RPC 用量",
        "Base priority (actual)": "基本优先级 (实际)",
        "Unknown": "未知",
        "Wait:": "等待:",
        "Waiting": "等待中",
        "Anonymous": "匿名",
        "Yes": "是",
        "Implicit MTA": "隐式 MTA",
        "NTA on ": "NTA 基于 ",
        "Main STA": "主 STA",
        "Local TID": "本地 TID",
        "UUID initialized": "UUID 已初始化",
        "In thread detach": "线程分离",
        "Channel thread initialized": "通道线程已初始化",
        "WoW thread": "WoW 线程",
        "Thread uninitializing": "线程取消初始化",
        "OLE1DDE disabled": "OLE1DDE 已禁用",
        "Single threaded (STA)": "单线程 (STA)",
        "Multi threaded (MTA)": "多线程 (MTA)",
        "Impersonating": "正在模拟",
        "Eventlogger disabled": "事件日志记录已禁用",
        "Neutral threaded (NTA)": "中性线程 (NTA)",
        "Dispatch thread": "调度线程",
        "Host thread": "宿主线程",
        "Allow CoInit": "允许 CoInit",
        "Pending uninit": "挂起取消初始化",
        "First MTA init": "初次 MTA 初始化",
        "First NTA init": "初次 NTA 初始化",
        "Apartment initializing": "Apartment 正在初始化",
        "UI messages in modal loop": "模态循环中的 UI 消息",
        "Marshaling error object": "编组错误对象",
        "WinRT initialized": "WinRT 已初始化",
        "Application STA": "应用程序 STA",
        "In shutdown callbacks": "位于关机回调",
        "Pointer input blocked": "指针输入被阻止",
        "In activation filter": "位于激活筛选器",
        "ASTA-to-ASTA exempt quirk": "ASTA 到 ASTA 的豁免特性",
        "ASTA-to-ASTA exempt proxy": "ASTA 到 ASTA 的豁免代理",
        "ASTA-to-ASTA exempt in doubt": "ASTA 到 ASTA 的豁免状态存疑",
        "Bridge STA": "桥接 STA",
        "NTA initializing": "NTA 正在初始化",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/thrdprv.c", "utf-8", {
        "Real-time": "实时",
        "Idle": "空闲",
        "Background": "后台",
        "Time critical": "时间关键",
        "Highest": "最高",
        "Above normal": "高于正常",
        "Normal": "正常",
        "Below normal": "低于正常",
        "Lowest": "最低",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/thrdstk.c", "utf-8", {
        "File: ": "文件: ",
        ": line ": ": 行 ",
        "File: %s: line %lu\n": "文件: %s: 行 %lu\n",
        "Name": "名称",
        "Stack address": "栈地址",
        "Frame address": "帧地址",
        "Stack parameter #1": "栈参数 #1",
        "Stack parameter #2": "栈参数 #2",
        "Stack parameter #3": "栈参数 #3",
        "Stack parameter #4": "栈参数 #4",
        "Control address": "控制地址",
        "Return address": "返回地址",
        "File name": "文件名",
        "Line number": "行号",
        "Architecture": "架构",
        "Frame distance": "帧距离",
        "Inspecting kernel stacks requires a connection to the kernel driver.": "检查内核堆栈需要连接到内核驱动程序。",
        "Unable to open the thread.": "无法打开线程。",
        "Stack - thread %lu": "栈 - 线程 %lu",
        "Unable to load the stack.": "无法加载栈。",
        "Unable to refresh the stack.": "无法刷新栈。",
        "&Inspect": "检查(&I)",
        "Open &file location": "打开文件所在位置(&F)",
        "Copy": "复制",
        "Make sure the PE Viewer executable file is present.": "请确保 PE Viewer 可执行文件存在。",
        "Make sure the Explorer executable file is present.": "请确保资源管理器可执行文件存在。",
        "Hide user frames": "隐藏用户帧",
        "Hide system frames": "隐藏系统帧",
        "Hide inline frames": "隐藏内联帧",
        "Highlight user frames": "高亮显示用户帧",
        "Highlight system frames": "高亮显示系统帧",
        "Highlight inline frames": "高亮显示内联帧",
        "Processing stack frame #": "正在处理栈帧 #",
        "Processing stack frames...": "正在处理栈帧...",
        " (No unwind info)": " (无展开信息)",
        " (Inline function)": " (内联函数)",
        "Loading symbols...": "正在加载符号...",
        "Loading symbols for image...": "正在加载映像符号...",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/thrdstks.c", "utf-8", {
        " (No unwind info)": " (无展开信息)",
        " (Inline function)": " (内联函数)",
        " (Inline Function)": " (内联函数)",
        "Enumerating processes...": "正在枚举进程...",
        "Walking stacks... %lu%% - %ls (%lu) %lu%%": "正在遍历栈... %lu%% - %ls (%lu) %lu%%",
        "Walking stacks... %lu%% - %ls (%lu)": "正在遍历栈... %lu%% - %ls (%lu)",
        "Go to process...": "转到进程...",
        "Go to thread...": "转到线程...",
        "Expand all": "全部展开",
        "Collapse all": "全部收起",
        "Hide user frames": "隐藏用户帧",
        "Hide system frames": "隐藏系统帧",
        "Hide inline frames": "隐藏内联帧",
        "Highlight user frames": "高亮显示用户帧",
        "Highlight system frames": "高亮显示系统帧",
        "Highlight inline frames": "高亮显示内联帧",
        "Copy": "复制",
        "Stack address": "栈地址",
        "Frame address": "帧地址",
        "Stack parameter #1": "栈参数 #1",
        "Stack parameter #2": "栈参数 #2",
        "Stack parameter #3": "栈参数 #3",
        "Stack parameter #4": "栈参数 #4",
        "Control address": "控制地址",
        "Return address": "返回地址",
        "File name": "文件名",
        "Line number": "行号",
        "Architecture": "架构",
        "Frame distance": "帧距离",
        "Symbol": "符号",
        "Frame": "帧",
        "Start address": "起始地址",
        "Start address (symbolic)": "起始地址 (符号)",
        "Process name": "进程名称",
        "Thread name": "线程名称",
        "Search Thread Stacks": "搜索线程栈",
        "Unable to create the window.": "无法创建窗口。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/tokprp.c", "utf-8", {
        "Unknown": "未知",
        "No (Default)": "否 (默认)",
        "No (Full)": "否 (完全)",
        "No (Limited)": "否 (受限)",
        "Yes": "是",
        "Yes (Default)": "是 (默认)",
        "Yes (Full)": "是 (完全)",
        "Yes (Limited)": "是 (受限)",
        "Anonymous": "匿名",
        "Identification": "身份",
        "Impersonation": "模拟",
        "Delegation": "委托",
        "Primary": "候选",
        "User": "用户",
        "Group": "组",
        "Domain": "域",
        "Alias": "别名",
        "WellKnownGroup": "特定组",
        "DeletedAccount": "已删除账户",
        "Computer": "计算机",
        "Label": "标签",
        "Logon session": "已登录会话",
        "Integrity": "完整性",
        "Logon Id": "登录 ID",
        "Owner": "所有者",
        "Mandatory": "强制性",
        "Use for deny only": "仅用于拒绝",
        "Resource": "资源",
        "There are no attributes to display.": "没有要显示的属性。",
        "There are no claims to display.": "没有要显示的内容。",
        "There are no capabilities to display.": "没有要显示的能力。",
        "Unable to duplicate the token.": "无法复制令牌。",
        "Enabled (as a group)": "已启用 (作为组)",
        "Enabled": "已启用",
        "Enabled (modified)": "已启用 (已修改)",
        "Disabled (modified)": "已禁用 (已修改)",
        "Disabled": "已禁用",
        " (restricted)": " (受限)",
        "Removed": "已删除",
        "[Unknown SID]": "[未知 SID]",
        "Resolving...": "正在解析...",
        "No-Write-Up Policy": "No-Write-Up 策略",
        "Prevents the process from modifying objects with a higher integrity": "防止该进程修改具有更高完整性的对象。",
        "Sandbox Inert": "沙箱惰性",
        "Ignore AppLocker rules and Software Restriction Policies": "忽略 AppLocker 规则和软件限制策略",
        "Ignore User Interface Privilege Isolation": "忽略用户界面权限隔离",
        "Name": "名称",
        "Status": "状态",
        "Description": "描述",
        "Use": "使用",
        "Flags": "标志",
        "Privileges": "特权",
        "Restricting SIDs": "受限 SID",
        "Groups": "组",
        "Groups (Logon SID)": "组 (登录 SID)",
        "Groups (Mandatory label)": "组 (强制性标签)",
        "No": "否",
        "Not allowed": "不允许",
        "Linked Token": "已链接令牌",
        "remove": "移除",
        "the selected privilege(s)": "已选中的特权",
        "set": "设置",
        "enable": "启用",
        "disable": "禁用",
        "reset": "重置",
        "Unable to %s %s.": "无法%s %s。",
        "privilege": "特权",
        "Unable to open the token.": "无法打开令牌。",
        "group": "组",
        "the UIAccess flag": "UIAccess 标志",
        "Unable to disable UIAccess flag.": "无法禁用 UIAccess 标志。",
        "Default Token": "默认令牌",
        "Protected": "受保护",
        "System": "系统",
        "High": "高",
        "Medium +": "中等 +",
        "Medium": "中等",
        "Low": "低",
        "Untrusted": "不受信任",
        "Custom...": "自定义...",
        "Intermediate level": "中级",
        "the integrity level": "完整性级别",
        "Once lowered, the integrity level of the token cannot be raised again.": "令牌的完整性级别一旦降低，就无法再次提高。",
        "Integrity Level": "完整性级别",
        "Enter a custom integrity level:": "输入自定义完整性级别:",
        "Unable to set the integrity level": "无法设置完整性级别",
        "&Enable": "启用(&E)",
        "&Disable": "禁用(&D)",
        "Re&set": "重置(&S)",
        "&Remove": "移除(&R)",
        "&Copy": "复制(&C)",
        "Container": "容器",
        "Claims": "声明",
        "Policy": "策略",
        "Attributes": "属性",
        "Not Allowed": "不允许",
        "Unable to open the token": "无法打开令牌",
        "Value": "值",
        "General": "常规",
        "LUIDs": "LUID",
        "Memory": "内存",
        "Properties": "属性",
        "Impersonation level": "模拟级别",
        "Token LUID": "令牌 LUID",
        "Authentication LUID": "认证 LUID",
        "ModifiedId LUID": "已修改 LUID",
        "Origin LUID": "原始 LUID",
        "Memory used": "已使用内存",
        "Memory available": "可用内存",
        "Token object path": "令牌对象路径",
        "Token SDDL": "令牌 SDDL",
        # "TrustLevel": "信任级别",
        "TrustLevel Sid": "TrustLevel SID",
        "TrustLevel Name": "TrustLevel 名称",
        "Logon": "登录",
        "Token logon SID": "令牌登录 SID",
        "Token logon Name": "令牌登录名称",
        "Folder path": "文件夹路径",
        "Registry path": "注册表路径",
        "System ID": "系统 ID",
        "HWID (Publisher)": "HWID (发布者)",
        "HWID (User)": "HWID (用户)",
        "FullName: %s": "全名: %s",
        "Capability: %s": "能力: %s",
        "Package: ": "包: ",
        "Guid: ": "GUID: ",
        "Capability: ": "能力: ",
        "Capabilities": "能力",
        "Copy": "复制",
        "Invalid": "无效",
        "String": "字符串",
        "Boolean": "布尔值",
        "Octet string": "八位字符串",  # todo "八位" or "八进制"？
        "(Unknown)": "(未知)",
        "Mandatory, ": "强制, ",
        "Disabled, ": "禁用, ",
        "Default disabled, ": "默认禁用, ",
        "Use for deny only, ": "仅用于拒绝, ",
        "Case-sensitive, ": "区分大小写, ",
        "Non-inheritable, ": "不可继承, ",
        "Compare-ignore, ": "比较忽略, ",
        "(None)": "(无)",
        "Version ": "版本 ",
        "(Invalid SID)": "(无效 SID)",
        "True": "是",
        "False": "否",
        "(Octet string)": "(八位字符串)", # todo "八位" or "八进制"？
        "Shared token": "已共享令牌",
        "Trusted": "受信任",
        "Service": "服务",
        "Multiple instances allowed": "允许多实例",
        "Breakaway inhibited": "已禁止分离",
        "Runtime broker": "运行时代理",
        "Universal console": "通用控制台",
        "Win32 process": "Win32 进程",
        "Unsigned": "未签名",
        "Inbox": "收件箱",
        "Store": "存储",
        "Developer unsigned": "开发者未签名",
        "Developer signed": "开发者已签名",
        "Line of business": "业务线",
        "Undefined": "未定义",
        "Not background": "非后台",
        "Mixed host": "混合代理",
        "Pure host": "纯代理",
        "System host": "系统代理",
        "Called": "已调用",
        "App reputation called": "应用信誉度已调用",
        "Prompt displayed": "已显示提示",
        "Uninstaller": "卸载程序",
        "Ignore unknown or bad": "忽略未知或损坏信息",
        "Defender trusted installer": "Defender 可信安装程序",
        "MOTW present": "MOTW 呈现",
        "Elevated no propagation": "未传播",
        "(Octet string of ": "(八位字符串 ",
        " bytes)": " 字节)",
        "Type: %s": "类型: %s",
        "Flags: %s (0x%lx)": "标志: %s (0x%lx)",
        "Value %u: %s": "值 %u: %s",
        "User claims": "用户声明",
        "Device claims": "设备声明",
        "Parent": "父对象",
        "Package": "包",
        "Number": "编号",
        "Path": "路径",
        "Child": "子对象",
        "None": "无",
        "Known": "已知",
        "Allowed": "已允许",
        "Denied": "已拒绝",
        "Full": "完全",
        "Limited": "受限",
        "Unmanaged": "未管理",
        "Others": "其他",
        "Universal": "通用",
        "All": "全部",
        "Agile": "灵敏",
        "NonAgile": "非灵敏",
        "Caller": "调用方",
        "Isolated": "已隔离",
        "CopyOnWrite": "写时复制",
        "Normal": "正常",
        "Virtualized": "已虚拟化",
        "Unrestricted": "未受限",
        "Default": "默认",
        "NoWake": "非唤醒",
        "Wake": "唤醒",
        "Unsupported": "不受支持",
        "Manifested": "显现",
        # todo VOID PhEnumTokenAppModelPolicy(...) {...}
        "Initializing kernelbase symbols...": "正在初始化 kernelbase 符号...",
        "There are no policies to display.": "没有要显示的策略。",
    }, [
        ('PhAddIListViewColumn(tokenPageContext->ListViewClass, 4, 4, 4, LVCFMT_LEFT, 100, L"Type"',
         'PhAddIListViewColumn(tokenPageContext->ListViewClass, 4, 4, 4, LVCFMT_LEFT, 100, L"类型"'),
        ('''L"Removing privileges may reduce the functionality of the process, "
                            L"and is permanent for the lifetime of the process."''',
         'L"移除权限可能会降低进程的功能，并且对进程的生命周期是永久性的。"'),
        ('''L"Removing this flag may reduce the functionality of the process "
                        L"provided it is an accessibility application."''',
         'L"如果这是一个辅助功能应用程序，移除此标志可能会降低该进程的功能。"'),
        ('propSheetHeader.pszCaption = L"Token"', 'propSheetHeader.pszCaption = L"令牌"'),
        ('PhAddIListViewGroupItem(context->ListView, 0, MAXINT, L"Type"', 'PhAddIListViewGroupItem(context->ListView, 0, MAXINT, L"类型"'),
        ('PhAddIListViewGroup(context->ListView, listViewGroupIndex++, L"Profile"', 'PhAddIListViewGroup(context->ListView, listViewGroupIndex++, L"配置文件"'),
        ('PhAddIListViewGroup(context->ListView, 4, L"Profile"', 'PhAddIListViewGroup(context->ListView, 4, L"配置文件"'),
        ('PhAddListViewColumn(tokenPageContext->ListViewHandle, 4, 4, 4, LVCFMT_LEFT, 100, L"Type")',
         'PhAddListViewColumn(tokenPageContext->ListViewHandle, 4, 4, 4, LVCFMT_LEFT, 100, L"类型")'),
        ('PhAddListViewGroupItem(context->ListViewHandle, 0, MAXINT, L"Type"',
         'PhAddListViewGroupItem(context->ListViewHandle, 0, MAXINT, L"类型"'),
        ('PhAddListViewGroup(context->ListViewHandle, listViewGroupIndex++, L"Profile"',
         'PhAddListViewGroup(context->ListViewHandle, listViewGroupIndex++, L"配置文件"'),
        ('PhAddListViewGroup(context->ListViewHandle, 4, L"Profile"',
         'PhAddListViewGroup(context->ListViewHandle, 4, L"配置文件"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/usrlist.c", "utf-8", {
        "Guest": "来宾",
        "No encryption": "未加密",
        "Cached account": "已缓存账户",
        "Used LM password": "已使用 LM 密码",
        "Extra SIDs": "扩展 SID",
        "Subauth session key": "子认证会话密钥",
        "Server trust account": "服务器信任账户",
        "NTLMv2 enabled": "NTLMv2 已启用",
        "Resource groups": "资源组",
        "Profile path returned": "配置文件路径返回",
        "Optimized": "已优化",
        "WinLogon created": "已创建 WinLogon",
        "Not optimized": "未优化",
        "No elevation": "无提升",
        "Managed service": "受管理服务",
        "Number of users: ": "用户数量: ",
        "Undefined": "未定义",
        "Interactive": "交互式",
        "Network": "网络",
        "Batch": "批处理",
        "Service": "服务",
        "Proxy": "代理",
        "Unlock": "解锁",
        "Network cleartext": "网络明文",
        "New credentials": "新凭据",
        "Remote interactive": "远程交互",
        "Cached interactive": "已缓存交互",
        "Cached remote interactive": "已缓存远程交互",
        "Cached unlock": "已缓存解锁",
        "Copy": "复制",
        "User name": "用户名",
        "Logon domain": "登录域",
        "Session ID": "会话 ID",
        "Logon type": "登录类型",
        "Authentication package": "认证包",
        "DNS domain name": "DNS 域名",
        "Logon time": "登录时间",
        "Password last set": "密码最后设置于",
        "Logon ID": "登录 ID",
        "Logon server": "登录服务器",
        "User principal name": "用户主体名称",
        "User flags": "用户标志",
        "Failed logon attempts since": "自上次登录尝试以来失败的次数",
        "Last successful logon": "上次成功登录",
        "Last failed logon": "上次登录失败",
        "Longon script": "登录脚本",  # 源代码拼写错误: PH_USER_LIST_COLUMN_PROFILE_PATH
        "Logon script": "登录脚本",
        "Profile path": "配置文件路径",
        "Home directory": "主目录",
        "Home directory drive": "主目录驱动器",
        "Logoff time": "登出时间",
        "Kickoff time": "启动时间",
        "Password can set": "密码可以设置",
        "Password must set": "密码必须设置",
        "Search Users": "搜索用户",
        "Unable to locate routines.": "无法定位例程。",
        "Unable to create the window.": "无法创建窗口。",
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/ksisup.c", "utf-8", {
        "    - not securely created\r\n": "    - 未安全创建\r\n",
        "    - unverified primary image\r\n": "    - 未验证主要映像\r\n",
        "    - inactive protections\r\n": "    - 未激活保护\r\n",
        "    - unsigned images (likely an unsigned plugin)\r\n": "    - 未签名映像 (可能是未签名插件)\r\n",
        "    - process is being debugged\r\n": "    - 进程正在被调试\r\n",
        "    - tampered primary image\r\n": "    - 已修改主要映像\r\n",
        "You will be unable to use more advanced features, view details about system processes or terminate malicious software.": "您将无法使用更高级的功能，查看系统进程的详细信息或终止恶意软件。",
        "Access to the kernel driver is restricted.": "内核驱动程序的访问权限已受到限制。",
        "Unknown error.": "未知错误。",
        "Unknown": "未知",
        "Process State ": "进程状态 ",
        "Windows Kernel ": "Windows 内核 ",
        "Driver warnings are disabled.": "驱动程序警告已禁用。",
        "Unable to load kernel driver": "无法加载内核驱动程序",
        "The dynamic configuration was not found.": "未找到动态配置。",
        "Failed to access the dynamic configuration.": "访问动态配置时出现错误。",
        "The kernel driver was not found.": "未找到内核驱动程序。",
        "Try again with alternate driver load method?": "请尝试使用其他驱动程序加载方式?",
        "Kernel driver loaded": "已加载内核驱动程序",
        "Unable to load the kernel driver service.": "无法加载内核驱动程序服务。",
        "Unable to restart.": "无法重新启动。",
        "Unable to create the window.": "无法创建窗口。",
        "Initializing System Informer kernel driver...": "正在初始化 System Informer 内核驱动程序...",
        "The last System Informer update requires a reboot.": "需重新启动 System Informer 以应用最新更新。",
        "The kernel driver is not supported on this architecture.": "内核驱动程序不支持此架构。",
        "Platform support pending review.": "平台支持待审核。",
        "Kernel version not supported": "内核版本不受支持",
        "Checking for pending platform update...": "正在检查待处理的平台更新...",
    }, [
        ('''L"The kernel driver is not yet supported on this kernel "
                L"version. For the latest kernel support switch to the Canary "
                L"update channel (Help > Check for updates > Canary > Check)."''',
         'L"此内核版本尚不支持内核驱动程序。要获得最新的内核支持，请切换到 Canary 更新通道（帮助 > 检查更新 > Canary > 检查）。"'),
        ('''L"The kernel driver is not yet supported on this kernel "
                L"version. Request support by submitting a GitHub issue with "
                L"the Windows Kernel version."''',
         'L"此内核版本尚不支持内核驱动程序。请提交 GitHub issue 并注明 Windows 内核版本，以请求支持。"'),
        ('''L"The kernel driver was successfully loaded using an alternate "
                L"method. The settings used to load the driver have been saved. "
                L"You can revert these settings in the advanced options."''',
         'L"内核驱动程序已使用备用方法成功加载。用于加载驱动程序的设置已保存。您可以在高级选项中恢复这些设置。"'),
        ('''L"The kernel driver is not supported on this Windows version, the "
            L"minimum supported version is Windows 10."''',
         'L"此 Windows 版本不支持内核驱动程序，最低支持版本为 Windows 10。"'),
        ('''L"The kernel driver is not supported under Wow64, use the native "
            "binary instead."''',
         'L"Wow64 不支持内核驱动程序，请改用本地二进制文件。"'),
        ('''L"Your kernel version is pending review on the development branch. "
                        L"Your kernel will be supported in the next build!"''',
         'L"您的内核版本正在开发分支上等待审核。您的内核将在下一个版本中得到支持！"'),
        ('''L"This kernel version is not yet supported. "
                            L"Your kernel version is pending review review on the development branch."''',
         'L"此内核版本尚不受支持。您的内核版本正在开发分支上等待审核。"'),
        ('''L"This kernel version is not yet supported. "
                            L"For the latest kernel support switch to the Canary update channel "
                            L"(Help > Check for updates > Canary > Check)."''',
         'L"此内核版本尚不受支持。要获得最新的内核支持，请切换到 Canary 更新通道（帮助 > 检查更新 > Canary > 检查）。"'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/ksidbg.c", "utf-8", {
        r"%04x:%04x:%016llx created process %lu (%016llx)%ls(parent %lu (%016llx)) \"%wZ\" \"%wZ\"":
            r"%04x:%04x:%016llx 已创建进程 %lu (%016llx)%ls(父进程 %lu (%016llx)) \"%wZ\" \"%wZ\"",
        " subsystem process ": " 子系统进程 ",
        "%04x:%04x:%016llx process exited with %ls (0x%08x)": "%04x:%04x:%016llx 进程已退出，退出代码 %ls (0x%08x)",
        "UNKNOWN": "未知",
        "%04x:%04x:%016llx thread %lu created in process %lu (%016llx)": "%04x:%04x:%016llx 线程 %lu 已创建于进程 %lu (%016llx)",
        "%04x:%04x:%016llx thread beginning execution": "%04x:%04x:%016llx 线程正在开始执行",
        "%04x:%04x:%016llx thread exited with %ls (0x%08x)": "%04x:%04x:%016llx 线程已退出，退出代码 %ls (0x%08x)",
        r"%04x:%04x:%016llx image \"%wZ\" loaded into process %lu (%016llx) at %p":
            r"%04x:%04x:%016llx 映像 \"%wZ\" 已加载至进程 %lu (%016llx) 的 %p 处",
        "%04x:%04x:%016llx %c %p %llu granted 0x%08x (desired 0x%08x, original 0x%08x) to process %lu (duplicate %lu -> %lu) %llu %llu %ls (0x%08x)":
            "%04x:%04x:%016llx %c %p %llu 已授予 0x%08x (请求 0x%08x, 原始值 0x%08x) 进程 %lu (复制 %lu -> %lu) %llu %llu %ls (0x%08x)",
        "%04x:%04x:%016llx %c %p %llu granted 0x%08x (desired 0x%08x, original 0x%08x) to process %lu %llu %llu %ls (0x%08x)":
            "%04x:%04x:%016llx %c %p %llu 已授予 0x%08x (请求 0x%08x, 原始值 0x%08x) 进程 %lu %llu %llu %ls (0x%08x)",
        "%04x:%04x:%016llx %c %p desires 0x%08x (original 0x%08x) to process %lu (duplicate %lu -> %lu)":
            "%04x:%04x:%016llx %c %p 请求 0x%08x (原始值 0x%08x) 进程 %lu (复制 %lu -> %lu)",
        "%04x:%04x:%016llx %c %p desires 0x%08x (original 0x%08x) to process %lu": "%04x:%04x:%016llx %c %p 请求 0x%08x (原始值 0x%08x) 给进程 %lu",
        "%04x:%04x:%016llx %c %p %llu granted 0x%08x (desired 0x%08x, original 0x%08x) to thread %lu (process %lu, duplicate %lu -> %lu) %llu %llu %ls (0x%08x)":
            "%04x:%04x:%016llx %c %p %llu 已授予 0x%08x (请求 0x%08x, 原始值 0x%08x) 线程 %lu (进程 %lu, 复制 %lu -> %lu) %llu %llu %ls (0x%08x)",
        "%04x:%04x:%016llx %c %p %llu granted 0x%08x (desired 0x%08x, original 0x%08x) to thread %lu (process %lu) %llu %llu %ls (0x%08x)":
            "%04x:%04x:%016llx %c %p %llu 已授予 0x%08x (请求 0x%08x, 原始值 0x%08x) 线程 %lu (进程 %lu) %llu %llu %ls (0x%08x)",
        "%04x:%04x:%016llx %c %p %llu desires 0x%08x (original 0x%08x) to thread %lu (process %lu, duplicate %lu -> %lu)":
            "%04x:%04x:%016llx %c %p %llu 请求 0x%08x (原始值 0x%08x) 线程 %lu (进程 %lu, 复制 %lu -> %lu)",
        "%04x:%04x:%016llx %c %p %llu desires 0x%08x (original 0x%08x) to thread %lu (process %lu)":
            "%04x:%04x:%016llx %c %p %llu 请求 0x%08x (原始值 0x%08x) 线程 %lu (进程 %lu)",
        r"%04x:%04x:%016llx %c %p %llu granted 0x%08x (desired 0x%08x, original 0x%08x) to desktop \"%wZ\" (duplicate %lu -> %lu) %llu %llu %ls (0x%08x)":
            r"%04x:%04x:%016llx %c %p %llu 已授予 0x%08x (请求 0x%08x, 原始值 0x%08x) 桌面 \"%wZ\" (复制 %lu -> %lu) %llu %llu %ls (0x%08x)",
        r"%04x:%04x:%016llx %c %p %llu granted 0x%08x (desired 0x%08x, original 0x%08x) to desktop \"%wZ\" %llu %llu %ls (0x%08x)":
            r"%04x:%04x:%016llx %c %p %llu 已授予 0x%08x (请求 0x%08x, 原始值 0x%08x) 桌面 \"%wZ\" %llu %llu %ls (0x%08x)",
        r"%04x:%04x:%016llx %c %p %llu desires 0x%08x (original 0x%08x) to desktop \"%wZ\" (duplicate %lu -> %lu)":
            r"%04x:%04x:%016llx %c %p %llu 请求 0x%08x (原始值 0x%08x) 桌面 \"%wZ\" (复制 %lu -> %lu)",
        r"%04x:%04x:%016llx %c %p %llu desires 0x%08x (original 0x%08x) to desktop \"%wZ\"": r"%04x:%04x:%016llx %c %p %llu 请求 0x%08x (原始值 0x%08x) 桌面 \"%wZ\"",
        "%04x:%04x required state failure, message %lu, state 0x%08x, required 0x%08x": "%04x:%04x 需要状态失败，消息 %lu，状态 0x%08x，需要 0x%08x",
        ", paging file": ", 分页文件",
        ", system paging file": ", 系统分页文件",
        ", remote origin": ", 远程原始数据",
        ", ignoring sharing": ", 忽略共享",
        ", in stack file object": ", 位于栈文件对象",
        ", delete pending": ", 删除挂起",
        ", opened exclusively": ", 独占打开",
        ", busy": ", 忙碌",
        ", waiters": ", 等待器",
        ", oplock key": ", oplock 键",
        ", transaction": ", 转换",
        ", data section": ", 数据节",
        ", image section": ", 映像节",
        "NULL": "空",
        "Debug Log Finalize": "调试日志完成",
        "%llu messages totaling %.4f GB": "%llu 条消息总计 %.4f GB",
        # todo static SI_DEBUG_LOG_DEF KsiDebugLogDefs[] = ...
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/log.c", "utf-8", {
        ") started by ": ") 创建方 ",
        "Unknown process": "未知进程",
        "Process created: %s (%lu) started by %s (%lu)": "进程已创建: %s (%lu) 创建方 %s (%lu)",
        "); exit status ": "); 退出代码 ",
        "Process terminated: %s (%lu); exit status 0x%x": "进程已退出: %s (%lu); 退出代码 0x%x",
        "Service created: %s (%s)": "服务已创建: %s (%s)",
        "Service deleted: %s (%s)": "服务已删除: %s (%s)",
        "Service started: %s (%s)": "服务已启动: %s (%s)",
        "Service stopped: %s (%s)": "服务已停止: %s (%s)",
        "Service continued: %s (%s)": "服务已恢复运行: %s (%s)",
        "Service paused: %s (%s)": "服务已暂停: %s (%s)",
        "Service modified: %s (%s)": "服务已修改: %s (%s)",
        "Service stopped: ": "服务已停止: ",
        "Service started: ": "服务已启动: ",
        "Service deleted: ": "服务已删除: ",
        "Service created: ": "服务已创建: ",
        "Process created: ": "进程已创建: ",
        "Process terminated: ": "进程已退出: ",
        "Service paused: ": "服务已暂停: ",
        "Service continued: ": "服务已恢复运行: ",
        "Service modified: ": "服务已修改: ",
        "Device removed: ": "设备已移除: ",
        "Device arrived: ": "设备已就绪: ",
        "Service stopped": "服务已停止",
        "Service started": "服务已启动",
        "Service deleted": "服务已删除",
        "Service created": "服务已创建",
        "Process created": "进程已创建",
        "Process terminated": "进程已退出",
        "Service paused": "服务已暂停",
        "Service continued": "服务已恢复运行",
        "Service modified": "服务已修改",
        "Device removed": "设备已移除",
        "Device arrived": "设备已就绪",
        "Service terminated": "服务已终止",
        "Unknown": "未知",
    }, []),
]

if OPTION_TRANSLATE_SECURITY_EDITOR_MANDATORY_LEVEL == EnumTranslateSecurityEditorMandatoryLevel.EnumWindowAndSubwindowTranslate:
    DATA.append(
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/main.c", "utf-8", {}, [

#####################################################################
(
'''static PH_AUTO_POOL BaseAutoPool;

INT WINAPI wWinMain(
    _In_ HINSTANCE Instance,
    _In_opt_ HINSTANCE PrevInstance,
    _In_ PWSTR CmdLine,
    _In_ INT CmdShow
    )
{''',
# 旧字符串 ============================================ 新字符串
'''static PH_AUTO_POOL BaseAutoPool;

/////////////////////////////////////////////////////////////////////////////////////////
// 以下代码由 ANONYMOUS9075331734 插入
// 全局变量定义
wchar_t Zyx220623_szSearchStringBuffer[256] = L"...";
wchar_t Zyx220623_szReplaceStringBuffer[256] = L"...";
HANDLE Zyx220623_hReplaceThreadHandle = NULL;
BOOL Zyx220623_isReplaceThreadRunning = FALSE;

// 回调函数声明
BOOL CALLBACK Zyx220623_EnumChildWindowsProc(HWND hwndChild, LPARAM lParam);
BOOL CALLBACK Zyx220623_EnumWindowsProc(HWND hwnd, LPARAM lParam);
DWORD WINAPI Zyx220623_ReplaceThreadProc(LPVOID lpParameter);
BOOL Zyx220623_StartTextReplaceThread();
BOOL Zyx220623_StopTextReplaceThread();

typedef struct _Zyx220623_ReplaceTextStruct {
    wchar_t SearchString[256];
    wchar_t ReplaceString[256];
} Zyx220623_ReplaceTextStruct, *pZyx220623_ReplaceTextStruct;

Zyx220623_ReplaceTextStruct Zyx220623_GlobalReplaceStructList[] = {
    {.SearchString = L"High Mandatory Level", .ReplaceString = L"高强制性级别"},
    {.SearchString = L"Medium Mandatory Level", .ReplaceString = L"中强制性级别"},
    {.SearchString = L"Low Mandatory Level", .ReplaceString = L"低强制性级别"},
    {.SearchString = L"Medium+ Mandatory Level", .ReplaceString = L"中+强制性级别"},
    {.SearchString = L"Medium + Mandatory Level", .ReplaceString = L"中+强制性级别"},
    {.SearchString = L"System Mandatory Level", .ReplaceString = L"系统强制性级别"},
    {.SearchString = L"Protected Mandatory Level", .ReplaceString = L"受保护强制性级别"},
    {.SearchString = L"Custom Mandatory Level", .ReplaceString = L"自定义强制性级别"},
    {.SearchString = L"Untrusted Mandatory Level", .ReplaceString = L"不受信任强制性级别"}, 
};
INT Zyx220623_GlobalReplaceStructListLength = sizeof(Zyx220623_GlobalReplaceStructList) / sizeof(Zyx220623_ReplaceTextStruct);

// 定义
BOOL Zyx220623_ReplaceWindowText(HWND hwnd)
{
    int nLength = GetWindowTextLengthW(hwnd);
    if (nLength == 0)
        return FALSE;

    wchar_t* pszText = (wchar_t*)malloc((nLength + 1) * sizeof(wchar_t));
    if (!pszText)
        return FALSE;

    GetWindowTextW(hwnd, pszText, nLength + 1);

    pZyx220623_ReplaceTextStruct CurrentReplaceStruct;
    for (int i = 0; i < Zyx220623_GlobalReplaceStructListLength; i++)
    {
        CurrentReplaceStruct = &(Zyx220623_GlobalReplaceStructList[i]);
        wcscpy_s(Zyx220623_szSearchStringBuffer, _countof(Zyx220623_szSearchStringBuffer), CurrentReplaceStruct->SearchString);
        wcscpy_s(Zyx220623_szReplaceStringBuffer, _countof(Zyx220623_szReplaceStringBuffer), CurrentReplaceStruct->ReplaceString);
        wchar_t* pFound = wcsstr(pszText, Zyx220623_szSearchStringBuffer);
        if (pFound != NULL)
        {
            wchar_t szNewText[1024] = { 0 };
            size_t nPrefixLen = pFound - pszText;
            wcsncpy_s(szNewText, _countof(szNewText), pszText, nPrefixLen);
            wcscat_s(szNewText, _countof(szNewText), Zyx220623_szReplaceStringBuffer);
            wcscat_s(szNewText, _countof(szNewText), pFound + wcslen(Zyx220623_szSearchStringBuffer));
            SetWindowTextW(hwnd, szNewText);
        }
    }

    free(pszText);
    return TRUE;
}

BOOL CALLBACK Zyx220623_EnumChildWindowsProc(HWND hwndChild, LPARAM lParam)
{
    Zyx220623_ReplaceWindowText(hwndChild);
    EnumChildWindows(hwndChild, Zyx220623_EnumChildWindowsProc, 0);

    return TRUE;
}

BOOL CALLBACK Zyx220623_EnumWindowsProc(HWND hwnd, LPARAM lParam)
{
    Zyx220623_ReplaceWindowText(hwnd);
    EnumChildWindows(hwnd, Zyx220623_EnumChildWindowsProc, 0);

    return TRUE;
}

DWORD WINAPI Zyx220623_ReplaceThreadProc(LPVOID lpParameter)
{
    Zyx220623_isReplaceThreadRunning = TRUE;

    while (TRUE) 
    {
        EnumWindows(Zyx220623_EnumWindowsProc, 0);
        Sleep(50);
    }

    Zyx220623_isReplaceThreadRunning = FALSE;
    return 0;
}

BOOL Zyx220623_StartTextReplaceThread()
{
    if (Zyx220623_isReplaceThreadRunning)
    {
        return FALSE;
    }
    Zyx220623_hReplaceThreadHandle = CreateThread(NULL, 0, Zyx220623_ReplaceThreadProc, NULL, 0, NULL);

    if (Zyx220623_hReplaceThreadHandle == NULL)
    {
        return FALSE;
    }
    return TRUE;
}

BOOL Zyx220623_StopTextReplaceThread()
{
    if (!Zyx220623_isReplaceThreadRunning || Zyx220623_hReplaceThreadHandle == NULL)
        return TRUE;

    TerminateThread(Zyx220623_hReplaceThreadHandle, 0);

    CloseHandle(Zyx220623_hReplaceThreadHandle);
    Zyx220623_hReplaceThreadHandle = NULL;
    Zyx220623_isReplaceThreadRunning = FALSE;
    return TRUE;
}
/////////////////////////////////////////////////////////////////////////////////////////

INT WINAPI wWinMain(
    _In_ HINSTANCE Instance,
    _In_opt_ HINSTANCE PrevInstance,
    _In_ PWSTR CmdLine,
    _In_ INT CmdShow
    )
{'''),
#####################################################################
(
'''INT WINAPI wWinMain(
    _In_ HINSTANCE Instance,
    _In_opt_ HINSTANCE PrevInstance,
    _In_ PWSTR CmdLine,
    _In_ INT CmdShow
    )
{
    LONG result;
#ifdef DEBUG
    PHP_BASE_THREAD_DBG dbg;
#endif

    if (!NT_SUCCESS(PhInitializePhLib(L"System Informer")))
        return 1;
    if (!NT_SUCCESS(PhInitializeDirectoryPolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeExceptionPolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeExecutionPolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeNamespacePolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeComPolicy()))
        return 1;

    PhpProcessStartupParameters();
    PhpEnablePrivileges();

    if (PhStartupParameters.RunAsServiceMode)''',
# 旧字符串 ============================================ 新字符串
'''INT WINAPI wWinMain(
    _In_ HINSTANCE Instance,
    _In_opt_ HINSTANCE PrevInstance,
    _In_ PWSTR CmdLine,
    _In_ INT CmdShow
    )
{
    LONG result;
#ifdef DEBUG
    PHP_BASE_THREAD_DBG dbg;
#endif

    if (!NT_SUCCESS(PhInitializePhLib(L"System Informer")))
        return 1;
    if (!NT_SUCCESS(PhInitializeDirectoryPolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeExceptionPolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeExecutionPolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeNamespacePolicy()))
        return 1;
    if (!NT_SUCCESS(PhInitializeComPolicy()))
        return 1;

    PhpProcessStartupParameters();
    PhpEnablePrivileges();
    /////////////////////////////////////////////////////////////////////////////////////////
    // 以下代码由 ANONYMOUS9075331734 插入
    Zyx220623_StartTextReplaceThread();
    /////////////////////////////////////////////////////////////////////////////////////////

    if (PhStartupParameters.RunAsServiceMode)'''),
#####################################################################
('''PhEnableTerminationPolicy(TRUE);

    PhDrainAutoPool(&BaseAutoPool);

    result = PhMainMessageLoop();

    PhEnableTerminationPolicy(FALSE);

    if (PhEnableKsiSupport)
    {
        PhCleanupKsi();
    }

    PhExitApplication(result);
    return result;
}''',
# 旧字符串 ============================================ 新字符串
'''PhEnableTerminationPolicy(TRUE);

    PhDrainAutoPool(&BaseAutoPool);

    result = PhMainMessageLoop();

    PhEnableTerminationPolicy(FALSE);

    if (PhEnableKsiSupport)
    {
        PhCleanupKsi();
    }

    PhExitApplication(result);
    /////////////////////////////////////////////////////////////////////////////////////////
    // 以下代码由 ANONYMOUS9075331734 插入
    Zyx220623_StopTextReplaceThread();
    /////////////////////////////////////////////////////////////////////////////////////////
    return result;
}'''),
#####################################################################
    ]),
)