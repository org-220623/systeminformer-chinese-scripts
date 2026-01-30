from Config.static_data_type import (
    EnumTranslateDotNetCounters,
    EnumTranslateMalwareScanningWebsite,
    EnumTranslateMandatoryLevel
)

# 处理 .NET 计数器全局选项
# 受影响的插件: DotNetTools (.NET 工具)
OPTION_TRANSLATE_DOTNET_COUNTERS: EnumTranslateDotNetCounters = EnumTranslateDotNetCounters.AddHeader

# 处理恶意软件扫描网站名称的全局选项
# 受影响的插件: OnlineChecks
OPTION_TRANSLATE_MALDETECT_WEBSITE: EnumTranslateMalwareScanningWebsite = EnumTranslateMalwareScanningWebsite.ToServiceName

# 处理强制完整性级别全局选项
# 涉及动态字符串替换
# 受影响的组件: Phlib
OPTION_TRANSLATE_MANDATORY_LEVEL: EnumTranslateMandatoryLevel = EnumTranslateMandatoryLevel.DynamicSubViewTranslate