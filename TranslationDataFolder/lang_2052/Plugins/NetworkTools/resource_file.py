from Config.const_values import CONST_PATH_PLUGIN_NETWORKTOOLS
from Config.static_data_type import TranslationDataType

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/version.rc", "utf-8", {
        "Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved.":
            "版权所有 (c) Winsider Seminars & Solutions, Inc. 保留所有权利。",
    }, []),
    (f"{CONST_PATH_PLUGIN_NETWORKTOOLS}/NetworkTools.rc", "utf-8", {
        "Network Tools": "网络工具",
        "Options": "选项",
        "Ping packet length:": "Ping 数据包长度:",
        "Max Tracert Hops:": "最大跟踪路由跳数:",
        "Enable extended TCP statistics": "启用扩展 TCP 统计信息",
        "MaxMind GeoLite Account ID:": "MaxMind GeoLite 帐户 ID:",
        "Open GeoIP.conf": "导入 GeoIP.conf",
        "Change": "更改",
        "Note: You can also download GeoLite updates from the Main menu > Tools > Network Tools > Update GeoLite...": "注意: 您也可以从主菜单 > 工具 > 网络工具 > 更新 GeoLite 下载 GeoLite 更新...",
        "MaxMind GeoLite License Key:": "MaxMind GeoLite 许可证密钥:",
        "Download update": "下载更新",
        "GeoLite Update": "GeoLite 更新",
        "Close": "关闭",
        "Refresh": "刷新",
        "Save": "保存",
        "Cancel": "取消",
        "Pinging X with X bytes of data:": "正在 Ping X 具有 X 字节的数据:",
        "PingGraphLayout": "Ping 图表布局",
        "Ping statistics": "Ping 统计信息",
        "Average: 0.00 ms": "平均延迟: 0.00 ms",
        "Pings sent: 0": "已发送: 0",
        "Bad replies: 0": "无效回复: 0",
        "Minimum: 0.00 ms": "最小值: 0.00 ms",
        "Pings lost: 0 (0%)": "丢失: 0 (0%)",
        "Anon replies: 0": "匿名回复: 0",
        "Maximum: 0.00 ms": "最大值: 0.00 ms",
        "Deviation: 0.00 ms": "偏差: 0.00 ms",
        "Tracing route to xyz...": "正在跟踪路由 xyz...",
        "Update MaxMind License Key": "更新 MaxMind 许可证密钥",
        "Paste the license key below:": "在下方粘贴许可证密钥:",
        r'Checkout <a href=""https://support.maxmind.com/hc/en-us/articles/4407111582235-Generate-a-License-Key"">How-to-generate-a-license-key</a>':
            r'查看 <a href=""https://support.maxmind.com/hc/en-us/articles/4407111582235-Generate-a-License-Key"">如何生成许可证密钥</a>'
    }, [
        ('"MaxMind GeoLite License Key:",IDC_STATIC,16,116,97,8', '"MaxMind GeoLite License Key:",IDC_STATIC,16,116,130,8'), 
    ]),
]