# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 25-捕获多个指定异常.py
# Time       ：2023/4/22 8:56
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 第一种
"""
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...):
    捕获异常执行的代码
"""
"""
try:
    num = int(input('数字:'))
    result = 1/num
except(ValueError, ZeroDivisionError):
    print('输入错误')
"""


# TODO 第二种
"""
try:
    可能发生异常的代码
except 异常类型1:
    捕获类型1,执行的代码
except 异常类型2:
    捕获类型2,执行的代码
except ...:
    pass
"""


try:
    num = int(input('数字:'))
    result = 1/num
except ValueError:
    print('输入的不是数字')
except ZeroDivisionError:
    print('0不能作为除数')