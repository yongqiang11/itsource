# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03-文件写操作.py
# Time       ：2023/4/11 20:55
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# TODO write()
# 说明：一次写入一个内容
f = open('demo2.txt', 'w', encoding='utf8')
f.write('hello')
f.close()


# TODO wirtelines([xx, xx])
# 说明：一次写入多个内容

f = open('demo3.txt', 'w', encoding='utf8')
# f.writelines(['111', 'hello', 'test'])
f.writelines(['111\n', 'hello\n', 'test\n'])
f.close()
