# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_data.py
# Time       ：2023/5/10 10:56
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import datetime


# 装饰器


# 定义装饰器

def fun2(fn):
    def inner():
        print('前置')
        fn()
        print('后置')

    return inner


# @fun2
def fun1():
    print('哈哈哈')



fun1()