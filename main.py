from Config.debug_file import DEBUG_FILE
from Payload.objtype import TranslateFileObject
from sys import argv

# import data
import SystemInformer
import Tools

# create global data structure
TRANSLATION_DATA = (
        Tools.DATA +
        SystemInformer.DATA
)

if __name__ == '__main__':
    if len(argv) == 2:
        if argv[1] == "--nodebug":
            DEBUG_OPTION = False
        else:
            DEBUG_OPTION = True
    else:
        DEBUG_OPTION = True
    for (file_path, encoding, translate_data, raw_translate_data) in TRANSLATION_DATA:
        if (DEBUG_OPTION and DEBUG_FILE == file_path) or not DEBUG_OPTION:
            obj = TranslateFileObject(
                file_path = "../" + file_path,
                encoding=encoding,
                data_dict=translate_data,
                raw_data_dict=raw_translate_data
            )
            obj.start()