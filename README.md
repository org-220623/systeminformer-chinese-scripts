# System Informer 汉化项目

这是一个用于汉化 System Informer 字符串资源的脚本。（随时准备摆烂）

## [`Winsiderss/SystemInformer`](https://github.com/winsiderss/systeminformer) 上与 i18n 相关的 issue

从官方的态度和计划看，未来很长一段时间都不会有 i18n, 所以要么学会英语，要么学会搜索，要么学会劳动。

1. https://github.com/winsiderss/systeminformer/issues/302
2. https://github.com/winsiderss/systeminformer/issues/1219
3. https://github.com/winsiderss/systeminformer/issues/1301
4. AND AND AND MORE

## 说明

1. 本项目因工程量太大，作者随时可能放弃维护并存档，想坚持到底的欢迎 Fork。
2. 脚本仓库完全独立于 System Informer 源码仓库，本人复刻的源码仓库仅用来跟踪上游更新。

## 进度信息

1. 提示：`static_assert` 提示信息一律不处理。
2. 本项目仅处理 `SystemInformer/*`、`tools/*` 和 `plugins/*` 下的内容，以及 `phlib/*` 下与 UI 有关的内容，`kphlib/*` 和 `KSystemInformer/*` 下的内容未计划处理。

### 跟踪情况

62ddfd63185cdfbd5b721b411ff9bdeeecc76dbb

### todo

- 处理 11 个插件中未完成的 9 个：
   - HardwareDevices
   - DotNetTools
   - NetworkTools
   - WindowExplorer
   - ExtendedNotifications
   - ExtendedServices
   - OnlineChecks
   - Updater
   - UserNotes
   - ExtendedTools (已完成)
   - ToolStatus (已完成)
- 重审 `actions.c` 的翻译；
- 持续跟踪并完成 GitHub Issue 中的任务。

### 已完成的文件

#### 主程序 (`SystemInformer/*`) (已初步完成，挂起)

- `SystemInformer/log.c` 计划处理，挂起
- `SystemInformer/ksidbg.c` 计划处理，挂起
- `phsvc/*` (暂时没有要处理的条目)
- `sdk/*` (暂时没有要处理的条目)
- 中间已处理的文件已省略...
- `main.c` (已初步完成，可能要再次修改)
- `tokprp.c` (已初步完成，可能要再次修改)
- 末尾已处理的文件已省略...

#### 工具

##### PEView 工具 (`tools/peview/*`) (已初步完成，挂起)

- 备注：其中已处理的文件已省略，以下列出需要进行重新审查的文件：
- `disimp.c`

##### 已全部完成的模块（进度信息已省略）

- SetupTool (`tools/CustomSetupTool/*`) (已初步完成)

#### 插件

正在进行，进度见上。

## 依赖

### System Informer 项目依赖

- Visual Studio 2022
   - .NET 桌面开发
   - 使用 C++ 的桌面开发
   - 单个组件 -> 编译器、生成工具和运行时 -> Spectre 缓解库（最新）（x64/x86 和 ARM64/ARM64EC）

### 汉化脚本项目依赖

- Python 3.*（建议使用 3.12 及以上版本）

## 用法

### 构建 System Informer

请参考 System Informer 仓库说明中的“[构建项目](https://github.com/winsiderss/systeminformer?tab=readme-ov-file#building-the-project)”章节和 [build/README.md](https://github.com/winsiderss/systeminformer/blob/master/build/README.md)。

使用 Visual Studio 2026 并运行 `build_init.cmd` 或 `build_tools.cmd` 构建 `CustomBuildTool` 会提示“找不到链接库”，需通过打开 `tools/CustomBuildTool/CustomBuildTool.sln` 在 Visual Studio 中构建。建议使用 Visual Studio 2022 以避免此问题。

### 汉化项目

执行如下命令：

```bash
git clone https://github.com/winsiderss/systeminformer.git
cd systeminformer
git clone https://github.com/org-220623/systeminformer-chinese-scripts.git .i18n
cd .i18n
python main.py --nodebug
```

然后重新构建程序即可。

### 许可证

MIT

P.S. **金玉其外，败絮其中**