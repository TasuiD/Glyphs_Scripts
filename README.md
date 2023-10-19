# 关于
锐锐自己写的一些Glyphs3用Python脚本，也不知道有没有bug

# 安装
1. 安装模块：打开Glyphs3-Window-Plugin Manager-Module，确保「Python」和「Vanilla」模块已经安装；
2. 安装脚本：打开Glyphs3-Script-Open Script Folder，将下载的.py文件复制进脚本所在文件路径，然后重启Glyphs3以使用脚本。

# 说明
摸鱼脚本
* 图层展开：为所有选中字符创建各自的预览窗口，并在窗口中显示那个字符的所有图层；
* 统一视图图层：将预览窗口的所有字符的显示图层更改为当前所选中图层的同名图层，并删除没有同名图层的字符；
* 各母版预览：依次显示当前预览窗口的文本的所有母版图层，应用于多母版项目；
* 永结同心：计算选中字符的平均中心位置并显示在宏面板中
* 要修边幅：
* 森破图样：升级版Sample Strings，可照猫画虎编辑/SampleTextDataset/SampleText.txt中的文本。识别序列是
   `##标题在这##
  样本字串在这
  %%`
