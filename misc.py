def pre_format_string(string: str):
    return string.replace("\"", "\\\"")

def format_string(string: str):
    return "\"" + string.replace("\n", "\\n") \
        .replace("\t", "\\t") \
        .replace("\r", "\\r") \
        .replace("\0", "\\0") + "\""