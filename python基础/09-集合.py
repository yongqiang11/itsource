# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 07-集合.py
# Time       ：2023/3/21 14:35
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO  集合的定义

# 一般方式
set1 = {}  # 这种情况下是错误的，空的{},表示字典
print(type(set1))

set2 = {'python', 'linux', 'mysql'}
print(type(set2))
# 函数方式
# set3 = set()
set4 = set('hello')
set5 = set(['python', 'linux', 'mysql'])
set6 = set(('python', 'linux', 'mysql'))
print(set3, set4, set5, set6)

# 特点：
# 1.字典是无序的,没有索引
# 2.集合的元素是唯一的,去重

# TODO 集合操作
print(set4.pop())
set4.add('git')
print(set4)
