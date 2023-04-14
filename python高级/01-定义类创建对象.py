# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-定义类创建对象.py
# Time       ：2023/4/14 15:17
# Author     ：ant
# version    ：python 3.11
# Description：
"""

'''
语法：
class 类名:
    pass
    
类名：
    遵循标识符的命名规则
    类名一般使用大驼峰命名法 

类和对象的关系
    先创建类，通过类创建对象
    
语法：
类名()
说明：
    创建(实例化)了一个类的实例(对象)
    
一个类可以创建多个对象,对象之间是隔离的。
'''

# 定义类


class Person:
    pass


# 创建对象

p1 = Person()
print(p1)   # <__main__.Person object at 0x000002637D9C0990> 0x000002637D9C0990为十六位内存地址

print(id(p1))  # 打印出10进制内存地址
# 10进制转16进制
print(hex(id(p1)))

#  打印出的对象只要是 <> ，就是一个对象


# 创建多个对象

p2 = Person()
print(p2)

p3 = Person()
print(p3)
