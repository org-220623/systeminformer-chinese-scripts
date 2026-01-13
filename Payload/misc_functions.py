from Config.const_values import (
    CONST_STRING_LEFT_BRACKET,
    CONST_STRING_RIGHT_BRACKET,
    CONST_STRING_CRLF_NEWLINE,
)
from Config.static_data_type import TranslationDataType


def pre_format_string(string: str):
    """
    字符串的预格式化，仅格式化双引号。
    因为 rc 文件中的字符串允许直接包含双引号（"）而无需进行格式化（\"），故提供此函数。
    :param string: 原字符串
    :return: 预格式化后的字符串
    """
    return string.replace("\"", r"\"")

def format_string(string: str):
    """
    字符串格式化
    :param string: 原字符串
    :return: 格式化后的字符串
    """
    return ("\"" + string.replace("\n", "\\n")
            .replace("\t", "\\t")
            .replace("\r", "\\r")
            .replace("\0", "\\0")
            .replace("\b", "\\b") + "\"")

def check_symbols(old: str, new: str):
        """
        检查翻译条目并给出警告和建议
        :param old: 原字符串
        :param new: 新字符串
        :return: None
        """
        if old == "" or new == "":
            print("发现为空的翻译项。")
        if old[-1] == ":" and new[-1] != ":":
            print(f"\t新字符串末尾未使用英文冒号："
                  f"{CONST_STRING_LEFT_BRACKET}{old}{CONST_STRING_RIGHT_BRACKET}，"
                  f"{CONST_STRING_LEFT_BRACKET}{new}{CONST_STRING_RIGHT_BRACKET}")
        # {
        if old[-1] == "\n" and new [-1] != "\n":
            print(f"\t新字符串末尾未换行："
                  f"{CONST_STRING_LEFT_BRACKET}{old}{CONST_STRING_RIGHT_BRACKET}，"
                  f"{CONST_STRING_LEFT_BRACKET}{new}{CONST_STRING_RIGHT_BRACKET}")
        elif (old[:len(old) - len(CONST_STRING_CRLF_NEWLINE)] == CONST_STRING_CRLF_NEWLINE and
              new[:len(new) - len(CONST_STRING_CRLF_NEWLINE)] != CONST_STRING_CRLF_NEWLINE):
            print(f"\t新字符串末尾未使用 CR+LF 换行符："
                  f"{CONST_STRING_LEFT_BRACKET}{old}{CONST_STRING_RIGHT_BRACKET}，"
                  f"{CONST_STRING_LEFT_BRACKET}{new}{CONST_STRING_RIGHT_BRACKET}")
        # }
        if old[:len(old) - 3] == "..." and new[:len(new) - 3] != "...":
            print(f"\t新字符串末尾未使用英文省略号："
                  f"{CONST_STRING_LEFT_BRACKET}{old}{CONST_STRING_RIGHT_BRACKET}，"
                  f"{CONST_STRING_LEFT_BRACKET}{new}{CONST_STRING_RIGHT_BRACKET}")
        if "（" in new or "）" in new:
            print(f"\t新字符串包含中文圆括号："
                  f"{CONST_STRING_LEFT_BRACKET}{old}{CONST_STRING_RIGHT_BRACKET}，"
                  f"{CONST_STRING_LEFT_BRACKET}{new}{CONST_STRING_RIGHT_BRACKET}")

def get_translation_item_total_count(obj_in: TranslationDataType):
    result = 0
    for file_entry in obj_in:
        result += (len(file_entry[2].keys()) + len(file_entry[3]))
    print(result)