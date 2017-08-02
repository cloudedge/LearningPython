Note
# 记忆内容
用%r 输出string 会带双引号 ！

Can I use single-quotes or double-quotes to make a string or do they do different things?
In Python either way to make a string is acceptable although typically you'll use single-quotes for any short strings like 'a' or 'snow'.

Python %r时，如果字符串内层有单引号或双引号，外层会采用另外一种引号

""" 之间的文字可分行输出
''' (三个单引号)取代三个双引号，效果一样

print 结尾加上逗号，后续打印会连续输出不换行
如果前面有格式符，后面需要加%
多个打印之间需要通过逗号分隔

\(在行尾时)	续行符
\r	回车
\f	换页

raw_input()函数将用户输入的任意类型数据都转换为一个字符串。 raw_input() 会从标准输入（sys.stdin）读取输入值并返回一个字符串，且尾部换行符从末尾移除

widows powershell下
python -m pydoc os可用来显示操作系统相关参数

filename.close() filename.close均可

文件对象 = open(文件名)然后进行文件操作
文件操作：
close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
read – 读取文件内容。你可以把结果赋给一个变量。
readline – 读取文本文件中的一行。
truncate – 清空文件，请小心使用该命令。
write(stuff) – 将 stuff 写入文件。

 from ex25 import *

elements = range(0, 6)
python中只要一行用colon冒号结尾，下一行必须4个空格缩进，否则报错

for num in range(0, 6)
range返回的是整数列表[0,1,2,3,4,5]
表达式执行一次，直接产生循环序列，循环变量依次赋值
循环变量 每次会直接移动到列表中下一项，即使循环体内对循环变量进行改变，结果循环变量还是依次加1

for 不能直接写 for i < 6:

# 常见错误：
* print 中多个打印参数需要用,间隔开
* print 中打印内容前不要忘记加%
* def后面勿忘加：
* 文件文件退出后勿忘关闭


# 疑问
* / ** 开头的变量指的是指针吗？
