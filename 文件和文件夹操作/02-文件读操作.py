# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-文件读操作.py
# Time       ：2023/4/11 14:21
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO f.read() 一次性读取所有内容
'''
f.read(n=-1)
n=-1 默认值，一次性读取所有内容
n=正整数
    1.文本操作：按照字符个数进行操作，不区分字母和汉字
    2.二进制操作；按照字节大小进行操作， 1汉字=3Byte
'''
f = open('demo.txt', 'r', encoding='utf8')
content = f.read()
print(content)
f.close()

# TODO 文本操作

f = open('demo.txt', 'r', encoding='utf8')
content = f.read(-1)
print(content)
f.close()

f = open('demo.txt', 'r', encoding='utf8')
content = f.read(3)
print(content)
f.close()
print('--' * 20)
# TODO 二进制操作

# 注意：如果是二进制模式就不需要加字符集
f = open('demo.txt', 'rb')
content = f.read(3)
print(content)
f.close()

# 将bytes型转成字符串类型 bytes.decode()
print(type(content))
byte = content.decode()
print(byte)
print(type(byte))
print('--' * 20)
# 将字符串类型转成bytes型 str.encode()
print(byte.encode())

print('--' * 20)
# TODO f.readline()
# 一行一行读取数据

f = open('demo.txt', encoding='utf8')
line = f.readline()
print(line, end=' ')
line = f.readline()
print(line, end='')
f.close()

print('--' * 20)
# 需求：一行一行全部读取所有的信息

f = open('demo.txt', encoding='utf8')
while True:
    line = f.readline()
    print(line, end='')
    if not line:
        break

f.close()
print()
print('--' * 20)

# TODO f.readlines()
# 一次性读取都有的行，返回列表，会把每一行的内容，放在列表中
f = open('demo.txt', encoding='utf8')
# content = f.readlines()
# print(content)
# f.close()

# 以上代码会在打印出现\n换行符


data = f.read().splitlines()    # 按照行('\r', '\r\n', \n')分隔字符串，返回一个包含各行作为元素的列表
print(data)
f.close()

