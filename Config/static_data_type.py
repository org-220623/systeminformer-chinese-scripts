from enum import Enum

# ----------------------------------------------------------------------------------
# 定义类型常量
data_list_type = dict[str, str]
raw_data_list_type = list[tuple[str, str]]
TranslationDataType = list[tuple[str, str, data_list_type, raw_data_list_type]]
# ----------------------------------------------------------------------------------
# 定义枚举类
class EnumTranslateDotNetCounters(Enum):
    # 定义“特殊格式计数器”为名称包含 # 和 % 的计数器，“非特殊格式计数器”为名称不包含 # 和 % 的计数器，则：
    NotTranslate = 0                    # 完全不翻译
    AddHeader = 1                       # 只对所有计数器添加 "计数器: " 头部
    FullTranslate = 2                   # 翻译所有计数器（可能会丢失信息）
    PartialTranslate = 3                # 只翻译非特殊格式计数器（对特殊格式计数器不做任何处理）
    PartialTranslateAddHeader = 4       # 只翻译非特殊格式计数器（对特殊格式计数器添加 "计数器: " 头部）

class EnumTranslateMalwareScanningWebsite(Enum):
    # 处理恶意软件扫描网站
    NotTranslate = 0
    ToServiceName = 1

class EnumTranslateMandatoryLevel(Enum):
    # 处理强制完整性级别
    NotTranslate = 0
    DynamicSubViewTranslate = 1
# ----------------------------------------------------------------------------------