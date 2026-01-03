# System Informer 汉化项目

这是一个用于汉化 System Informer 字符串资源的脚本。

## 进度信息

1. 提示：`static_assert` 提示信息一律不翻译。
2. 本项目仅处理 `SystemInformer/*`、`tools/*` 和 `plugins/*` 下的内容，`kphlib/*`、`phlib/*` 和 `KSystemInformer/*` 下的内容未计划处理。

### todo

- ksisup.c from line 315
- log.c pending
- mainwnd.c from line 3873
- And more...

### 已完成的文件

#### 主程序 (`SystemInformer/*`)

- `phsvc/*` (没有要翻译的条目)
- `sdk/*` (没有要翻译的条目)
- And more
- `ksidbg.c` (暂不翻译)
- And more **but log.c hasn't been translated**.
- `main.c` (已初步完成，可能要再次修改)
- files between up and down haven't translated.
- `mdump.c`
- files between up and down haven't translated.
- `SystemInformer.rc`
- files between up and down haven't translated.
- `version.rc`

#### 工具

##### PEView 工具 (`tools/peview/*`)

- `peview.rc`

##### SetupTool (`tools/CustomSetupTool/*`)（已初步完成）

- `extract.c`
- `install.c` (没有要翻译的条目)
- `main.c`
- `resource.h` (没有要翻译的条目)
- `resource.rc` (没有要翻译的条目)
- `setup.h` (没有要翻译的条目)
- `startpage.c`
- `uninstall.c`
- `util.c` (没有要翻译的条目)
- `version.rc`
- `update.c` 

#### 插件

（尚未开始）

## 依赖

### System Informer 项目依赖

- Visual Studio 2022
   - .NET 桌面开发
   - 使用 C++ 的桌面开发
   - 单个组件 -> 编译器、生成工具和运行时 -> Spectre 缓解库（最新）（x64/x86 和 ARM64/ARM64EC）

### 汉化脚本项目依赖

- Python 3.*（建议使用 3.10 及以上版本）

## 用法

### 构建 System Informer

请参考 System Informer 仓库说明中的“[构建项目](https://github.com/winsiderss/systeminformer?tab=readme-ov-file#building-the-project)”章节和 [build/README.md](https://github.com/winsiderss/systeminformer/blob/master/build/README.md)。

使用 Visual Studio 2026 并运行 `build_init.cmd` 或 `build_tools.cmd` 构建 `CustomBuildTool` 会提示“找不到链接库”，需通过打开 `tools/CustomBuildTool/CustomBuildTool.sln` 在 Visual Studio 中构建。建议使用 Visual Studio 2022 以避免此问题。

### 汉化项目

执行如下命令：

```bash
git clone https://github.com/winsiderss/systeminformer.git
cd systeminformer
git clone https://gitlab.com/anonymous9075331734/systeminformer-chinese
cd systeminformer-chinese
python main.py
```

然后重新构建程序即可。

### 已追踪提交情况

请见 [GitLab Wiki](https://gitlab.com/anonymous9075331734/systeminformer-chinese/-/wikis/internal/tracked-commits)。