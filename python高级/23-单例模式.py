# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 23-单例模式.py
# Time       ：2023/4/21 14:05
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
单例模式：
    一个类只能创建一个对象
"""


class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return  cls.__instance


d1 = Singleton()
d2 = Singleton()
d3 = Singleton()
d4 = Singleton()
d5 = Singleton()

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
