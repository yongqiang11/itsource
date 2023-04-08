# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06-参数拆包.py
# Time       ：2023/4/7 21:21
# Author     ：ant
# version    ：python 3.11
# Description：
"""


def fn1(a, b, c):
    print(a, b, c)


list1 = [1, 2, 3]
fn1(list1[0], list1[1], list1[2])

# 拆包  列表 元组
fn1(*list1)

tuple1 = (1, 2, 3)
fn1(*tuple1)
print('==' * 20)

# 字典 拆包
dict1 = {'a': 1, 'b': 2, 'c': 3}
fn1(**dict1)
