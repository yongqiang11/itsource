# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_data.py
# Time       ：2023/5/10 10:56
# Author     ：ant
# version    ：python 3.11
# Description：
"""

list1 = {'1': 1, '2': 2}
list2 = list1
list1['1'] = 5
sum1 = list1['1'] + list2['1']
print(sum1)

