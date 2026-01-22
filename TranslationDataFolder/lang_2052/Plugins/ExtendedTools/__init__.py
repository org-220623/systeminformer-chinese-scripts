from Config.static_data_type import TranslationDataType
from . import c_file, c_file_after_smbios_c

DATA: TranslationDataType = (
    c_file.DATA + c_file_after_smbios_c.DATA
)