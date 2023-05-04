# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 08-文件操作封装.py
# Time       ：2023/4/17 17:32
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
类：File
属性： f 打开的文件资源句柄
方法: read
     write
"""


class File:
    def __init__(self, filename, mode, encoding=None):
        self.f = open(filename, mode, encoding=encoding)

    def read(self):
        return self.f.read()

    def write(self, content):
        self.f.write(content)

    def seek(self, size=0):
        self.f.seek(size)

    def __del__(self):
        self.f.close()
# 创建对象


p1 = File('demo.txt', 'w+', 'utf8')
# 调用写方法
p1.write('1234\n3333777')

p1.seek()
print(p1.read())


