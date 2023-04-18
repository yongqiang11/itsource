# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 14-私有权限.py
# Time       ：2023/4/18 16:20
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
私有成员：具有私有权限的成员
成员：属性和方法
私有权限只有在类的内部访问

私有属性：在属性名的前面加上__ 就是私有属性
私有方法：在方法名的前面加上__ 就是私有方法
"""


class Person:
    def __init__(self, name, age):
        self.__name = name   # 私有属性
        self.age = age

    # 私有方法
    def __info(self):
        print('haha')

    def run(self):
        print(f'{self.__name}跑起来')

class Student(Person):
    def get(self):
        print(self.age)
        print(self.__name)

"""

p = Person('李四', 20)
p.run()

# TODO 在类的外部访问私有属性和方法
print(p.age)
# print(p.__name)  # 在类的外部访问私有属性
p.__info()   # 在类的外部访问私有方法
"""

# TODO 在派生类中访问私有属性和方法

s = Student('hello', 20)
s.get()