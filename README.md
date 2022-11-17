# FreeBSD 手册翻译项目 PDF优化版

**本手册内容由[FreeBSD 中文社区](https://handbook.bsdcn.org)翻译，官方仓库为：[https://github.com/FreeBSD-Ask](https://github.com/FreeBSD-Ask)**

本仓库使用[d2lbook](https://book.d2l.ai/)和Latex进行PDF的编译，为了适应d2book的一些特性，对部分格式做了微调，并且对最后生成的tex文件也做了一些调整。最终通过Latex编译成PDF。

## 编译
1. 先安装d2lbook，可以参考：https://book.d2l.ai/
2. 编译PDF：`d2lbook build pdf`，会在`_build`文件夹下生成pdf文件夹，所需要的tex文件和图片资源文件都会在此文件夹下生成。  
~~3. 修改`FreeBSD_Handbook.tex`文件：~~
   ~~1. 在`documentclass`中增加`oneside`，用于减少章节后面的空白页面~~
   ~~2. 修改logo的中的`sphinxincludegraphics`为`includegraphics`，并且增加`[width=0.4\linewidth]`，用于调整logo的大小~~
   ~~3. 将所有的章节标记增加一级，即将`chapter`提升至`part`，将`section`提升至`chapter`，将`subsection`提升至`section`等等。但是需要注意，前两章不需要提升（即**FreeBSD 手册**和**概述**）~~
~~4. 重新编译tex: `xelatex FreeBSD_Handbook.tex` 运行两次~~

## 已知问题
1. pandoc转rst格式时，会自动分割超长行，会导致带链接的行被拆分，导致后续的格式错误。解决办法是修改`nbconvert`库下的代码
   1. 编辑 `nbconvert/filters/pandoc.py` 文件，修改`convert_pandoc`函数的参数，赋给`extra_args`参数默认值为`['--columns','10000']`即可。
2. 链接过多导致脚注超出页面，目前没到找合适的解决方法，直接在源文件进行分页相关的操作（例如长表格分成多个小表格）