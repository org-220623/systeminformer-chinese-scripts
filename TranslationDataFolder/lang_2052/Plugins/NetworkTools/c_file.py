from Config.const_values import CONST_PATH_PLUGIN_NETWORKTOOLS
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/main.c", "utf-8", {
        "Ping the Hostname or IP Address": "Ping 主机名或 IP 地址",
        "You can use an IPv4 or IPv6 address as the target or a fully qualified domain name (FQDN) or a website URL as the target.":
            "您可以使用 IPv4 或 IPv6 地址作为目标，也可以使用完全限定域名 (FQDN) 或网站 URL 作为目标。",
        "Tracert the Hostname or IP Address": "跟踪路由主机名或 IP 地址",
        "Whois the Hostname or IP Address": "Whois 主机名或 IP 地址",
        "&Network Tools": "网络工具(&N)",
        "&GeoLite database update...": "GeoLite 数据库更新(&G)...",
        "&Ping address...": "Ping 地址(&P)...",
        "&Traceroute address...": "跟踪路由地址(&T)...",
        "&Whois address...": "Whois 地址(&W)...",
        "&Ping": "Ping(&P)",
        "&Traceroute": "跟踪路由(&T)",
        "&Whois": "Whois(&W)",  # https://zh.wikipedia.org/wiki/WHOIS
        "Country": "国家",
        "Local service": "本地服务",
        "Remote service": "远程服务",
        "Total bytes in": "入站字节总计",
        "Total bytes out": "出站字节总计",
        # Line 452
    }, [
        ('''optionsEntry->CreateSection(
        L"NetworkTools"''', '''optionsEntry->CreateSection(
        L"网络工具"'''),
    ]),
]