# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 16-python中的权限不强制(了解).py
# Time       ：2023/4/19 14:19
# Author     ：ant
# version    ：python 3.11
# Description：
"""


class Person:
    def __init__(self):
        self.name = 'hello'

    def __infoa(self):
        print('info')


# 通过特殊的方式可以在类的外部访问私有成员
# 语法：_类名__成员名
p1 = Person()
print(p1._Person__name)
p1._Person__infoa()



