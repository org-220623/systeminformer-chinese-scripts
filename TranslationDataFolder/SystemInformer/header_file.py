from Config.const_values import CONST_PATH_SYSTEM_INFORMER_INC
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_SYSTEM_INFORMER_INC}/ksisup.h", "utf-8", {
        "Kernel driver not connected": "内核驱动程序未连接",
    }, [
        ('''L"System Informer is not connected to the kernel driver or lacks the required state "
        L"necessary for this feature. Make sure that the \\\"Enable kernel-mode driver\\\" option is "
        L"enabled and that System Informer is running with administrator privileges."''',
         'L"System Informer 未连接到内核驱动程序，或缺少此功能所需的必要状态。请确保已启用“启用内核模式驱动程序”选项'
         '，并且 System Informer 以管理员权限运行。"'),
    ]),
]