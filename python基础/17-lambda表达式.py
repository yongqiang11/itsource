# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 17-lambda表达式.py
# Time       ：2023/4/10 14:02
# Author     ：ant
# version    ：python 3.11
# Description：
"""
'''
匿名函数：
    lambda表达式
语法：
    lambda [参数列表]:表达式
特点：
    lambda会把执行的结果返回
'''
# 需求：求2数之和


def fn(x, y):
    return x + y


print(fn(1, 2))

# 第一种
# 定义
add = lambda x, y: x + y
# 调用
print(add(1, 3))

# 第二种  自调用
result = (lambda x, y: x + y)(2, 3)
print(result)


# 需求：求2个数的和
def fn1(x, y):
    return x + y

# 练习
print((lambda: 1 + 1)())
print('==' * 20)


# 案例
def operation(a, b, operator):  # a = 1 b = 2 operator:add
    """
    求2个数的运算结果
    :param a: int 第一个数
    :param b: int 第二个数
    :param operator: 运算的函数
    :return: 运算结果
    """
    return operator(a, b)


def add(a, b):
    return a + b


def dec(a, b):
    return a - b


print(operation(1, 2, add))
print(operation(3, 1, dec))

operation(1, 2, lambda a, b: a * b)
# 函数：函数带名字的代码块
# 变量：数据的名字
# 函数可以作为参数使用，也可以作为函数返回值使用
