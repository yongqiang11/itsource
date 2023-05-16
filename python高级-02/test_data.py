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


a = 1
b = 2
c = (3, 5)

# 装包

tuple1 = a, b, *c
print(type(tuple1))
print(tuple1)
list2 = list(tuple1)
print(list2)

set1 = set(tuple1)
print(set1)
print(type(set1))
#
# dict1 = dict(tuple1)
# print(dict1)
# print(type(dict1))

print('==' * 20)
list1 = [1, 2, 3, 4]
c, d, *e = list1
print(c, d, e)
