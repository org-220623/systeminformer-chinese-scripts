# 本文件存储 System Informer 源码汉化数据。
# 作者：anonymous9075 (anonymous9075331734@proton.me)

from misc import pre_format_string

# 定义类型类
class RawDataDictEntryType:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new

# 定义类型常量
data_list_type = dict[str, str]
raw_data_list_type = list[tuple[str, str]]

# 定义目录路径常量 (CONST_PATH_*)
CONST_PATH_SYSTEM_INFORMER_SRC = "SystemInformer"
CONST_PATH_PEVIEW_TOOL_SRC = "tools/peview"

# 当开启调试模式时，将只处理 debug_file 变量指定的文件。
debug_file = f"{CONST_PATH_SYSTEM_INFORMER_SRC}/actions.c"

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
]

TRANSLATION_DATA: list[tuple[str,      str,  data_list_type, raw_data_list_type]] = [
    # meanings:               |         |          |
    #                   [(file_path, encoding, data_dict), ...]
    #################################################################################
    # System Informer source files
    # (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/{FILE_NAME}", ENCODING, {...}), ...
    (f"{CONST_PATH_SYSTEM_INFORMER_SRC}/SystemInformer.rc", "utf-8", {     # File complete.
        "Terminate": "终止",
        "General": "常规",
        "Permissions": "权限",
        "File": "文件",
        "Version:": "版本:",
        "Image file name (Win32):": "映像文件名 (Win32):",
        "Inspect": "检查",
        "Open": "打开",
        "Process": "进程",
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
        "Token": "令牌",
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
        "Job": "作业",
        "Processes in job:": "作业中的进程:",
        "Add...": "添加...",
        "Limits:": "限制:",
        "Event": "事件",
        "Signaled:": "有信号:",
        "Set": "设置",
        "Reset": "重置",
        "Pulse": "脉冲",
        "Mutant": "互斥体", 
        "Count:": "计数:", 
        "Abandoned:": "已弃用:", 
        "Semaphore": "信号量", 
        "Current count:": "当前值:", 
        "Maximum count:": "最大值:", 
        "Acquire": "获取", 
        "Release": "释放", 
        "Timer": "计时器", 
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
        "Section": "节区",
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
        "&Ok": "确定",
        "Input Prompt": "输入提示",
        "Socket": "套接字",
        "Add": "添加",
        "Remove": "移除",
        "Auditing": "审核",
    }, []),
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

        # line 5670
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
    #################################################################################
    # System Informer PEView Tool source files
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/peview.rc", "utf-8", {
        "Properties": "属性",
        "Close": "关闭",
        "Options": "选项",
        "Permissions": "权限",
        "General": "常规",
        "File": "文件",
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
    }, []),
]