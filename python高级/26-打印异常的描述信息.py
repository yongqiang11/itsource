# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 26-打印异常的描述信息.py
# Time       ：2023/4/22 9:19
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...) as 变量:
    捕获异常执行的代码
    print(变量)
"""
"""
try:
    num = int(input('数字:'))
    result = 1/num
except(ValueError, ZeroDivisionError) as e:
    print(e)
"""

try:
    num = int(input('数字:'))
    result = 1/num
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
