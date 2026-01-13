from . import c_file
from . import resource_file
from . import header_file

DATA = (
        c_file.DATA +
        resource_file.DATA +
        header_file.DATA
)