# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 24-捕获单个指定异常.py
# Time       ：2023/4/21 15:47
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
语法：

try:
    可能发生异常的代码
except 异常的类型：
    捕获到异常执行代码
"""

# 捕获成功
try:
    result = 1/0
except ZeroDivisionError:
    print('0不能做除数')

print(1111)

print('--' * 20)
# 捕获失败
# try:
#     result = 1/0
# except NameError:
#     print('0不能做除数')
#
# print(1111)

# 没有异常

try:
    result = 1/1
except ZeroDivisionError:
    print('0不能做除数')

print(1111)