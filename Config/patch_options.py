from Config.static_data_type import EnumTranslateDotNetCounters, EnumTranslateMalwareScanningWebsite

# 处理 .NET 计数器全局选项
# 受影响的插件：DotNetTools (.NET 工具)
OPTION_TRANSLATE_DOTNET_COUNTERS: EnumTranslateDotNetCounters = EnumTranslateDotNetCounters.AddHeader

# 处理恶意软件扫描网站名称的全局选项
# 受影响的插件：OnlineChecks
OPTION_TRANSLATE_MALDETECT_WEBSITE: EnumTranslateMalwareScanningWebsite = EnumTranslateMalwareScanningWebsite.ToServiceName