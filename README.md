# System Informer 汉化项目

这是一个用于汉化 System Informer 字符串资源的脚本。

## 软件下载

https://github.com/org-220623/si-chs-builds/releases/latest

## 说明

1. 本项目因工程量太大，作者随时可能放弃维护并存档，想坚持到底的欢迎 Fork。
2. 脚本仓库完全独立于 System Informer 源码仓库，本人复刻的源码仓库仅用来跟踪上游更新和测试构建，你可以在本人复刻的源码仓库中找到很多 `test/************` 分支。当前使用的复刻源码仓库：https://github.com/org-220623/systeminformer-chinese-2

## 进度信息

1. 提示：`static_assert` 提示信息一律不处理。
2. 本项目仅处理 `SystemInformer/*`、`tools/*` 和 `plugins/*` 下的内容，以及 `phlib/*` 下与 UI 有关的内容，`kphlib/*` 和 `KSystemInformer/*` 下的内容未计划处理。

### 跟踪情况

1a2d84bd98167e5de5035cd8e084e56d1f3dfb12

### todo

- 持续跟踪上游提交并完成 GitHub Issue 中的任务。

## 依赖

### System Informer 项目依赖

- Visual Studio 2022
   - .NET 桌面开发
   - 使用 C++ 的桌面开发
   - 单个组件 -> 编译器、生成工具和运行时 -> Spectre 缓解库（最新）（x64/x86 和 ARM64/ARM64EC）

以上信息可能过时，详细信息请参考 System Informer 仓库说明中的“[构建项目](https://github.com/winsiderss/systeminformer?tab=readme-ov-file#building-the-project)”章节和 [build/README.md](https://github.com/winsiderss/systeminformer/blob/master/build/README.md)。

### 汉化脚本依赖

- Python 3.*（建议使用 3.12 及以上版本）

## 用法

执行如下命令或操作：

```bash
git clone https://github.com/winsiderss/systeminformer.git systeminformer
cd systeminformer
build\build_init.cmd
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 由于 System Informer 主开发分支情况并不稳定，有可能出现构建失败的情况，因此请按照下述列表切换至某次特定提交。
# 切换提交的语法为（用下面列表中你想构建的版本的提交哈希替换 "<commit-hash>"，此时仓库进入分离头指针 (detached head) 状态，无法进行提交操作）：
#       git checkout <commit-hash> 
# 如果你想切换至某次提交并在此之上创建新的分支（这样可以创建新的提交），请执行以下操作（使用你想创建的分支名称替换 "<new-branch-name>"，你想构建的版本的提交哈希替换 "<commit-hash>"）：
#       git checkout -b <new-branch-name> <commit-hash>
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
git clone https://github.com/org-220623/systeminformer-chinese-scripts.git chs_l10n
cd chs_l10n && python main.py --nodebug
cd ..\build && build_release.cmd
```

构建的可直接执行二进制文件位于根目录下 `/bin/<计算机架构>/`，安装包、符号文件和 binlog 位于 `/build/output/`。

### 版本和提交哈希

以下数据来源于 [System Informer 预发行版构建仓库](https://github.com/winsiderss/si-builds) 和 System Informer 正式版本二进制文件信息。

| 版本 | 哈希 |
|--|--|
| v4.0.26036.1143 (预发行) | 774d2ec4b6d029fe8b111a46e74f39792f97f23b |
| v3.4.26017.1750 (预发行) | 533bf1b384a8eaa80ae5004078e82ab0609fb3fe |

## 许可证

MIT
