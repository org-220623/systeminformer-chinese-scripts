# 本文件存储 System Informer 源码汉化数据。
# 作者：anonymous9075 (anonymous9075331734@proton.me)

from misc import pre_format_string
from config import (
    CONST_PATH_PEVIEW_TOOL_SRC,
    CONST_PATH_SETUP_TOOL_SRC,
    CONST_PATH_SYSTEM_INFORMER_SRC,
)

# 定义类型常量
data_list_type = dict[str, str]
raw_data_list_type = list[tuple[str, str]]

###############################################################################
# 主数据开始
###############################################################################

# SHOULD_NOT_TRANSLATE_STRING_LIST 列表包含窗口控件信息、字体信息等不应翻译的内容，
# 即使窗口控件显示的文字或字符串表的其中一项恰好是这些内容，也不应被翻译。
SHOULD_NOT_TRANSLATE_STRING_LIST = [
    "Button",
    "SysListView32",
    "SysTreeView32",
    "PhTreeNew",
    "MS Shell Dlg",     # Default font name
    "SysLink", 
    "PhColorBox", 
    "PhGraph", 
    "PhHexEdit",
    "Segoe UI",         # Font name
    "taskschd.dll",     # {CONST_PATH_SYSTEM_INFORMER_SRC}/admintask.c
    # -------------------------------------------------------------------
    # Windows Kernel Object Types, from WinObjEx64 -> \ObjectTypes\*
    "ActivationObject",
    "ActivityReference",
    "Adapter",
    "ALPC Port",
    "Callback",
    "Composition",
    "Controller",
    "CoreMessaging",
    "CoverageSampler",
    "DebugObject",
    "Desktop",
    "Device",
    "Directory",
    "DmaAdapter",
    "Driver",
    "DxgkCompositionObject",
    "DxgkCurrentDxgThreadObject",
    "DxgkDisplayManagerObject",
    "DxgkSharedBundleObject",
    "DxgkSharedKeyedMutexObject",
    "DxgkSharedProtectedSessionObject",
    "DxgkSharedResource",
    "DxgkSharedSwapChainObject",
    "DxgkSharedSyncObject",
    "EnergyTracker",
    "EtwConsumer",
    "EtwRegistration",
    "EtwSessionDemuxEntry",
    "Event",
    "File",
    "FilterCommunicationPort",
    "FilterConnectionPort",
    "IoCompletion",
    "IoCompletionReserve",
    "IRTimer",
    "Job",
    "Key",
    "KeyedEvent",
    "Mutant",
    "NdisCmState",
    "Partition",
    "PcwObject",
    "PowerRequest",
    "Process",
    "Profile",
    "PsSiloContextNonPaged",
    "PsSiloContextPaged",
    "RawInputManager",
    "RegistryTransaction",
    "Section",
    "Semaphore",
    "Session",
    "SymbolicLink",
    "Thread",
    "Timer",
    "TmEn",
    "TmRm",
    "TmTm",
    "TmTx",
    "Token",
    "TpWorkerFactory",
    "Type",
    "UserApcReserve",
    "VRegConfigurationContext",
    "WaitCompletionPacket",
    "WindowStation",
    "WmiGuid",
    # Kernel Objects End
]

TRANSLATION_DATA: list[tuple[str,      str,  data_list_type,   raw_data_list_type]] = [
    # meanings:               |         |          |                   |
    #                     file path; encoding; data dict; data without quotes & formatting
    #################################################################################
    # System Informer source files: CONST_PATH_SYSTEM_INFORMER_SRC
    # Status: Processing
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/SystemInformer.rc", "utf-8", {     # File complete.
        "Terminate": "终止",
        "General": "常规",
        "Permissions": "权限",
        "Version:": "版本:",
        "Image file name (Win32):": "映像文件名 (Win32):",
        "Inspect": "检查",
        "Open": "打开",
        "Command line:": "命令行:",
        "Current directory:": "工作目录:",
        "Started:": "开始于:",
        "Parent console:": "父控制台:",
        "Parent process:": "父进程:",
        "View": "查看",
        "Mitigation policies:": "缓解策略:",
        "Details": "详情",
        "Protection:": "保护:",
        "<a>Company name link</a>": "<a>发行商名称链接</a>",
        "Image type:": "映像类型:",
        "Image file name:": "映像文件名:",
        "Policy": "策略",
        "Modules": "模块",
        "Options": "选项",
        "Threads": "线程",
        "Handles": "句柄",
        "Environment": "环境",
        "Refresh": "刷新",
        "Thread Stack": "线程栈",
        "Copy": "复制",
        "Close": "关闭",
        "About": "关于",
        "Copyright (c) Winsider Seminars && Solutions, Inc.":
            "版权所有 (c) Winsider Seminars && Solutions, Inc.",
        "<a href=\"\"https://systeminformer.sourceforge.io\"\">System Informer on SourceForge.net</a>":
            "<a href=\"\"https://systeminformer.sourceforge.io\"\">SourceForge 上的 System Informer</a>",
        "Diagnostics": "统计信息",
        "OK": "确定",
        "&Start": "启动(&S)",
        "&Pause": "挂起(&S)",
        "Type:": "类型:",
        "Start type:": "启动类型:",
        "Error control:": "错误控制:",
        "Group:": "组:",
        "Binary path:": "映像路径:",
        "Browse...": "选择...",
        "User account:": "用户账户:",
        "Password:": "密码:",
        "Service DLL:": "服务 DLL:",
        "Delayed start": "延迟启动",
        "Information": "信息",
        "Save...": "保存...",
        "Find Handles or DLLs": "查找句柄或 DLL",
        "Find": "查找",
        "Thread Stacks": "线程栈",
        "Users List": "用户列表",
        "User:": "用户:",
        "User SID:": "用户 SID:",
        "Session:": "会话:",
        "Unknown": "未知",
        "Elevated:": "提升:",
        "Virtualized:": "虚拟化:",
        "Integrity": "完整性",
        "Advanced": "高级",
        "Default token": "默认令牌",
        "Zombie Processes": "僵尸进程",
        "Processes highlighted red are hidden while those highlighted grey have terminated.":
            "红色高亮的进程已被隐藏，灰色高亮的进程已终止。",
        "&Scan": "扫描",
        "Run As": "以指定用户身份运行",
        "Enter the command to start as the specified user.": "输入命令以指定用户身份运行。",
        "Program:": "程序:",
        "User name:": "用户名:",
        "Toggle elevation": "更改海拔高度",
        "Session ID:": "会话 ID:",
        "Desktop:": "桌面:",
        "Cancel": "取消",
        "Browse": "选择",
        "Create suspended": "创建并挂起",
        "Create UIAccess": "创建 UIAccess",
        "Please wait...": "请稍等...",
        "Progress": "正在进行",
        "Pagefiles": "页面文件",
        "Owner:": "所有者:",
        "Primary group:": "主组:",
        "Virtualization:": "虚拟化:",
        "Linked token": "关联的令牌:",
        "Source": "源",
        "Name:": "名称:",
        "Processes in job:": "作业中的进程:",
        "Add...": "添加...",
        "Limits:": "限制:",
        "Signaled:": "有信号:",
        "Set": "设置",
        "Reset": "重置",
        "Pulse": "脉冲",
        "Count:": "计数:", 
        "Abandoned:": "已弃用:",
        "Current count:": "当前值:", 
        "Maximum count:": "最大值:", 
        "Acquire": "获取", 
        "Release": "释放",
        "Statistics": "统计数据", 
        "Active processes": "活动进程数", 
        "Total processes": "进程总数", 
        "Terminated due to job limits": "因作业限制已终止", 
        "Time": "时间", 
        "User time": "用户时间", 
        "Kernel time": "内核时间", 
        "User time (period)": "用户时间 (周期)", 
        "Kernel time (period)": "内核时间 (周期)", 
        "Memory": "内存", 
        "Page faults": "页面错误", 
        "Peak process usage": "进程使用量峰值", 
        "Peak job usage": "作业使用量峰值", 
        "Reads": "读取", 
        "Read bytes": "读取字节", 
        "Writes": "写入", 
        "Write bytes": "写入字节", 
        "Other": "其他", 
        "Other bytes": "其他字节", 
        "Event Pair": "事件配对", 
        "Set low": "设置低值", 
        "Set high": "设置高值", 
        "Affinity": "处理器相关性", 
        "Affinity controls which CPUs threads are allowed to execute on.": "处理器相关性控制线程可以在哪些 CPU 上执行。", 
        "Select all": "全选", 
        "Deselect all": "全不选", 
        "System Information": "系统信息", 
        "Message": "消息", 
        "Title:": "标题:", 
        "Text:": "文字:", 
        "Icon:": "图标:", 
        "Timeout (s):": "超时 (秒):", 
        "Session Properties": "会话属性", 
        "Option": "选项", 
        "Search engine:": "搜索引擎:", 
        "PE viewer:": "PE 查看器:", 
        "Max. size unit:": "最大大小单元:", 
        "Icon processes:": "图标处理:", 
        "Font...": "字体...", 
        "Monospace...": "等宽字体...", 
        "Make default...": "设置默认值...", 
        "Graph history length:": "图像历史长度:", 
        "Automatic": "自动", 
        "Application font:": "应用程序字体:", 
        "System Informer is the default Task Manager:": "System Informer 是默认的任务管理器:", 
        "Symbol path:": "符号路径:", 
        "Highlighting": "高亮显示", 
        "New objects:": "新对象:", 
        "New objects": "新对象", 
        "Removed objects:": "已删除对象:", 
        "Removed objects": "已删除对象", 
        "Highlighting duration:": "高亮显示时长:", 
        "Double-click an item to change it.": "双击项目以更改。", 
        "Enable all": "全部启用", 
        "Disable all": "全部禁用", 
        "Choose Columns": "选择列", 
        "Inactive columns:": "未显示的列:", 
        "Show >": "显示 >", 
        "< Hide": "< 隐藏", 
        "Move up": "上移", 
        "Move down": "下移", 
        "Active columns:": "显示的列:", 
        "Select the columns that will appear in the list.": "选择要在列表中显示的列。", 
        "Network Stack": "网络栈", 
        "Create Service": "创建服务", 
        "Display name:": "显示名称:", 
        "Performance": "性能", 
        "Private bytes": "私有字节", 
        "GDI Handles": "GDI 句柄", 
        "Log": "日志", 
        "Clear": "清空", 
        "Auto-scroll": "自动滚动", 
        "Re-read": "重新读取", 
        "Write": "写入", 
        "Go to...": "转到...", 
        "Memory Protection": "内存保护", 
        "New value:": "新值:", 
        "Strings": "字符串", 
        "Filter": "筛选器", 
        "String Search": "搜索字符串", 
        "Minimum length:": "最小长度:", 
        "Results": "结果", 
        "Results.": "结果", 
        "Detect Unicode": "检测 Unicode", 
        "Search in the following types of memory regions:": "在以下类型的内存区域中进行搜索:", 
        "Private": "私有", 
        "Image": "映像", 
        "Mapped": "映射", 
        "Extended Unicode": "扩展 Unicode", 
        "Graphs": "图像", 
        "Show text": "显示文字", 
        "Use old colors (black background)": "使用旧颜色 (黑色背景)", 
        "Show commit charge instead of physical memory in summary view":
            "在摘要视图中显示提交用量而不是物理内存", 
        "Plugins": "插件", 
        "Changes may require a restart to take effect.": "更改可能需要重启才能生效。", 
        "Disabled plugins (0)": "已禁用插件 (0)", 
        "Handle Statistics": "句柄统计数据", 
        "Handle": "句柄",
        "Process Record": "进程记录", 
        "Parent:": "父进程:", 
        "Terminated:": "结束于:", 
        "Properties": "属性", 
        "Select a Process": "选择进程", 
        "Select a process from the list below.": "从下面的列表中选择一个进程。", 
        "Services": "服务", 
        "Remote Control": "远程控制", 
        "To end the remote control session, press this key and the modifiers selected below:":
            "要结束远程控制会话，请按此键以及下面选择的组合键:", 
        "Capabilities": "兼容性", 
        "Attributes": "属性", 
        "CPU name": "CPU 名称", 
        "Panel layout": "面板布局", 
        "Graph layout": "图像布局", 
        "Utilization:": "使用率:", 
        "Speed:": "速度:", 
        "System": "系统", 
        "Processes": "进程", 
        "Uptime": "运行时间", 
        "&Show one graph per CPU": "每个 CPU 显示一个图表(&S)", 
        "Context switches delta": "上下文切换增量", 
        "Interrupts delta": "中断增量", 
        "DPCs delta": "DPC 增量", 
        "System calls delta": "系统调用增量", 
        "Topology": "拓扑结构", 
        "Cores": "核心", 
        "Sockets": "套接字", 
        "Logical processors": "逻辑处理器", 
        "Latency": "延迟", 
        "Hardware": "硬件", 
        "L1 cache": "L1 缓存", 
        "L2 cache": "L2 缓存", 
        "L3 cache": "L3 缓存",
        "Commit charge": "提交用量",
        "Current": "当前",
        "Peak": "峰值",
        "Limit": "限制",
        "Physical memory": "物理内存",
        "Cache WS": "缓存工作集",
        "Total": "总计",
        "Kernel WS": "内核工作集",
        "Driver WS": "驱动工作集",
        "Paged pool": "分页池",
        "Working set": "工作集",
        "Virtual size": "虚拟内存大小",
        "Allocs delta": "分配增量",
        "Frees delta": "释放增量",
        "Non-paged pool": "非分页池",
        "Usage": "用量",
        "Memory lists": "内存列表",
        "Zeroed": "零化",
        "Modified": "已修改",
        "Free": "空闲",
        "Modified no-write": "已修改不写出",
        "Standby": "待命",
        "Priority 0": "优先级 0",
        "Priority 1": "优先级 1",
        "Priority 2": "优先级 2",
        "Priority 3": "优先级 3",
        "Priority 4": "优先级 4",
        "Priority 5": "优先级 5",
        "Priority 6": "优先级 6",
        "Priority 7": "优先级 7",
        "Paging": "分页",
        "Page faults delta": "页面错误增量",
        "Pagefile writes delta": "页面文件写入增量",
        "Page reads delta": "页面读取增量",
        "Mapped writes delta": "映射写入增量",
        "Modified pagefile": "已修改页面文件",
        "&More": "更多",
        "Reserved": "保留",
        "Mapped IO": "映射 I/O",
        "Mapped reads": "映射读取",
        "Mapped writes": "映射写入",
        "&Empty": "清空",
        "Slots used": "已使用槽",
        "Form factor": "形态因数",
        "Technology": "技术",
        "Memory type": "内存类型",
        "Speed": "速度",
        "Total physical": "物理内存总计",
        "Commit charge:": "提交用量:",
        "Physical memory:": "物理内存:",
        "Read bytes:": "读取字节:",
        "Write bytes:": "写入字节:",
        "Other bytes:": "其他字节:",
        "I/O deltas": "I/O 增量",
        "Reads delta": "读取增量",
        "Read bytes delta": "读取字节增量",
        "Writes delta": "写入增量",
        "Write bytes delta": "写入字节增量",
        "Other delta": "其他增量",
        "Other bytes delta": "其他字节增量",
        "I/O totals": "I/O 总计",
        "Memory Lists": "内存列表",
        "Bad": "损坏",
        "(Repurposed)": "(已重用)",
        "Content layout": "内容布局",
        "Pin": "固定",
        "Mitigation Policies": "缓解策略",
        "Description:": "描述:",
        "Edit Environment Variable": "编辑环境变量",
        "Value:": "值:",
        "Apply": "应用",
        "Cleanup": "清空",
        "Plugin Properties": "插件属性",
        "Plugin": "插件",
        "Internal name:": "内部名称:",
        "Author:": "作者:",
        "<a>Open</a>": "<a>打开</a>",
        "File name:": "文件名:",
        "Options...": "选项...",
        "Disabled Plugins": "已禁用的插件",
        "Organize Column Sets": "组织列集",
        "Rename": "重命名",
        "Delete": "删除",
        "Run": "运行",
        "&Open:": "打开:",
        "Type the name of a program, folder, document, or Internet resource, and Windows will open it for you.":
            "输入程序、文件夹、文档或互联网资源的名称，Windows 将为您打开它。",
        "&Browse...": "选择...",
        "Create this task with TrustedInstaller privileges.": "以 TrustedInstaller 权限创建此任务",
        "Create this task with Administrative privileges.": "以 Administrators 权限创建此任务",
        "Process dump": "进程转储",
        "Normal": "正常",
        "With data segments": "包含数据段",
        "With full memory": "包含全部内存",
        "With handle data": "包含句柄数据",
        "Filter memory": "筛选内存",
        "Scan memory": "扫描内存",
        "With unloaded modules": "包含未加载模块",
        "With indirectly referenced memory": "包含间接引用内存",
        "Filter module paths": "筛选模块路径",
        "With process and thread data": "包含进程和线程数据",
        "With private read-write memory": "包含私有可读写内存",
        "Without optional data": "排除可选数据",
        "With full memory info": "包含全部内存信息",
        "With thread info": "包含线程数据",
        "With code segments": "包含代码段",
        "Without auxiliary state": "排除次要状态",
        "With full auxiliary state": "包含全部次要状态",
        "With private write-copy memory": "包含私有写时复制内存",
        "Ignore inaccessible memory": "忽略无法访问的内存",
        "With token information": "包含令牌信息",
        "With module headers": "包含模块头部",
        "With filter triage data": "包含筛选分流数据",
        "With AVX state context registers": "包含 AVX 状态上下文寄存器",
        "With Intel processor trace data": "包含 Intel 处理器跟踪数据",
        "Scan inaccessible partial pages": "扫描部分无法访问的页面",
        "Filter write-combined memory": "筛选写合并内存",
        "Save": "保存",
        "Live kernel dump": "活动内核转储",
        "Use dump storage stack": "使用转储文件存储栈",
        "Compress memory pages": "压缩内存页面",
        "Capture user pages": "捕获用户页面",
        "Capture Hypervisor pages": "捕获虚拟机监控程序页面",
        "Include nonessential Hypervisor pages": "包含非必要虚拟机监控程序页面",
        "Only kernel thread stacks": "仅包含内核线程栈",
        "Heaps": "堆",
        "Sizes in bytes": "字节大小",
        "Select a package": "选择应用包",
        "Select the identity for access to the package file system and registry.":
            "选择用于访问软件包文件系统和注册表的身份。",
        "Enter the command to start as the specified package.":
            "输入要以指定软件包身份启动的命令。",
        "Mappings": "映射",
        "Modified pages": "已修改页面",
        "Status": "状态",
        "&Ok": "确定(&O)",
        "Input Prompt": "输入提示",
        "Socket": "套接字",
        "Add": "添加",
        "Remove": "移除",
        "Auditing": "审核",
    },
                                                                            [
        ('CAPTION "Job"', 'CAPTION "作业"'),
        ('"File",IDC_FILE', '"文件",IDC_FILE'),
        ('"Process",IDC_PROCESS', '"进程",IDC_PROCESS'),
        ('CAPTION "Token"', 'CAPTION "令牌"'),
        ('"Token",IDC_STATIC', '"令牌",IDC_STATIC'),
        ('CAPTION "Event"', 'CAPTION "事件"'),
        ('CAPTION "Mutant"', 'CAPTION "互斥体"'),
        ('CAPTION "Semaphore"', 'CAPTION "信号量"'),
        ('CAPTION "Timer"', 'CAPTION "计时器"'),
        ('"Section",IDC_SECTION', '"节区",IDC_SECTION'),
    ]),
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/version.rc", "utf-8-sig", {
        "Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved.":
                # xref: "{CONST_PATH_SETUP_TOOL_SRC}/version.rc" down
            "版权所有 (c) Winsider Seminars & Solutions, Inc. 保留所有权利。"
    }, []), # UTF-8-BOM
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
            'config.pszMainInstruction = PhaConcatStrings(3, L"Do you want to ", action->Buffer, L"?")->Buffer',
            'config.pszMainInstruction = PhaConcatStrings(3, L"你想要", action->Buffer, L"吗?")->Buffer'
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
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/dbgcon.c", "utf-8", {
        "\tCount: %u": "\t计数: %u",
        "Type: %s\n": "类型: %s\n",
        "Reference count: %ld\n": "引用计数: %ld\n",
        "Flags: %x\n": "标志: %x\n",
        "Name: %s\n": "名称: %s\n",
        "Number of objects: %lu\n": "对象数量: %lu\n",
        "Flags: %u\n": "标志: %u\n",
        "Type index: %u\n": "类型索引: %u\n",
        "Free list count: %lu\n": "空闲列表计数: %lu\n",
        "Error.\n": "错误。\n",
        "Count: %u\n": "计数: %u\n",
        "Allocated buckets: %u\n": "已分配桶: %u\n",    # Windows 低碎片堆？
        "Allocated entries: %u\n": "已分配条目: %u\n",
        "Next free entry: %d\n": "下一个空闲条目: %d\n",
        "Next usable entry: %d\n": "下一个可用条目: %d\n",
        "Equal function: %s\n": "等价函数: %s\n",
        "Hash function: %s\n": "哈希函数: %s\n",
        "\nBuckets:\n": "\n桶:\n",
        "\nExpected lookup misses: %lu\n": "\n预期查找未命中: %lu\n",
        "Leak at 0x%Ix (%Iu bytes). Stack trace:\n": "泄漏发生在 0x%Ix (%Iu 字节)，堆栈跟踪:\n",
        "[fail]: writers active in read zone!\n": "[失败]：读取区域中有处于活动状态的写入区域!\n",  # todo
        "[fail]: readers active in write zone!\n": "[失败]：写入区域中有处于活动状态的读取区域!\n", # todo
        "[null] %s: %ums\n": "[空] %s: %ums\n", # and line 586: L"[strs] %s: %ums\n"
        pre_format_string("Press Ctrl+C or type \"exit\" to close the debug console. "
                          "Type \"help\" for a list of commands.\n"):
            pre_format_string("按 Ctrl+C 或输入 \"exit\" 关闭调试控制台。输入 \"help\" 查看命令列表。\n"),
        "This command is not available on non-debug builds.\n": "此命令在非调试版本中不可用。\n",
        "Commands:\n": "可用的命令:\n",
        "Referencing: %ums\n": "正在引用: %ums\n",
        "Critical section: %ums\n": "关键节区: %ums\n",
        "Fast lock: %ums\n": "快速锁: %ums\n",
        "Queued lock: %ums\n": "队列锁: %ums\n",
        "Object small free list count: %u\n": "对象小型空闲列表计数:%u\n",
        "Statistics:\n": "统计数据:\n",
        "Total number: %lu\n": "总计: %lu\n",
        "Total overhead (header): %s\n": "总开销 (header): %s\n",
        "Missing object address.\n": "丢失对象地址。\n",
        "Error: %s\n": "错误: %s\n",
        "Invalid object address.\n": "对象地址无效。\n",
        "No snapshot.\n": "无快照。\n",
        "Static count: %u\n": "静态计数: %u\n",
        "Dynamic count: %u\n": "动态计数: %u\n",
        "Dynamic allocated: %u\n": "动态分配: %u\n",
        "Static objects:\n": "静态对象:\n",
        "Dynamic objects:\n": "动态对象:\n",
        "Thread %u\n": "线程 %u\n",
        "\tStart Address: %s\n": "\t起始地址: %s\n",
        "\tParameter: %Ix\n": "\t参数: %Ix\n",
        "\tCurrent auto-pool: %Ix\n": "\t当前 auto-pool: %Ix\n",
        "Thread not running\n": "线程未运行\n",
        "\tProvider registration at %Ix\n": "\t服务提供商注册 %Ix\n",
        "\t\tEnabled: %s\n": "\t\t已启用: %s\n",
        "Yes": "是",
        "No": "否",
        "\t\tFunction: %s\n": "\t\t函数: %s\n",
        "\t\tObject:\n": "\t\t对象:\n",
        "Work queue at %s\n": "工作队列 %s\n",
        "Maximum threads: %lu\n": "最大线程数: %lu\n",
        "Minimum threads: %lu\n": "最小线程数: %lu\n",
        "No work timeout: %lu\n": "无工作超时: %lu\n",
        "Current threads: %lu\n": "当前线程: %lu\n",
        "Busy count: %lu\n": "忙碌计数: %lu\n",
        "\tWork queue item at %Ix\n": "\t工作队列项 %Ix\n",
        "\t\tContext: %Ix\n": "\t\t上下文: %Ix\n",
        "Records for %s %s:\n": "%s %s 的记录:\n",
        "\tRecord at %Ix: %s (%lu) (refs: %ld)\n": "\t记录 %Ix: %s (%lu) (引用: %ld)\n",
        "Process item at %Ix: %s (%u)\n": "进程项 %Ix: %s (%u)\n",
        "\tRecord at %Ix\n": "\t记录 %Ix\n",
        "\tQuery handle %Ix\n": "\t队列句柄 %Ix\n",
        "\tFile name at %Ix: %s\n": "\t文件名 %Ix: %s\n",
        "\tCommand line at %Ix: %s\n": "\t命令行 %Ix: %s\n",
        "\tFlags: %u\n": "\t标志: %u\n",
        "\nTotal unique strings: %u\n": "\n唯一字符串总计: %u\n",
        "Unable to initialize heap debugging. Make sure that you are using Windows 7 or above.":
            "无法初始化堆调试。请确保您使用的是 Windows 7 或更高版本。",
        "Warning: user-mode stack trace database is not enabled. Stack traces will not be displayed.\n":
            "警告：用户模式堆栈跟踪数据库未启用。堆栈跟踪将不会显示。\n",
        "\nNumber of leaks: %lu (%lu displayed)\n": "\n泄漏数量: %lu (%lu 已显示)\n",
        "Number of bytes must be 256 or smaller.\n": "字节数必须小于或等于 256。\n",
        "Error reading address near %Ix.\n": "读取地址 %Ix 附近时出错。\n",
        "Usage: mem address [numberOfBytes]\n": "语法: mem address [numberOfBytes]\n",
        "Example: mem 12345678 16\n": "示例: mem 12345678 16\n",
        "Unrecognized command.\n": "无法识别的命令。\n",
    }, []),
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
            "Received config": "已接收配置",
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
        "Mapped file": "已映射文件",
        "Mapped image": "已映射映像",
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
    #################################################################################
    # System Informer PEView Tool source files: CONST_PATH_PEVIEW_TOOL_SRC
    # Status: Pending
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/peview.rc", "utf-8", {
        "Properties": "属性",
        "Close": "关闭",
        "Options": "选项",
        "Permissions": "权限",
        "General": "常规",
        "Version:": "版本:",
        "<a>Company Name Link</a>": "<a>发行商名称链接</a>",
        "Imports": "导入",
        "Exports": "导出",
        "Runtime version:": "运行时版本:",
        "Flags:": "标志:",
        "Sections:": "节区:",
        "PublicKeyToken:": "公共密钥令牌:",
        "Target version:": "目标版本:",
        "Entry point:": "入口点:",
        "Load config": "加载配置",
        "Symbols": "符号",
        "Resources": "资源",
        "Strings": "字符串",
        "String Search": "搜索字符串",
        "Minimum length:": "最小长度:",
        "OK": "确定",
        "Cancel": "取消",
        "Target machine:": "目标平台:",
        "Image base:": "映像基址:",
        "Image type:": "映像类型:",
        "Attributes": "详细信息",           # "Attributes" 与 "Properties" 在语义上重复，故修改翻译。
        "Streams": "流",
        "Links": "链接",
        "Pids": "PID",
        "Dynamic": "动态",
        "Tls": "TLS",
        "Max. size unit:": "最大大小单元:",
        "Font...": "字体...",
        "Application font:": "应用程序字体:",
        "Symbol path:": "符号路径:",
        "Reset": "重置",
        "Cleanup": "清空",
        "Preview": "预览",
        "Directories": "文件夹",
        "ProdID": "产品 ID",             # todo: 查明此条目的含义
        "Checksum:": "校验和:",
        "Hash (raw):": "哈希值 (二进制):",
        "Hash:": "哈希值:",
        "Production ID": "产品 ID",
        "Debug": "调试",
        "Sections": "节区",
        "Refresh": "刷新",
        "EH Continuation":          # See: https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdynamicehcontinuationtargets
                                    #      https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-process_dynamic_eh_continuation_target
            "异常处理延续",
        "Layout": "布局",
        "Hashes": "哈希",
        "Exceptions": "异常",
        "Relocations": "重定位",
        "Choose Columns": "选择列",
        "Inactive columns:": "未显示的列:",
        "Show >": "显示 >",
        "< Hide": "< 隐藏",
        "Move up": "上移",
        "Move down": "下移",
        "Active columns:": "显示的列:",
        "Select the columns that will appear in the list.": "选择要在列表中显示的列。",
        "Headers": "头部",
        "CLR Imports": "CLR 导入项",
        "Volatile Metadata": "易失性元数据",
        "CLR Tables": "CLR 表",
    },
                                                                [
        ('"File",IDC_FILE', '"文件",IDC_FILE'),
    ]),
    #################################################################################
    # Install & update & uninstall tool: CONST_PATH_SETUP_TOOL_SRC
    # Status: Completed
    (f"{CONST_PATH_SETUP_TOOL_SRC}/extract.c", "utf-8", {
        "Extracting: ": "正在复制: ",
        "Progress: ": "进度: ",
        " of ": "，总计: "
    }, []),
    (f"{CONST_PATH_SETUP_TOOL_SRC}/main.c", "utf-8", {
        # config.pszContent = (
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