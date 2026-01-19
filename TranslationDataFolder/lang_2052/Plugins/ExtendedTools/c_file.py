from Config.const_values import CONST_PATH_PLUGIN_EXTENDEDTOOLS
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_EXTENDEDTOOLS}/disktab.c", "utf-8", {
        "Disk": "磁盘",
        "Search Disk": "搜索磁盘",
        "Disk monitoring requires System Informer to be restarted with administrative privileges.": "磁盘监控需要以管理员权限重启 System Informer。",
        "Unable to start the kernel event tracing session: ": "无法启动内核事件跟踪会话: ",
        "Name": "名称",
        "Read rate average": "平均读取速率",
        "Write rate average": "平均写入速率",
        "Total rate average": "平均总速率",
        "I/O priority": "I/O 优先级",
        "Response time (ms)": "响应时间 (ms)",
        "Original name": "原始名称",
    }, [
        ('PhAddTreeNewColumn(WindowHandle, ETDSTNC_FILE, TRUE, L"File"', 'PhAddTreeNewColumn(WindowHandle, ETDSTNC_FILE, TRUE, L"文件"'),
    ]),
]