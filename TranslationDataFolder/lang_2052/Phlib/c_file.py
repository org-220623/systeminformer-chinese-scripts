from Config.const_values import CONST_PATH_PHLIB_SRC
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PHLIB_SRC}/util.c", "utf-8", {
        "Cancel": "取消",
        "Do you want to ": "你确定要",
        " Are you sure you want to continue?": " 你确定要继续吗?",
        "Are you sure you want to %s?": "你确定要 %s 吗?",
        "Unable to perform the operation.": "无法执行操作。",
    }, []),
]