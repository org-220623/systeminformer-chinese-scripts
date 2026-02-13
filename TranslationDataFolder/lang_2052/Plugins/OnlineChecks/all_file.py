from Config.const_values import CONST_PATH_PLUGIN_ONLINECHECKS
from Config.global_dict import GLOBAL_DICT
from Config.static_data_type import TranslationDataType, EnumTranslateMalwareScanningWebsite
from Config.patch_options import OPTION_TRANSLATE_MALDETECT_WEBSITE

DATA: TranslationDataType = [
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/main.c", "utf-8", {
        "All files (*.*)": "所有文件 (*.*)",
        "&Online Checks": "在线检查(&O)",
        "&Enable VirusTotal scanning": "启用 VirusTotal 扫描(&E)",
        "Upload file to &Filescan...": "上传文件至 FileScan(&F)...",
        "Upload file to &Hybrid-Analysis...": "上传文件至 Hybrid Analysis(&H)...",
        "Upload file to &VirusTotal...": "上传文件至 VirusTotal(&V)...",
        "&Upload file to VirusTotal...": "上传文件至 VirusTotal(&U)...", 
        "Upload file to &Jotti...": "上传文件至 Jotti(&J)...",
        "Upload unknown files to VirusTotal...": "上传未知文件至 VirusTotal...",
        "Sen&d to": "发送到(&D)",
        "Scanning disabled": "扫描已禁用",
        "Online Checks": "在线检查",
        "Allows files to be checked with online services.": "允许使用在线服务检查文件。",
    }, [
        ('''optionsEntry->CreateSection(
        L"OnlineChecks"''', '''optionsEntry->CreateSection(
        L"在线检查"'''),
    ]),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/OnlineChecks.rc", "utf-8", {
        "Options": "选项",
        "Enable VirusTotal scanning": "启用 VirusTotal 扫描",
        "Enable VirusTotal detection highlighting": "启用 VirusTotal 检测结果高亮显示",
        "Enable scanning": "启用扫描",
        "API key:": "API 密钥:",
        "Change": "更改",
        "Update Key": "更新密钥",
        "Save": "保存",
        "Cancel": "取消",
        "Paste the key below:": "在下方粘贴密钥:",
        'Checkout <a href="""">How-to-generate-a-license-key</a>': '查看 <a href="""">如何生成许可证密钥</a>',
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/options.c", "utf-8", {
        "Paste the license key here:": "在此处粘贴密钥:",
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/page1.c", "utf-8", {
        "Uploading %s...": "正在上传 %s...",
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/page2.c", "utf-8", {
        r"View last analysis\nView the last or outdated analysis page": r"查看最新分析结果\n查看最新或已过期的分析页面",
        r"Reanalyze file\nRescan the existing sample on VirusTotal": r"重新分析文件\n重新在 VirusTotal 扫描现有样本",
        r"Upload file\nUpload fresh sample for updated analysis": r"上传文件\n上传最新样本以进行更新分析",
        "%s was last analyzed %s": "%s 上次分析时间为 %s",
        "First analyzed:": "首次分析:",
        "Last analyzed:": "上次分析:",
        "Upload size:": "上传大小:",
        "You can take a look at the last analysis or upload it again now.": "您可以查看上次分析结果，或立即重新上传。",
        "Detections:": "检测结果:",
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/page3.c", "utf-8", {
        "Uploading %s...": "正在上传 %s...",
        "Uploaded: ~ of ~ (0%)\r\nSpeed: ~ KB/s": "已上传: ~ 共 ~ (0%)\r\n速度: ~ KB/s",
        "Rescanning %s...": "正在重新扫描 %s...",
        "Locating analysis for %s...": "正在查找 %s 的分析结果...",
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/page4.c", "utf-8", {
        "Uploading %s...": "正在上传 %s...",
        "Error uploading %s...": "上传 %s 时出错...",
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/upload.c", "utf-8", {
        "Unable to create the http socket.": "无法创建 HTTP 套接字。",
        "Unable to connect to the service.": "无法连接到服务。",
        "Unable to create the request.": "无法创建请求。",
        "Unable to send the request.": "无法发送请求。",
        "Unable to receive the request.": "无法接收请求。",
        "Unable to download the response.": "无法下载响应。",
        "Unable to upload the file": "无法上传文件",
        "Unable to open the file": "无法打开文件",
        "Unable to load the image.": "无法加载映像。",
        "File architecture not supported.": "不支持的文件架构。",
        "Unable to add request headers": "无法添加请求标头",
        "Unable to send the request": "无法发送请求",
        "Unable to write the post header": "无法写入 POST 标头",
        "Uploading %s...": "正在上传 %s...",
        "Unable to complete the request.": "请求无法完成。",
        "Unable to read the file": "无法读取文件",
        "Unable to upload the file data": "无法上传文件数据",
        "Uploaded: ": "已上传: ",
        " of ": " 共 ",
        "%)\r\nSpeed: ": "%)\r\n速度: ",
        "Unable to write the post footer": "无法写入 POST 页脚",
        "Unable to receive the response": "无法接收响应",
        "Unable to query http headers": "无法查询 HTTP 标头",
        "Hybrid Analysis API error.": "Hybrid Analysis API 错误。",
        "Unable to complete the request": "请求无法完成",
        "Unable to parse the request": "无法解析请求",
        "Unable to complete the request (please try again after a few minutes)": "请求无法完成 (请稍后再试)",
        "The file is too large (over 128 MB)": "文件过大 (超过 128 MB)",
        "The file is too large (over 100 MB)": "文件过大 (超过 100 MB)",
        "The file is too large (over 20 MB)": "文件过大 (超过 20 MB)",
        "You need to configure HybridAnalysis from the Options window > OnlineChecks page.": "您需要在“选项”窗口 > “在线检查”页面中配置 Hybrid Analysis。",
        "Unable to hash the file": "无法计算文件哈希",
        "Unable to parse the response.": "无法解析响应。",
        "You need to configure VirusTotal from the Options window > OnlineChecks page.": "您需要在“选项”窗口 > “在线检查”页面中配置 VirusTotal。",
        "VirusTotal ReScan API error.": "VirusTotal 重新扫描 API 错误。",
        "VirusTotal ViewReport API error.": "VirusTotal ViewReport API 错误。",
        "Initializing...": "初始化中...",
        "Unable to query the service.": "无法查询服务。",
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/version.rc", "utf-8", {
        "Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved.":
            GLOBAL_DICT["Copyright (c) Winsider Seminars & Solutions, Inc.  All rights reserved."],
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/virustotal.c", "utf-8", {
        "%s ago (%s)": "%s 以前 (%s)",
    }, []),
    (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/api.c", "utf-8", {
        "%s ago (%s)": "%s 以前 (%s)",
    }, []),
]

#######################################################################################
if OPTION_TRANSLATE_MALDETECT_WEBSITE == EnumTranslateMalwareScanningWebsite.ToServiceName:
    DATA.append(
        (f"{CONST_PATH_PLUGIN_ONLINECHECKS}/main.c", "utf-8", {
            "&Filescan.io": "FileScan.IO(&F)",
            "&Hybrid-analysis.com": "Hybrid Analysis(&H)",
            "Virusscan.&Jotti.org": "Jotti(&J)",
            "&VirusTotal.com": "VirusTotal(&V)",
            "&filescan.io": "FileScan.IO(&F)",
            "&hybrid-analysis.com": "Hybrid Analysis(&H)",
            "virusscan.&jotti.org": "Jotti(&J)",
            "&virustotal.com": "VirusTotal(&V)",
        }, [])
    )
#######################################################################################
