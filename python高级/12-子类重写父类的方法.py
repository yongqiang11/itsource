# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 12-子类重写父类的方法.py
# Time       ：2023/4/18 15:08
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
子类重写父类的方法
    子类和父类的方法重名，子类会覆盖父类。也就是使用子类的方法
"""

# 定义一个人类


class Person:
    def __init__(self):
        self.name = 'lisi'
        self.age = 20

    def run(self):
        print('人类跑')
# 定义一个学生类


class Student(Person):

    def __init__(self):
        self.name = 'wangwu'
        self.age = 28

    def run(self):
        print('学生跑')

student = Student()
student.run()

print(student.name)
print(student.age)