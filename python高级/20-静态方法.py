# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20-静态方法.py
# Time       ：2023/4/19 16:54
# Author     ：ant
# version    ：python 3.11
# Description：
"""


class Person:
    @staticmethod
    def info():
        print('hehe')


# 类调用   一般用这种
Person.info()

# 对象调用
p1 = Person()
p1.info()

"""

方法选择：
1.如果你不知道用什么方法，你就直接用对象方法
2.如果一个方法中，要使用对象属性，那么就定义为对象方法
3.如果一个方法中，要使用类属性，那么就定义为类方法
4.如果一个方法中，既没有使用类属性，也没有使用对象属性，那么就可以定位静态方法

"""