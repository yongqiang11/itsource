# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06-魔术方法str.py
# Time       ：2023/4/17 16:15
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
魔术方法： __str__
触发：当对象被print打印输出时，触发str执行
作用：打印对象的时候，不是返回对象的内存地址，而是返回对象的标识信息
说明： 
    注意：str方法必须返回字符串类型
"""
# 定义类


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


# 创建对象


p1 = Person('hello', 19)
print(p1)  # 触发str方法执行


p2 = Person('哈哈', 19)
print(p2)  # 触发str方法执行
