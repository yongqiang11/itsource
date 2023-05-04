# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 18-获取对象类型.py
# Time       ：2023/4/19 15:10
# Author     ：ant
# version    ：python 3.11
# Description：
"""


class Dome:
    def info(self):
        pass


class Dome2:
    def info1(self):
        pass


d1 = Dome()

# TODO type 获取对象的类型

print(type('qwe'))
print(type(d1))

print('--' * 20)

# TODO dir   查看对象的所有成员

print(dir('qwe'))
print(dir(d1))

print('--' * 20)

# TODO isinstance(obj, class) 判断对象是某个类的实例
print(isinstance(d1, Dome))
print(isinstance(d1, Dome2))
print(isinstance('hello', str))
print(isinstance([], list))
