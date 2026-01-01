from data import data_list_type, SHOULD_NOT_TRANSLATE_STRING_LIST, raw_data_list_type
from misc import format_string

# 定义字符串常量 (CONST_STRING_*)
CONST_STRING_ELLIPSIS = "..."
CONST_STRING_COLON = ":"
CONST_STRING_LF_NEWLINE = "\n"
CONST_STRING_CRLF_NEWLINE = "\r\n"
CONST_STRING_LEFT_BRACKET = "[ "
CONST_STRING_RIGHT_BRACKET = " ]"

class TranslateFileObject:
    def __init__(self,
                 file_path: str,
                 encoding: str,
                 data_dict: data_list_type,
                 raw_data_dict: raw_data_list_type):
        """
        初始化过程
        :param file_path: 文件路径
        :param encoding: 编码方式（System Informer 中大多采用 UTF-8）
        :param data_dict: 封装在引号内的翻译条目（单行，上下文无关）
        :param raw_data_dict: 非封装翻译条目（多行或上下文相关）
        """
        self.file_path = file_path
        self.encoding = encoding
        self.data_dict = data_dict
        self.raw_dict = raw_data_dict

    @staticmethod
    def format_string(string: str):
        return format_string(string)

    @staticmethod
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

    def start(self):
        """
        Main procedure
        :return: None
        """
        print(f"正在处理文件：{self.file_path}，编码：{self.encoding}")
        with open(self.file_path, "r+", encoding=self.encoding) as file:
            file_data = file.read()
            ##########################################################
            # 处理跨行或上下文相关的文本内容
            if len(self.raw_dict) != 0:
                for _object in self.raw_dict:
                    old_item = _object[0]
                    new_item = _object[1]
                    file_data = file_data.replace(
                        old_item, # 不需要格式化
                        new_item
                    )
            ##########################################################
            # 处理上下文无关的文本内容
            if len(self.data_dict) != 0:
                for old_item in self.data_dict:
                    if old_item in SHOULD_NOT_TRANSLATE_STRING_LIST:
                        print(f"发现无法处理的条目：{old_item}")
                        continue
                    new_item = self.data_dict[old_item]
                    self.check_symbols(old_item, new_item)
                    file_data = file_data.replace(
                        self.format_string(old_item),
                        self.format_string(new_item)
                    )
            ##########################################################
            file.seek(0)
            file.write(file_data)
            file.truncate()