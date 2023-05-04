# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 19-类成员.py
# Time       ：2023/4/19 15:46
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 类属性

"""
语法：
class 类名：
    属性名 = 属性值
说明：
类属性属于整个类，包括这个类的所有实例

"""


class Person:
    # 类属性
    country = '中国'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 类的外部
# 获取类属性
print(Person.country)

p1 = Person('he', 10)
print(p1.country)

# 修改类属性
# 语法： 类名.类属性名 = 新属性值
Person.country = '美国'
print(Person.country)
print('--' * 20)

p1.country = 'xxx'
print(p1.country)
print(Person.country)

# 删除类属性    # 一般没有这种需求
# del Person.country
# print(Person.country)

print('--' * 20)

# TODO 类方法
"""
语法：
class 类名:
    @classmethod   # 装饰器
    def info(cls):
        pass
        
调用：
    类名.类方法名()  # 一般用这种
    对象名.类方法名()
说明：
@classmethod   # 装饰器
cls:当前类
"""


# 类方法
class Person:
    country = 'china'
    @classmethod
    def info(cls):
        print(cls)
        print('hello')
        print(cls.country)


# 类方法调用
Person.info()
# print(Person)
# Person().info()