# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-文件的追加模式.py
# Time       ：2023/4/11 21:19
# Author     ：ant
# version    ：python 3.11
# Description：
"""
'''

文件操作模式：
r(read): 读操作
w(write)：覆盖写，文件不存在创建
a(append): 追加写，文件不存在创建

b(binary): 二进制模式，不能单独使用。必须配合读写模式
+：扩展模式，不能单独使用。
'''
# a模式

# f = open('demo3.txt', 'a', encoding='utf8')
# f.write('world')
# f.close()

# b模式
f = open('demo3.txt', 'ab')
byte_str = '555'.encode()
f.write(byte_str)
f.close()

# + 模式
'''
f = open('demo3.txt', 'r+', encoding='utf8')
# 读取数据
content = f.read()
print(content)
# 写入数据
f.write('\n6666')

f.close()
'''
'''
f = open('demo3.txt', 'w+', encoding='utf8')
# 读取数据
content = f.read()
print(content)         # 打印出来会为空，因为目前的光标在最后
# 写入数据
f.write('6666')
f.close()
'''

'''
f = open('demo3.txt', 'a+', encoding='utf8')
# 读取数据
content = f.read()
print(content)         # 打印出来会为空，因为目前的光标在最后
# 写入数据
f.write('6666')
f.close()
'''

f = open('demo5.txt', 'w+', encoding='utf8')
# 操作文件
# 写入内容
f.write('你好')

# 移动光标
# 语法：f.seek(size)  size:距离左边的字节大小  0表示最左边
f.seek(3)

# 读取内容
content = f.read()
print(content)

# 关闭文件
f.close()