# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 15-私有权限的案例.py
# Time       ：2023/4/18 16:54
# Author     ：ant
# version    ：python 3.11
# Description：
"""


# 在不想属性可以被直接修改，或者数据是固定的。可以使用私有权限设置



class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        if 1 <= age <= 120:
            self.__age = age

    def get_age(self):
        return self.__age


p1 = Person('hallo', 20)
# print(p1.name)

# 修改年龄
# print(p1.__age)    失败

p1.set_age(-21)
print(p1.get_age())
