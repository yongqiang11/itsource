# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 30-异常处理案例.py
# Time       ：2023/4/22 13:57
# Author     ：ant
# version    ：python 3.11
# Description：
"""

filename = input('输入文件名:')
try:
    f = open(filename, 'r', encoding='utf8')

except FileNotFoundError:
    f = open(filename, 'w', encoding='utf8')
    f.write('hello\n12345')
else:
    print(f.read())

finally:
    f.close()

