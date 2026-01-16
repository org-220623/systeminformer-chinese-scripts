from Config.const_values import CONST_PATH_PEVIEW_TOOL_SRC
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/attributes.c", "utf-8", {
        "Name": "名称",
        "Value": "值",
        "Delete": "删除",
        "&Copy": "复制(&C)",
        "Unable to remove attribute.": "无法移除属性。",
    }, []),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/cfgprp.c", "utf-8", {
        # todo 53 56 59
        "(unnamed)": "(未命名)",
        # todo 125 127 129
        "Name": "名称",
        "Flags": "标志",
        "XFG Hash": "XFG 哈希",
    }, [
        ('PhAddListViewColumn(context->ListViewHandle, 2, 2, 2, LVCFMT_LEFT, 50, L"Type"',
         'PhAddListViewColumn(context->ListViewHandle, 2, 2, 2, LVCFMT_LEFT, 50, L"类型"'),
    ]),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/chcol.c", "utf-8", {
        "Inactive columns...": "未显示的列...",
        "Active columns...": "已显示的列...",
    }, []),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/clrprp.c", "utf-8", {
        "IL only, ": "仅 IL, ",
        "32-bit only, ": "仅 32 位, ",
        "32-bit preferred, ": "首选 32 位, ",
        "IL library, ": "IL 库, ",
        "Strong-name signed, ": "强名称签名, ",
        "Strong-name delay signed, ": "强名延迟签署, ",
        "Native entry-point, ": "原生入口点, ",
        "Track debug data, ": "跟踪调试数据, ",
        "%s (%s) (deterministic)": "%s (%s) (确定的)",
        "Name": "名称",
        "RVA (start)": "RVA (起始)",
        "RVA (end)": "RVA (结束)",
        "Size": "大小",
        "Hash": "哈希",
    }, []),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/clrprptables.c", "utf-8", {
        "Name": "名称",
        "Count": "计数",
        "Size": "大小",
        "RVA (start)": "RVA (起始)",
        "RVA (end)": "RVA (结束)",
        "Hash": "哈希",
    }, []),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/clrtableimportprp.c", "utf-8", {
        "Name": "名称",
        "Flags": "标志",
    }, []),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/clrtableimports.cpp", "utf-8", {
        "No mangle, ": "无损坏, ",
        "Ansi charset, ": "ANSI 字符集, ",
        "Unicode charset, ": "Unicode 字符集, ",
        "Auto charset, ": "自动字符集, ",
        "Supports last error, ": "支持 LastError, ",
        "Winapi, ": "WINAPI, ",
        "Bestfit enabled, ": "Bestfit 已启用, ",
        "Bestfit disabled, ": "Bestfit 已禁用, ",
        "Bestfit assembly, ": "Bestfit 汇编, ",
        "ThrowOnUnmappableChar enabled, ": "ThrowOnUnmappableChar 已启用, ",
        "ThrowOnUnmappableChar disabled, ": "ThrowOnUnmappableChar 已禁用, ",
        "ThrowOnUnmappableChar assembly, ": "ThrowOnUnmappableChar 汇编, ",
        "Unknown": "未知",
    }, []),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/debugprp.c", "utf-8", {
        "Name": "名称",
        "Count": "计数",
        "Size": "大小",
        "RVA (start)": "RVA (起始)",
        "RVA (end)": "RVA (结束)",
        "Hash": "哈希",
    }, [
        ('PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 100, L"Type")',
         'PhAddListViewColumn(context->ListViewHandle, 1, 1, 1, LVCFMT_LEFT, 100, L"类型")'),
    ]),
    (f"{CONST_PATH_PEVIEW_TOOL_SRC}/delayhook.c", "utf-8", {
        "Unable to register window class.": "无法注册窗口类。",
        "Unable to commit detours transaction.": "无法提交绕行事务。",
    }, []),
]