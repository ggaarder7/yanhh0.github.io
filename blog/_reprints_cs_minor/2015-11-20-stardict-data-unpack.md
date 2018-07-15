---
title: 解出星际译王词典
author: zlr
source: http://zlr.iteye.com/blog/2258123
---

制作trados词库的工具及其方法

主要是为了抛砖引玉，希望各位词库制作高手或是软件编程人员能够给给意见；
大家一起交流交流，共同提高。

金山词霸专业词典解码工具： KSdrip.exe

具体方法 把KSdrip.exe程序复制到金山词霸的dicts目录下，开始运行CMD，进
入命令提示符窗口，输入“cd C:/Program Files/Kingsoft/Powerword
2007/dicts”，即输入dicts文件夹的实际安装路径；然后输入“KSdrip 词典
名.DIC”并回车，会在dicts目录下解出一个新文件夹，用UltraEdit打开这个文
件夹中格式为Da3的文件。

解出星际译王词典的工具： stardict-editor.exe

具体方法 把stardict-editor.exe复制到C:\Program Files\Common
Files\GTK\2.0\bin目录下，StarDict词典文件包含dz，idx和ifo文件，先用
7-zip软件对dz文件进行解压生成dict格式的文件；运行stardict-editor.exe，
在“DeCompile”选项下，选择ifo格式文件，并执行DeCompile，就会在Bin目录下
生成txt格式的词典文件。

解出Babylon词典解码的工具： stardict-editor.exe

具体方法 Babylon词典文件的格式为BGL，运行stardict-editor.exe，在
Compile选项下打开BGL文件，选择“Babylon file”，开始Build，在Bin目录下生
成babylon格式的词典文件；继续在Compile选项下打开生成的Babylon文件，选
择“BGL file”，开始Build，生成Stardict格式的词典文件；用上面的方法
DeCompile出StarDict格式的词典文件。

UltraEdit的使用 替换公式

删除空行

删除重复行


解出来的字典文件全部复制到excel工作表中，然后借助multiterm术语制作工具进行转换。

金山词霸专业词典解码工具： KSdrip.exe

具体方法 把KSdrip.exe程序复制到金山词霸的dicts目录下，开始运行CMD，进
入命令提示符窗口，输入“cd C:/Program Files/Kingsoft/Powerword
2007/dicts”，即输入dicts文件夹的实际安装路径；然后输入“KSdrip 词典
名.DIC”并回车，会在dicts目录下解出一个新文件夹，用UltraEdit打开这个文
件夹中格式为Da3的文件。

昨天找一下快速制作适用于minipad2的字典档的方法，想不到真的找到了，而且
很快很方便，现在分享一下。

（警告：字典档可能会有版权问题。警告2：字典档通常很大。而主站和论坛都
是徐大的。唔，大家看着办。）

简介：就是把别家的字典档转成minipad2可用的。重点是相对的字典档和反编译
工具。这里用星际译王的字典档做例子：

所需工具：
1. 7-zip（解压缩程式）
2. GTK库（一个图形用户界面dll库）
3. stardict-editor（星际译王官方编辑器，需要GTK库）

对应下载（全部为绿色免安装版）：
1. http://portableapps.com/apps/utilities/7-zip_portable
2. http://sourceforge.net/projects/portableapps/files/GTK%20Portable/
    （这里版本是旧的，但不影响功能。贪它小巧免安装。）
3. http://downloads.sourceforge.net/stardict/stardict-editor-3.0.1.rar
其中7-zip，GTK是自解的，选择解压缩的目的地就好了。

首先准备好stardict-editor：
1. 解压"GTK_Portable_Legacy_2.6.10.paf.exe"至"GTKLegacy\"。这里只有
   "GTKLegacy\bin"是需要的。
2. 解压"stardict-editor-3.0.1.rar"，里面只有一个编辑器"stardict-editor.exe"。
3. 把"stardict-editor.exe"放到"GTKLegacy\bin"。
（呵呵，星际译王编辑器组合完成。）

过程（第四至九步可以看图）：
1. 下载一个星际译王的字典档的包包，包里通常有三个文件，分别以
   ".dict.dz"、".idx"和".ifo"为副档名。解压备用。（下面一律以副档名代
   表该文件。）
2. 用7-zip解压".dict.dz"，得到".dict"。
3. 将同名的".dict"、".idx"和".ifo"放到同一文件夹下。
4. 启动"stardict-editor.exe"，点上面"DeCompile"（反编译）。
5. 点"Browse..."选择".ifo"的文件。
6. 点下面的"Decompile"（反编译）。
7. 等反编译结果。（我这里反编译一个14.2MB的"牛津高阶英汉双解.dic"不用10秒。）
8. 当看到三行英文字就代表完成程序。如果第二行不是以"Error"开头，就可以
   在"GTKLegacy\bin"找到同名的".txt"。
9. 最后一步是在".txt"的开始加上一行"@词典名称//备注"（不要用Notepad，
   文件大。我用Notepad++），然后改成".dic"（没有t）放在"minipad2\dict"
   就可以用了。

Notepad++绿色免安装版：
http://portableapps.com/apps/development/notepadpp_portable

最后附上几个可用的网址（它的官网好像本来是有很多的，因版权问题全都删掉了）：
1. （官方英文论坛，要注册）http://www.stardict.org/forum/index.php
2. （官方中文论坛，要注册）http://www.stardict.cn/forum/index.php
3. http://reciteword.cosoft.org.cn/stardict-iso/stardict-dic/
4. http://iask.sina.com.cn/u/1567516921/ish?folderid=37925
5. ftp://ftp.freebsd.org/pub/FreeBSD/ports/distfiles/stardict/

字典档我只用了两个，加上论坛上现有的，够用了：
1. 牛津高阶英汉双解修正版（增补多处漏词+美化（包括挤在一起的phr））
    http://www.stardict.cn/forum/viewtopic.php?f=12&t=518
2. DrEye4in1词典文件
    http://www.stardict.cn/forum/viewtopic.php?f=12&t=436

P.S. kdic和zdic好像也可以反编译，有兴趣的可以去找找。

http://blog.csdn.net/yangxiaojun9238/article/details/8482170

zh_CN 简体中文词典
http://abloz.com/huzheng/stardict-dic/zh_CN/ 
