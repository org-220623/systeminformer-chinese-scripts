# System Informer 汉化项目

这是一个用于汉化 System Informer 字符串资源的脚本。（随时准备摆烂）

## [`Winsiderss/SystemInformer`](https://github.com/winsiderss/systeminformer) 上与 i18n 相关的 issue

从官方的态度和计划看，未来很长一段时间都不会有 i18n, 所以要么学会英语，要么学会搜索，要么学会劳动。

1. https://github.com/winsiderss/systeminformer/issues/302
2. https://github.com/winsiderss/systeminformer/issues/1219
3. https://github.com/winsiderss/systeminformer/issues/1301

## 说明

本项目因工程量太大，作者随时可能放弃维护并存档，想坚持到底的欢迎 Fork。

## 远程仓库信息

1. GitLab (Origin): https://gitlab.com/anonymous9075331734/systeminformer-chinese
2. Gitea (有时推送会失败): https://gitea.com/anonymous9075331734/systeminformer-chinese
3. GitHub (大陆已被 GFW, 不推荐国内访问): https://github.com/org-220623/systeminformer-chinese-scripts
4. Gitee (推荐国内访问): https://gitee.com/MICRO201014_admin/systeminformer-chinese
5. Jihu GitLab (Web UI 设计缺陷): https://jihulab.com/anonymous9075331734/systeminformer-chinese
6. Codeberg (未计划)
7. Riseup (未计划)
8. GitCode / AtomGit (未计划)

## 进度信息

1. 提示：`static_assert` 提示信息一律不处理。
2. 本项目仅处理 `SystemInformer/*`、`tools/*` 和 `plugins/*` 下的内容，`kphlib/*`、`phlib/*` 和 `KSystemInformer/*` 下的内容未计划处理。

### 跟踪情况

43be024f678599440beda86eb4c57521e7965e12

### todo

- 处理 PEView；
- 处理 11 个插件（待定）；

### 已完成的文件

#### 主程序 (`SystemInformer/*`) (已初步完成，挂起)

- `SystemInformer/log.c` 计划处理，挂起
- `phsvc/*` (没有要处理的条目)
- `sdk/*` (没有要处理的条目)
- 中间已处理的文件已省略...
- `ksidbg.c` (暂不处理)
- 中间已处理的文件已省略，**(log.c 未处理)**。
- `main.c` (已初步完成，可能要再次修改)
- `tokprp.c` (已初步完成，可能要再次修改)
- 末尾已处理的文件已省略...

#### 工具

##### PEView 工具 (`tools/peview/*`) (正在进行)

- 开头已处理的文件已省略...
- `exlfimports.c`

##### 已全部完成的模块（进度信息已省略）

- SetupTool (`tools/CustomSetupTool/*`) (已初步完成)

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

### 许可证

无许可证，想做什么都行。

P.S. **金玉其外，败絮其中**