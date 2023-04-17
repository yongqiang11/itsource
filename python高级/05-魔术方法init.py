 # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 05-魔术方法init.py
# Time       ：2023/4/17 14:29
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
魔术方法： __init__
触发：当对象创建之后，init方法会自动执行
作用：初始化对象属性
说明： 以后对象属性的初始化，都在init方法中设置
"""

# 定义类


class Person:
    def __init__(self, name, age):
        print('hello')
        self.name = name
        self.age = age

# 实例化对象


p1 = Person('lisi', 20)   # 人的实例
print(p1.name)
print(p1.age)

p2 = Person(name='haha', age=90)
print(p2.name)
print(p2.age)


