def pre_format_string(string: str):
    """
    字符串的预格式化，仅格式化双引号。
    因为 rc 文件中的字符串允许直接包含双引号（"）而无需进行格式化（\"），故提供此函数。
    :param string: 原字符串
    :return: 预格式化后的字符串
    """
    return string.replace("\"", "\\\"")

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