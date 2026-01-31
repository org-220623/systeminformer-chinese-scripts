from Config.static_data_type import (
    EnumTranslateDotNetCounters,
    EnumTranslateMalwareScanningWebsite,
    EnumTranslateInHandleSecurityPropertiesPageMandatoryLevel,
    EnumTranslateSecurityEditorMandatoryLevel
)

# 处理 .NET 计数器全局选项
# 受影响的插件: DotNetTools (.NET 工具)
OPTION_TRANSLATE_DOTNET_COUNTERS: EnumTranslateDotNetCounters = EnumTranslateDotNetCounters.AddHeader

# 处理恶意软件扫描网站名称的全局选项
# 受影响的插件: OnlineChecks
OPTION_TRANSLATE_MALDETECT_WEBSITE: EnumTranslateMalwareScanningWebsite = EnumTranslateMalwareScanningWebsite.ToServiceName

# 处理句柄属性页中的强制完整性级别全局选项
# 警告: 涉及动态字符串替换
# 受影响的组件: Phlib
OPTION_TRANSLATE_HANDLE_PAGE_MANDATORY_LEVEL: EnumTranslateInHandleSecurityPropertiesPageMandatoryLevel =\
    EnumTranslateInHandleSecurityPropertiesPageMandatoryLevel.DynamicSubViewTranslate

# 处理安全编辑器页面中的强制完整性级别全局选项
# 警告: 涉及本地线程创建、窗口枚举、动态字符串替换
# 受影响的源代码文件和过程: SystemInformer/main.c -> wWinMain
OPTION_TRANSLATE_SECURITY_EDITOR_MANDATORY_LEVEL: EnumTranslateSecurityEditorMandatoryLevel =\
    EnumTranslateSecurityEditorMandatoryLevel.EnumWindowAndSubwindowTranslate