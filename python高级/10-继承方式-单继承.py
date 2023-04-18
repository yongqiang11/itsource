# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 10-继承方式-单继承.py
# Time       ：2023/4/18 14:44
# Author     ：ant
# version    ：python 3.11
# Description：
"""

#  单继承：一个子类继承一个父类

# 父类
class  Staff:
    def __init__(self):
        self.name = 'hello'
        self.age = 20

    def eat(self):
        print(f'{self.name}吃东西')

# 子类


class Teacher(Staff):
    pass


teacher = Teacher()
print(teacher.name)
print(teacher.age)
teacher.eat()