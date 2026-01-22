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
        "Reserved type 1": "保留类型 1",
        "Reserved type 2": "保留类型 2",
        "Reserved type 4": "保留类型 4",
        "Policy delete": "策略删除",
        "Write locked": "写入锁定",
        "Write all": "写入全部",
        "Write define": "写入定义",
        "Write lockable": "写入可锁定",
        "Global lock": "全局锁",
        "Platform read": "平台读取",
        "Owner read": "所有者读取",
        "Auth read": "认证读取",
        "Policy read": "策略读取",
        "Reserved flag 1": "保留标志 1",
        "Reserved flag 2": "保留标志 2",
        "Reserved flag 3": "保留标志 3",
        "Reserved flag 4": "保留标志 4",
        "Reserved flag 5": "保留标志 5",
        # Line 45
    }, []),
]