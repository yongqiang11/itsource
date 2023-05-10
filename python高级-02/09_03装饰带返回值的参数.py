# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 09_03装饰带返回值的参数.py
# Time       ：2023/5/10 16:16
# Author     ：ant
# version    ：python 3.11
# Description：
"""


# 定义装饰器
def decorator(fn):       # fn : add
    def inner(num1, num2):   # inner = add
        print('正在计算出')
        result = fn(num1, num2)
        print('测试')
        return result


    return inner


# 使用装饰器
@decorator
def add(num1, num2 ):   # add = decorater(add)  inner
    return num1 + num2


if __name__ == '__main__':

    print(add(1, 2))   # add = inner