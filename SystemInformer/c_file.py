# 本文件存储 System Informer 源码汉化数据。
# 作者：anonymous9075 (anonymous9075331734@proton.me)

from Config.const_values import CONST_PATH_SYSTEM_INFORMER_SRC
from Config.global_dict import GLOBAL_DICT
from Config.static_data_type import translation_data_type
from Payload.misc_functions import pre_format_string

DATA: translation_data_type = [
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
            "将改为创建 64 位转储文件。是否继续？", 
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
        "You are about to ": "你即将",
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
        " and its descendants": " 及其子进程",
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
        "The process will be restarted with the same command line, ":
            "该进程将使用相同的命令行重新启动， ",
        "working directory and privileges.": "工作目录和权限。",
        "debug": "调试",
        "Debugging a process may result in loss of data.": "调试进程可能会导致数据丢失。",
        # todo: line 2767
        "Unable to locate the debugger.": "无法定位调试器。",
        "reduce the working set of": "减少以下进程的工作集占用：",
        "empty the working set of": "清空以下进程的工作集占用：",
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
        "%s ago (%s)": "%s 前 (%s)",
        "set background activity moderation for": "为以下进程设置后台活动调节：",
        "set virtualization for": "为以下进程启用虚拟化：",
        "set critical status for": "为以下进程启用关键状态：",
        "set Eco mode for": "为以下进程启用节能模式：",
        "create execution required state for": "为以下进程创建执行所需状态",
        "Unable to detach the debugger.": "无法断开与调试器的连接。",
        "The process is not being debugged.": "该进程未进行调试。",
        "detach debugger from": "断开调试器与以下进程的连接",
        "DLL files (*.dll)": "DLL 文件 (*.dll)",
        "All files (*.*)": "所有文件 (*.*)",
        "load the DLL into": "加载 DLL 至以下进程：",
        "Unable to set the I/O priority of ": "无法为以下进程设置 I/O 优先级：",
        "set the I/O priority of": "为以下进程设置 I/O 优先级：",
        "set the page priority of": "为以下进程设置页面优先级：",
        "Unable to set the priority class of ": "无法为以下进程设置优先级类：",
        "set the priority class of": "为以下进程设置优先级类：",
        "change boost priority of": "为以下进程更改优先级提升值：",
        "set the boost priority of": "为以下进程设置优先级提升值：",
        "the selected service": "已选中的服务",
        "the selected services": "已选中的服务",
        "Close": "关闭",
        "Unable to %s services:": "无法%s服务:",
        "Attempting to ": "正在尝试",
        " Are you sure you want to continue?": " 你确定要继续吗?",
        "Initializing...": "初始化中...",
        "Unable to %s %s.": "无法%s %s.",
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
            "卸载模块可能会导致进程崩溃。注意：此功能可能无法在您的 Windows "
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
            '''L"为进程",
            L"启用虚拟化",
            L"为进程启用或禁用虚拟化可能"
            L"改变其功能并产生不良影响。"'''
        ), ('''L"enable",
                L"critical status on the process",
                L"If the process ends, the operating system will shut down immediately."''',
            '''L"为该进程",
                L"启用关键状态",
                L"如果此类进程结束，操作系统将立即关闭。"'''
        ), ('''L"disable",
                L"critical status on the process"''',
            '''L"为该进程",
                L"禁用关键状态"'''
        ), (
            '''L"enable",
                    L"Eco mode for this process",
                    L"Eco mode will lower process priority and improve power efficiency but may cause instability in some processes."''',
            '''L"为该进程",
                    L"启用节能模式",
                    L"节能模式会降低进程优先级并提高电源效率，但可能会导致某些进程不稳定。"'''
        ), (
            '''L"change the execution required state",
            PhaConcatStrings2(L"of ", Process->ProcessName->Buffer)->Buffer,
            L"The process continues to run instead of being suspended or terminated by process lifetime management (PLM)."''',
            '''L"更改进程 ",
            PhaConcatStrings2(Process->ProcessName->Buffer, L" 的执行所需状态")->Buffer,
            L"该进程会继续运行，而不是被进程生命周期管理模块 (PLM) 挂起或终止。"'''
        ), (
            'Config.pszMainInstruction = PhaConcatStrings(3, L"Do you want to ", action->Buffer, L"?")->Buffer',
            'Config.pszMainInstruction = PhaConcatStrings(3, L"你想要", action->Buffer, L"吗?")->Buffer'
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
            'PhpShowErrorThread(WindowHandle, L"为以下线程更改优先级：", Threads[i], status, 0)'
        ), (
            'PhpShowErrorThread(WindowHandle, L"set the priority of", Thread, status, 0)',
            'PhpShowErrorThread(WindowHandle, L"为以下线程设置优先级", Thread, status, 0)'
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
            'PhpShowErrorHandle(WindowHandle, L"设置以下句柄的属性：", NULL, Handle, status, 0)'
        ), (
            'PhpShowErrorProcess(WindowHandle, L"flush the process heap(s) of", Processes[i], status, 0)',
            'PhpShowErrorProcess(WindowHandle, L"刷新以下进程的堆：", Processes[i], status, 0)'
        )
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
    #     "[fail]: writers active in read zone!\n": "[失败]：读取区域中有处于活动状态的写入区域!\n",  # todo
    #     "[fail]: readers active in write zone!\n": "[失败]：写入区域中有处于活动状态的读取区域!\n", # todo
    #     "[null] %s: %ums\n": "[空] %s: %ums\n", # and line 586: L"[strs] %s: %ums\n"
    #     pre_format_string("Press Ctrl+C or type \"exit\" to close the debug console. "
    #                       "Type \"help\" for a list of commands.\n"):
    #         pre_format_string("按 Ctrl+C 或输入 \"exit\" 关闭调试控制台。输入 \"help\" 查看命令列表。\n"),
    #     "This command is not available on non-debug builds.\n": "此命令在非调试版本中不可用。\n",
    #     "Commands:\n": "可用的命令:\n",
    #     "Referencing: %ums\n": "正在引用: %ums\n",
    #     "Critical section: %ums\n": "关键节区: %ums\n",
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
    #         "警告：用户模式堆栈跟踪数据库未启用。堆栈跟踪将不会显示。\n",
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
            "Filtered": "已过滤",
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
        "Unable to create the window.": "无法创建窗口。"
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
        "Critical section": "关键节区",
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
        "Brute force": "暴力破解",
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
        "Brute Force\r\n": "暴力破解\r\n",
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
        "Unable to open key.": "无法打开键。",
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
        'Asynchronous': "异步",
        'Write through': "直写",
        'Sequential': '顺序',
        'No buffering': '无缓冲',
        'Synchronous alert': '同步警报',
        'Synchronous non-alert': '同步非警报',
        'LPC mode': 'LPC 模式',
        'Allow impersonation': "允许模拟",
        'Allow LPC requests': "允许 LPC 请求",
        'Waitable': "可等待",
        'Allow object duplication': "允许对象复制",
        'System process only': "仅系统线程",
        'Wake policy (1)': "唤醒策略 (1)",
        'Wake policy (2)': "唤醒策略 (2)",
        'Wake policy (3)': "唤醒策略 (3)",
        'No shared section (direct)': "无共享节区 (直接)",
        'Allow multi-handle attributes': "允许多句柄属性",
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
        'Low': "低",
        'Normal': "正常",
        'High': "高",
        'Critical': "关键",
        "Unknown": "未知",
        'Commit': "提交",
        'Image': "映像",
        'Reserve': "保留",
        "Value": "值",
        "&Copy": "复制(&C)",
        ' (User)': " (用户)",
        ' (Group)': " (组)",
        ' (Computer)': " (计算机)",
        'Allow': "允许",
        'Group': "组",
        'Integrity': "完整性",
        'Auditing information': "审核信息",
        'Access': "访问权限",
        'Principal': "主要",
        'Integrity level': "完整性级别",
        'Unable to disable the integrity level.': "无法禁用完整性级别。",
        'Inherited from': "继承自",
        'Source': "源",
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
        'Unable to open the process': "无法打开进程",
        'Unable to enumerate process handles': "无法枚举进程句柄",
        'Count': "计数",
        '(unknown: %lu)': '(未知: %lu)',
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
        "Console application": "命令行应用程序",
        "Console host": "命令行宿主程序",
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
        'Unknown': "未知",
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
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/main.c", "utf-8", {
        "Warning.": "警告",
        "You are attempting to run the 32-bit version of System Informer on 64-bit Windows. ":
            "您尝试在 64 位 Windows 系统上运行 32 位版本的 System Informer。",
        "Most features will not work correctly.\n\n": "大多数功能将无法正常工作。\n\n",
        "Please run the 64-bit version of System Informer instead.": "请改用 64 位版本的 System Informer。",
        "Unable to create the window.": "无法创建窗口。",
        "Found previous instance window: %ls (%p)": "找到之前的实例窗口: %ls (%p)",
        "Foreground previous instance: %lu": "前一个实例: %lu",
        "Foreground previous instance: %lu (%lu attempts)": "前一个实例: %lu (尝试次数：%lu)",
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
    }, []),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/mainwnd.c", "utf-8", {
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
        "&Always on top": "窗口置顶(&A)",
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
        "WMI Root Namespace": "WMI 根命名空间",
        "COM Access Permissions": "COM 访问权限",
        "COM Access Restrictions": "COM 访问限制",
        "COM Launch Permissions": "COM 启动权限",
        "COM Launch Restrictions": "COM 启动限制",
        "Current Window Desktop": "当前窗口所在桌面",
        "Current Window Station": "当前窗口站",
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
        "&Arrived devices": "已到达设备(&A)",
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
        "%u bytes per row": "每行 %u 字节",
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
    }, []),
]