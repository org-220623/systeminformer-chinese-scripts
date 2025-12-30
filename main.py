from data import TRANSLATION_DATA, debug, debug_file
from _class import TranslateFileObject

if __name__ == '__main__':
    for (file_path, encoding, translate_data) in TRANSLATION_DATA:
        if (debug and debug_file == file_path) or not debug:
            obj = TranslateFileObject(
                file_path = "../" + file_path,
                encoding=encoding,
                data_dict=translate_data
            )
            obj.start()