from Config.const_values import CONST_PATH_PLUGIN_UPDATER
from Config.global_dict import GLOBAL_DICT
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_UPDATER}/main.c", "utf-8", {
        "Switch update &channel": "切换更新通道(&C)",
        "Release": "正式版",
        "Preview": "预览版",
        "Canary": "测试版",
        "Developer": "开发者版",
        "Check for &updates": "检查更新(&U)",
        "Update Checker": "更新管理器",
        "Plugin for checking new System Informer releases via the Help menu.": "用于通过“帮助”菜单检查 System Informer 新版本的插件。",
    }, [
        ('''optionsEntry->CreateSection(
        L"Updater"''', '''optionsEntry->CreateSection(
        L"更新程序"'''),
    ]),
    (f"{CONST_PATH_PLUGIN_UPDATER}/options.c", "utf-8", {
        "Last update check: %s (%s ago)": "最近检查更新: %s (%s 以前)",
        "Next update check: %s (%s)": "下次检查更新: %s (%s)",
        "Next update check: %s": "下次检查更新: %s"
    }, []),
]