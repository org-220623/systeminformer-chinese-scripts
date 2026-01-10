# System Informer 汉化项目

这是一个用于汉化 System Informer 字符串资源的脚本。（正在施工）

## 远程仓库

1. GitLab (Origin): https://gitlab.com/anonymous9075331734/systeminformer-chinese
2. Gitea (有时推送会失败): https://gitea.com/anonymous9075331734/systeminformer-chinese
3. GitHub (大陆已被 GFW, 不推荐国内访问): https://github.com/org-220623/systeminformer-chinese-scripts
4. Gitee (推荐国内访问): https://gitee.com/MICRO201014_admin/systeminformer-chinese
5. Jihu GitLab (Web UI 设计缺陷): https://jihulab.com/anonymous9075331734/systeminformer-chinese
6. Codeberg (未计划)
7. Riseup (未计划)
8. GitCode / AtomGit (未计划)

## 进度信息

1. 提示：`static_assert` 提示信息一律不翻译。
2. 本项目仅处理 `SystemInformer/*`、`tools/*` 和 `plugins/*` 下的内容，`kphlib/*`、`phlib/*` 和 `KSystemInformer/*` 下的内容未计划处理。

### todo

- ksisup.c 从第 315 行开始
- log.c 延迟翻译
- prpgmod.c
- prpgperf.c
- prpgsrv.c
- prpgstat.c
- prpgthrd.c
- prpgtok.c
- prpgvdm.c
- prpgwmi.c
- runas.c
- And more...

### 已完成的文件

#### 主程序 (`SystemInformer/*`) (正在进行)

- `phsvc/*` (没有要翻译的条目)
- `sdk/*` (没有要翻译的条目)
- 中间已翻译的文件已省略...
- `ksidbg.c` (暂不翻译)
- 中间已翻译的文件已省略，**(log.c 未翻译)**。
- `main.c` (已初步完成，可能要再次修改)
- `mainwnd.c`
- 中间已翻译的文件已省略...
- `options.c`
- 中间的文件未翻译
- `searchbox.c` (没有要翻译的条目)
- 中间的文件未翻译
- `SystemInformer.rc`
- 中间的文件未翻译
- `version.rc`

#### 工具

##### PEView 工具 (`tools/peview/*`) (未完成，挂起)

- `peview.rc`

##### SetupTool (`tools/CustomSetupTool/*`) (已初步完成)

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