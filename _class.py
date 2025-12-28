from data import data_dict_type

class TranslateFileObject:
    def __init__(self,
                 file_path: str,
                 encoding: str,
                 data_dict: data_dict_type):
        self.file_path = file_path
        self.encoding = encoding
        self.data_dict = data_dict

    @staticmethod
    def format_string(string: str):
        return "\"" + string.replace("\n", "\\n") \
                     .replace("\t", "\\t") \
                     .replace("\0", "\\0") + "\""

    @staticmethod
    def check_symbols(old: str, new: str):
        if old[-1] == ":" and new[-1] != ":":
            print(f"发现不符合格式的项目：【{old}】，【{new}】")

    def start(self):
        with open(self.file_path, "r+", encoding=self.encoding) as file:
            file_data = file.read()
            for old_item in self.data_dict:
                new_item = self.data_dict[old_item]
                self.check_symbols(old_item, new_item)
                file_data = file_data.replace(
                    self.format_string(old_item),
                    self.format_string(new_item)
                )
            file.seek(0)
            file.write(file_data)
            file.truncate()