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
        # 134
    }, []),
]