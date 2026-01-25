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
        "Packet loss": "丢包",
        "Jitter (ms)": "抖动 (毫秒)",
        "Latency (ms)": "延迟 (毫秒)",
        "Extended TCP statistics are disabled": "扩展 TCP 统计信息已禁用",
        "Geoip database not found.": "未找到 GeoIP 数据库。",
        "Network Tools": "网络工具",
        "Provides ping, traceroute and whois for network connections.": "提供网络连接的 Ping、跟踪路由和 Whois 查询。",
    }, [
        ('''optionsEntry->CreateSection(
        L"NetworkTools"''', '''optionsEntry->CreateSection(
        L"网络工具"'''),
    ]),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/options.c", "utf-8", {
        "GeoLite Country (Small)": "GeoLite 国家 (小)",
        "GeoLite City (Large)": "GeoLite 城市 (大)",
        "GeoIP.conf files (*.conf)": "GeoIP 配置文件 (*.conf)",
        "All files (*.*)": "所有文件 (*.*)",
        "Paste the account id here:": "在此处粘贴帐户 ID:",
        "Paste the license key here:": "在此处粘贴许可证密钥:",
    }, []),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/pages.c", "utf-8", {
        "Restart": "重启",
        "Download": "下载",
        "Network Tools - GeoLite Updater": "网络工具 - GeoLite 更新程序",
        "Download the latest GeoLite database?": "是否下载最新的 GeoLite 数据库?",
        r"This product includes GeoLite2 data created by MaxMind, available from <a href=\"https://www.maxmind.com\">https://www.maxmind.com</a>\r\n\r\nSelect download to continue.":
            r"本产品包含 MaxMind 创建的 GeoLite2 数据，可从 <a href=\"https://www.maxmind.com\">https://www.maxmind.com</a> 获取。\r\n\r\n单击 \"下载\" 以继续。",
        "Downloading": "正在下载",
        r"Downloaded: ~ of ~ (~%%)\r\nSpeed: ~/s": r"已下载: ~ 共 ~ (~%%)\r\n速度: ~/s",
        "The GeoLite database has been updated.": "GeoLite 数据库已更新。",
        "Please restart System Informer for the changes to take effect...": "请重启 System Informer 以使更改生效...",
        "Error downloading GeoLite database.": "下载 GeoLite 数据库时出错。",
        "[%lu] Access denied (invalid license key)": "[%lu] 访问被拒绝 (许可证密钥无效)",
        "Click Retry to download the update again.": r"点击 \"重试\" 重新下载更新。",
        "Unable to download GeoLite update.": "无法下载 GeoLite 更新。",
        "Please check the Options > Network Tools > GeoLite ID or Key are configured before downloading geoLite updates.": "请在下载 GeoLite 更新之前，检查“选项”>“网络工具”>“GeoLite ID 或密钥”是否已配置。",
    }, []),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/ping.c", "utf-8", {
        "Pinging %s with %lu bytes of data...": "正在 Ping %s 具有 %lu 字节的数据...",
        "Average: %.2f ms": "平均延迟: %.2f ms",
        "Minimum: %.2f ms": "最小值: %.2f ms",
        "Maximum: %.2f ms": "最大值: %.2f ms",
        "Pings sent: %lu": "已发送: %lu",
        "Pings lost: %lu (%.0f%%)": "丢失: %lu (%.0f%%)",
        "Deviation: %.2f ms": "偏差: %.2f ms",
        "Bad replies: %lu": "无效回复: %lu",
        "Variance: %.2f ms": "偏差: %.2f ms",
        "Anon replies: %lu": "匿名回复: %lu",
    }, []),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/tracert.c", "utf-8", {
        "Tracing %s...": "正在跟踪 %s...",
        "Tracing route to %s with %lu bytes of data...": "正在跟踪路由 %s 具有 %lu 字节的数据...",
        "Traceroute": "跟踪路由",
        "Copy": "复制",
        "Tracing %s... %s": "正在跟踪 %s... %s",
        "error": "错误",
        "complete": "完成",
        "Tracing route to %s with %lu bytes of data... %s.": "正在跟踪路由 %s 具有 %lu 字节的数据... %s。"
    }, []),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/tracetree.c", "utf-8", {
        "The destination address route is unreachable.": "目标地址路由不可达。",
        "Geoip database not found.": "未找到 GeoIP 数据库。",
        "Time": "时间",
        "IP Address": "IP 地址",
        "Hostname": "主机名",
        "Country": "国家",
    }, []),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/update.c", "utf-8", {
        "Country": "国家",  # todo 翻译存疑
        "City": "城市",
        "Connecting...": "正在连接...",
        "Sending download request...": "正在发送下载请求...",
        "Waiting for response...": "正在等待请求响应...",
        "Downloading GeoLite2-%s...": "正在下载 GeoLite2-%s...",
        "Downloaded: ": "已下载: ",
        "%)\r\nSpeed: ": "%)\r\n速度: ",
        "Initializing...": "初始化中...",
        "The GeoLite updater doesn't support legacy versions of Windows.": "GeoLite 更新程序不支持旧版 Windows 系统。",
        "Network Tools - GeoLite Updater": "网络工具 - GeoLite 更新程序",
        "Unable to download GeoLite database updates.": "无法下载 GeoLite 数据库更新。",
        "A license key and account number are required to download GeoLite database updates and either the key or number are not configured.\n\n":
            "下载 GeoLite 数据库更新需要许可证密钥和帐户号，但密钥或帐户号未配置。\n\n",
        r"GeoLite license keys and accounts are free. If you're unsure how to create keys then please "
                r"review the documentation here: <a href=\"https://support.maxmind.com/hc/en-us/articles/4407111582235-Generate-a-License-Key\">Generate-a-License-Key</a>\n\n":
            r"GeoLite 许可证密钥和帐户是免费的。如果您不确定如何创建密钥，请参阅此处的文档: <a href=\"https://support.maxmind.com/hc/en-us/articles/4407111582235-Generate-a-License-Key\">创建许可证密钥</a>\n\n",
        r"Once you've created the key you can copy/paste the text into the Options window > NetworkTools settings and System Informer can start downloading GeoLite database updates.\n\n":
            r"创建密钥后，您可以将文本复制/粘贴到“选项”窗口 > “网络工具”设置中，然后 System Informer 即可开始下载 GeoLite 数据库更新。\n\n",
        r"Special thanks to MaxMind (<a href=\"https://www.maxmind.com\">https://www.maxmind.com</a>) for continuing free GeoLite services <3":
            r"特别感谢 MaxMind (<a href=\"https://www.maxmind.com\">https://www.maxmind.com</a>) 持续提供免费的 GeoLite 服务 <3",
        "Unable to create the window.": "无法创建窗口。",
    }, []),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/whois.c", "utf-8", {
        "Connecting to whois.iana.org...": "正在连接到 whois.iana.org...",
        "Connection to whois.iana.org failed.\n": "连接到 whois.iana.org 失败。\n",
        "Error parsing whois.iana.org response:\n%s\n": "解析 whois.iana.org 响应时出错:\n%s\n",
        "Connecting to %s...": "正在连接到 %s...",
        "%s referred the request to %s\n": "%s 将请求转发至 %s\n",
        "\nOriginal request to %s:\n%s\n": "\n发往 %s 的原始请求:\n%s\n",
        "Connection to %s failed.\n": "连接到 %s 失败。\n",
        "&Copy": "复制(&C)",
        "&Select all": "全选(&S)",
        "Unable to display the whois window.": "无法显示 Whois 查询窗口。",
    }, []),
]