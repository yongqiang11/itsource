# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 07-魔术方法del.py
# Time       ：2023/4/17 16:44
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
魔术方法： __del__
触发：当对象被销毁时，del方法会自动执行
作用：当对象在销毁之前，做一些收尾的工作。
说明：
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def  __del__(self):
        print('del执行')


# 创建对象


p1 = Person('hello', 19)
# del p1


