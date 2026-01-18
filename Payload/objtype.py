from Config.const_values import CONST_STRING_NOT_TRANSLATE_PREFIX
from Config.static_data_type import data_list_type, raw_data_list_type
from Payload.misc_functions import format_string, check_symbols, do_nothing_x
from Config.not_translate_data import SHOULD_NOT_TRANSLATE_STRING_LIST


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
        self.shouldNotTranslateList = []
        self.file_path = file_path
        self.encoding = encoding
        self.data_dict = data_dict
        self.raw_dict = raw_data_dict
        for key in self.data_dict:
            if key[:len(CONST_STRING_NOT_TRANSLATE_PREFIX)] == CONST_STRING_NOT_TRANSLATE_PREFIX:
                self.shouldNotTranslateList.append(key[len(CONST_STRING_NOT_TRANSLATE_PREFIX):])

    def start(self):
        """
        Main procedure
        :return: None
        """
        print(f"正在处理文件：{self.file_path}，编码：{self.encoding.replace("utf-8-sig", "utf-8-bom").upper()}")
        try:
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
                        if old_item[:len(CONST_STRING_NOT_TRANSLATE_PREFIX)] == CONST_STRING_NOT_TRANSLATE_PREFIX:
                            continue
                        if old_item in SHOULD_NOT_TRANSLATE_STRING_LIST:
                            print(f"发现无法处理的条目：{old_item}")
                            continue
                        if old_item in self.shouldNotTranslateList:
                            print(f"发现无法处理的条目：{old_item}")
                            continue
                        new_item = self.data_dict[old_item]
                        check_symbols(old_item, new_item)
                        file_data = file_data.replace(
                            format_string(old_item),
                            format_string(new_item)
                        )
                ##########################################################
                file.seek(0)
                file.write(file_data)
                file.truncate()
        except Exception as x:  # 由于旧版的 System Informer 没有 usrlist.c 故忽略此类错误。
            do_nothing_x(x)     # 占位，以后 x 可能有用。
            print(f"\t无法打开文件: {self.file_path}")