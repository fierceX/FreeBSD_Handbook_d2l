# FreeBSD 手册翻译项目 d2lbook优化版

## 原仓库信息
**本手册内容由[FreeBSD 中文社区](https://handbook.bsdcn.org)翻译，官方仓库为：[https://github.com/FreeBSD-Ask/handbook](https://github.com/FreeBSD-Ask/handbook)**

## 说明
为提升阅读体验，使用[d2lbook](https://book.d2l.ai/)进行编译成HTML和PDF、EPUB文档。

因为原d2lbook工具会使用ipynb作为中间存储结果，导致部分md格式导出成rst的过程中会出错，所以需要使用修改版的d2lbook：https://github.com/fierceX/d2l-book

当前同步中文仓库commit:[2022.11.14_14-21](https://github.com/FreeBSD-Ask/Handbook/commit/9ee9830f54e1aeacd267cf33e744d83b99c09127)

d2lbook生成静态页面：[FreeBSD_Handbook_d2l](https://fiercex.github.io/FreeBSD_Handbook_d2l/)

[最新PDF](https://fiercex.github.io/FreeBSD_Handbook_d2l/files/FreeBSD_Handbook.pdf)

[最新EPUB](https://fiercex.github.io/FreeBSD_Handbook_d2l/files/FreeBSD_Handbook.epub)

历史编译参见[Actions](https://github.com/fierceX/FreeBSD_Handbook_d2l/actions)
## 编译
1. 先安装d2lbook
   ```bash
   pip install git+https://github.com/fierceX/d2l-book
   ```
2. 编译PDF、HTML、EPUB：
   ```bash
   d2lbook build pdf html epub
   ```
结果在`_build`文件夹下生成
## 已知问题
1. 链接过多导致脚注超出页面，直接在源文件进行分页相关的操作（例如长表格分成多个小表格）