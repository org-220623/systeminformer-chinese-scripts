from enum import Enum

# ----------------------------------------------------------------------------------
# 定义类型常量
data_list_type = dict[str, str]
raw_data_list_type = list[tuple[str, str]]
TranslationDataType = list[tuple[str, str, data_list_type, raw_data_list_type]]
# ----------------------------------------------------------------------------------
# 定义枚举类
class TranslateDotNetCounters(Enum):
    NotTranslate = 0
    AddHeader = 1
    FullTranslate = 2
    PartialTranslate = 3
# ----------------------------------------------------------------------------------