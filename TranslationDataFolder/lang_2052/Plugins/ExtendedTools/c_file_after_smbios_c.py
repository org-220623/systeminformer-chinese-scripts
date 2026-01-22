from Config.const_values import CONST_PATH_PLUGIN_EXTENDEDTOOLS, CONST_STRING_NOT_TRANSLATE_PREFIX
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_EXTENDEDTOOLS}/thrdact.c", "utf-8", {
        "end": "终止",
        "I/O for the selected thread": "所选线程的 I/O",
        "There is no synchronous I/O to cancel.": "没有需要取消的同步 I/O。",
        "Unable to cancel synchronous I/O": "无法取消同步 I/O",
    }, []),
    (f"{CONST_PATH_PLUGIN_EXTENDEDTOOLS}/tpm.c", "utf-8", {
        "Platform write": "平台写入",
        "Owner write": "所有者写入",
        "Auth write": "认证写入",
        "Policy write": "策略写入",
        "Counter": "计数器",
        "Bits": "位",
        "Extend": "扩展",
        # Line 27
    }, []),
]