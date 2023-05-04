# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 13-子类调用父类重名的方法.py
# Time       ：2023/4/18 15:20
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
super()
"""


# 定义一个人类

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print('人类干活')

class Student(Person):

    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def work(self):
        super().work()    # 简单写法(一般用这种)
        super(Student, self).work()  # 传统写法
        print('学生干活')


student = Student('hehe', 19, 200)
print(student.name)
print(student.age)
print(student.number)
student.work()



