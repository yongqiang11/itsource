# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 09-装饰器基础.py
# Time       ：2023/5/5 15:53
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
在不改变原有函数的基础上，增加额外的功能，它本质上就是一个闭包函数。
"""


# def fn1():
#     # 开始时间
#     print('fn1')
#     # 结束时间
#     # 结果 = 结束时间 - 开始时间
#
#
# def fn2():
#     # 开始时间
#     print('fn2')
#     # 结束时间
#     # 结果 = 结束时间 - 开始时间

# 定义装饰器
# fn1是被装饰的函数

def wrapper(fn):
    def inner():
        print('前置拓展')
        fn()
        print('后置拓展')
    return inner


# 使用装饰器
fn1 = wrapper(fn1)
fn1()

# fn2 = wrapper(fn2)
# fn2()