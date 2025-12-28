from data import data
from _class import TranslateFileObject
for (file_path, encoding, translate_data) in data:
    obj = TranslateFileObject(
        file_path = "../" + file_path,
        encoding=encoding,
        data_dict=translate_data
    )
    obj.start()