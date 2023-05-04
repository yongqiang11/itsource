# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 22-魔术方法new.py
# Time       ：2023/4/20 17:32
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
魔术方法： __new__
概念:
    __new__: 在实例化对象的时候被触发
        干了什么事情?
            1. 触发的时候创建了一个对象   ----> super().__new__(cls)
            2. 将这个对象以self的形式给到__init__

    __init__: 在实例化对象的时候被触发, 触发后可以给对象赋予属性

"""


# 创建一个学生类
class Student(object):

    # 1. 创建一个对象
    # 2. 将这个对象以self的形式给到下一个流程的__init__
    def __new__(cls, *args, **kwargs):
        object = super().__new__(cls)  # 创建对象的代码
        print("**********", object)
        return object

    # 给对象赋予属性
    def __init__(self):
        print("---------", self)
        pass

# 实例化对象
s1 = Student()
s2 = Student()

# 查看对象
print(s1)
print(s2)
