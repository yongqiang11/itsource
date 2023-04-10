# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03_字符串.py
# Time       ：2023/3/17 16:27
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# TODO 字符串的认识
'''
字符串指的是一串连续的字符符号，通常用来记录、显示或比较字符内容。
Python中字符串是由单引号、双引号、三引号引起来表示的.
如果字符串的内容中包含了特殊字符，如单引号，那么就需要使用转义符号 \ 来进行转义
转义字符\可以将无意义的字符转换为具有指定功能的字符.
\n: 代码换行
\t: 代表制表符(tab键)
\\: 代表\字符
'''

print('abc\nqwe')
print('abc\tqwe')
print('abc\\qwe')

# TODO 检索字符串
'''
# 可以通过索引下标和切片实现      
# 字符串截取遵循“左闭右开”原则，也叫“包左不包右”
语法： 字符 = 字符串[索引]
语法： 子字符串= 字符串[开始:结束:步长]  
索引:用来定位元素的,正:从左向右定位; 负: 从右向左定位
步长:用来确定截取的方向,正:从左向右; 负:从右向左取
开始：如果不指定，默认为 0，也就是从字符串的开头截取
结束：如果不指定，默认为字符串的长度；
'''
str = 'mydsdksukss'
print(str[0])
print(str[-1])
print(str[1:3:1])
print(str[1:3:2])
print(str[::-1])  # 从最后往前取
print(str[0:-6])

# str.index('子字符串')
# 查找子字符串在字符串中出现的位置（下标）,找不到抛出错误
str1 = 'hello'
print(str1.index('el'))  # 找到返回索引位置
# print(str1.index('le')) # 找不到抛出错误
print('==' * 20)

# str.find('子字符串')
# 查找子字符串在字符串中出现的位置（下标）,找不到返回-1
print(str1.find('el'))  # 找到返回索引位置
print(str1.find('le'))  # 找不到抛出错误

# TODO 删除字符串
# 语法：del 字符串

# s = 'wqe'
# del s
# print(s)

# TODO 字符串的遍历
'''
# while 遍历
语法：
索引 = 0
长度 = len(字符串)
while 索引 < 长度
    print(字符串[索引])
    索引 += 1

# for 循环
for 字符  in  字符串：
    print(字符)
'''
s = '让学习成为一种习惯'
i = 0
length = len(s)
while i < length:
    print(s[i])
    i += 1

print('==' * 20)

for value in s:
    print(value)

# TODO 字符串去除空格
'''
1.去除两边的空格   str.strip()
2.去除左边的空格   str.lstrip()
3.去除右边的空格   str.rstrip()
'''
str1 = ' hello '
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

# TODO 字符串分割
'''
# 或者叫字符串转列表

1.按照空格进行分割  str.split()
2.按照指定的分割符进行分割  str.split(分割符)
3.从左按照指定分隔符分割,分割指定的次数,返回一个列表 str.split("分隔符",分割次数) 
4.从右按照指定分隔符分割,分割指定的次数,返回一个列表 str.rsplit("分隔符",分割次数) 

'''

str = 'hello world'
print(str.split())
str1 = 'python,mysql,sql'
print(str1.split(','))

print(str1.split(',', 1))
print(str1.rsplit(',', 1))

# TODO 大小写转换
'''
1.小写转大写  str.upper()
2.大写转小写  str.lower()
3.单词首字母大写  str.title()
'''

str1 = 'hello world'
print(str1.upper())
print(str1.lower())
print(str1.title())

# TODO 判断开头或者结尾的字符
# 判断开始
# str.startswith('开头字符')
# str.endswitch('结束字符')
str1 = 'hello world'
print(str1.startswith('he'))
print(str1.endswith('he'))
print(str1.endswith('d'))

# 举例：判断文件是不是.txt文件
print(str.endswith('.txt'))

# TODO 字符串拼接
'''
字符串拼接    # 也可以叫列表转字符串
string.join(列表)
列表中的元素使用string连接起来
'''
list = ['python', 'mysql', 'hello']
print(','.join(list))  # 以逗号拼接
print(''.join(list))  # 无符号拼接

print('--' * 20)

# TODO 字符串的替换
# 语法: str.replice('原文', '替换文')
str1 = 'my name is lisi'
str2 = str1.replace('lisi', '王五')
print(str2)
print('--' * 20)

# TODO 判断字符串组成
'''
判断字符串由数字组成   str.isdigit()
判断字符串由字母组成   str.isalpha()
判断字符串由字母和数字组成 str.isalnum()  # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
'''
a = '111'
b = 'ab11'
c = 'abc'
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())


print('--' * 20)
# TODO 字符串格式化
'''
%-formatting格式化、str.format方法格式化，以及Python 3.6版本之后支持的f-strings格式化

% 被称为 格式化操作符，专用于处理字符串中的格式，用于零时占位，等待后续的数据替换。
不同类型的数据需要使⽤不同的格式化字符。
%s	转成字符串
%d	转成整数
%f	转成浮点数
%%	输出%
语法：
1. '字符串%s字符串' % 变量1
2. '字符串%s字符串%d' % (变量1, 变量2...)
'''
name = '李四'
age = 20
str = 'my name is %s ,my age is %d岁' % (name, age)
print(str)
address = '成都'
str1 = 'my from  %s' % address
print(str1)

# %f默认占位保存6位小数。如果只想保留指定位数的小数，那么可以使用“%.2f”占位，代表保留两位小数
score = 98.125
str2 = 'my socre is %.2f' % score
print(str2)
'''
format方法格式化
'''
name, age, address = '李四', 20, '成都'
str1 = '姓名：{}, 年龄：{}, 地址：{}'.format(name, age, address)
str1 = '姓名：{2}, 年龄：{1}, 地址：{0}'.format(name, age, address)  # 根据索引传入
str1 = '姓名：{name}, 年龄：{age}, 地址：{address}'.format(name='哈哈', age=20, address='丽江')  # 根据关键字传入
print(str1)

print('--' * 20)

'''
f-string格式化
语法： f'{变量1}字符串{变量2'
'''
name = '张三'
age = 20
print(f'my name is {name},age is {age}')
price = 99.982
print(f'the final price is {price:.2f}')
# {变量: .nf} 其中的n就表示保留的小数的位数, 需要保留几位数, 就将n设置为几即可
