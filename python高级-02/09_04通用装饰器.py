# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 09_04通用装饰器.py
# Time       ：2023/5/10 17:45
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 求2个数的和
# 求3个数的和
# 求4个数的和


# 定义装饰器
def decorator(fn):
    def inner(*args, **kwargs):
        # 前置条件
        print('计算结果为.....')
        result  = fn(*args, **kwargs)
        # 后置
        return result
    return inner


# 调用装饰器
@decorator
def fn1(num1, num2):
    return  num1 + num2


@decorator
def fn2(num1, num2, num3, a, b):
    return  num1 + num2 + num3 + a + b


if __name__ == '__main__':
    print(fn1(1, 2))
    print(fn2(1, 2, 3, 4, b=5))