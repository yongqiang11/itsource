# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 09_02装饰器带参数的函数.py
# Time       ：2023/5/10 15:46
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# 如果装饰的函数有多个参数，也将参数赋给inner 和 fn
"""
使用装饰器实现
# 正在计算中 
# 求2个数的和
"""


# 定义装饰器
def decorator(fn):
    def inner(num3, num4):
        print('正在计算中')
        fn(num3, num4)
    return inner


# 使用装饰器
@decorator
def add(num1, num2):   # add = decorater(add)  inner
    print(num1 + num2)


# 调用
add(1, 2)

