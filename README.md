# 关于
锐锐自己写的一些Glyphs3用Python脚本，也不知道有没有bug，欢迎反馈！

# 安装
1. 安装模块：打开Glyphs3-Window-Plugin Manager-Module，确保「Python」和「Vanilla」模块已经安装。 <br />
   如果你的电脑安装过Python，确保Glyphs-Preferences-Addons中Python version是合适的版本。我也不知道哪个是合适的，反正不行就多试几个；
2. 安装脚本：打开Glyphs3-Script-Open Script Folder，将下载的.py文件复制进脚本所在文件路径，然后重启Glyphs3以使用脚本。

# 说明
摸鱼脚本
* 图层展开：为所有选中字符创建各自的预览窗口，并在窗口中显示那个字符的所有图层；
* 统一视图图层：将预览窗口的所有字符的显示图层更改为当前所选中图层的同名图层，并删除没有同名图层的字符；
* 各母版预览：依次显示当前预览窗口的文本的所有母版图层，应用于多母版项目；
* 永结同心：计算选中字符的平均中心位置并显示在宏面板中；
* 要修边幅：删除完全处于字符最小边界框和最小边界框向内偏移100单位范围内的形状（后续可能会增加控件以一定以偏移单位大小）
* 森破图样：升级版Sample Strings，需要在脚本文件夹创建新的文件夹/SampleTextDataset，并在里面创建名为SampleText.txt的文本文档，可照猫画虎编辑文本，识别序列是 <br />
   `##标题##样本字串%%`
<br />或者直接下载提供的数据集；
* 一扫而空：清空所选图层的形状；
* GlyphModificationForEastAsianWidth：迅速调整全宽和半宽东亚字符的工具，多用于自动生成的字符；
