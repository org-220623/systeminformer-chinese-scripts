# 配置文件

########################################################################################
# 定义字符串常量 (CONST_STRING_*)
CONST_STRING_ELLIPSIS = "..."
CONST_STRING_COLON = ":"
CONST_STRING_LF_NEWLINE = "\n"
CONST_STRING_CRLF_NEWLINE = "\r\n"
CONST_STRING_LEFT_BRACKET = "[ "
CONST_STRING_RIGHT_BRACKET = " ]"

########################################################################################
# 定义目录路径常量 (CONST_PATH_*)
# --------------------------------------------------------------------------------------
# System Informer 主程序目录
CONST_PATH_SYSTEM_INFORMER_SRC = "SystemInformer"
CONST_PATH_SYSTEM_INFORMER_INC = f"{CONST_PATH_SYSTEM_INFORMER_SRC}/include"
# --------------------------------------------------------------------------------------
# 工具目录
CONST_PATH_TOOLS_DIRECTORY = "tools"
CONST_PATH_PEVIEW_TOOL_SRC = f"{CONST_PATH_TOOLS_DIRECTORY}/peview"
CONST_PATH_SETUP_TOOL_SRC = f"{CONST_PATH_TOOLS_DIRECTORY}/CustomSetupTool"
# --------------------------------------------------------------------------------------
# Phlib 目录（我就不明白为什么有些字符串资源在这个目录下）
CONST_PATH_PHLIB_SRC = "phlib"
# --------------------------------------------------------------------------------------
# 插件目录
CONST_PATH_PLUGINS = "plugins" # internal, should not been imported
CONST_PATH_PLUGIN_DOTNETTOOLS = f"{CONST_PATH_PLUGINS}/DotNetTools"
CONST_PATH_PLUGIN_EXTENDEDNOTIFICATIONS = f"{CONST_PATH_PLUGINS}/ExtendedNotifications"
CONST_PATH_PLUGIN_EXTENDEDSERVICES = f"{CONST_PATH_PLUGINS}/ExtendedServices"
CONST_PATH_PLUGIN_EXTENDEDTOOLS = f"{CONST_PATH_PLUGINS}/ExtendedTools"
CONST_PATH_PLUGIN_HARDWAREDEVICES = f"{CONST_PATH_PLUGINS}/HardwareDevices"
CONST_PATH_PLUGIN_NETWORKTOOLS = f"{CONST_PATH_PLUGINS}/NetworkTools"
CONST_PATH_PLUGIN_ONLINECHECKS = f"{CONST_PATH_PLUGINS}/OnlineChecks"
CONST_PATH_PLUGIN_TOOLSTATUS = f"{CONST_PATH_PLUGINS}/ToolStatus"
CONST_PATH_PLUGIN_UPDATER = f"{CONST_PATH_PLUGINS}/Updater"
CONST_PATH_PLUGIN_USERNOTES = f"{CONST_PATH_PLUGINS}/UserNotes"
CONST_PATH_PLUGIN_WINDOWSEXPLORER = f"{CONST_PATH_PLUGINS}/WindowExplorer"
########################################################################################