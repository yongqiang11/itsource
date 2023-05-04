# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-对象属性-类的外部.py
# Time       ：2023/4/14 15:40
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 定义类


class Person:
    pass

# 创建对象


p1 = Person()

# TODO 设置属性
# 语法： obj.属性名 = value
p1.name = '测试'
p1.age = 19

# TODO 查看属性(使用属性)
# 语法：obj.属性名
print(p1.age)
print(p1.name)

# TODO 修改属性
# 语法： obj.属性名 = new_value
p1.name = '哈哈'
print(p1.name)

# TODO 删除属性
# 语法： del obj.属性名
del p1.name
print(p1.name)
