# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 16-变量的作用域.py
# Time       ：2023/4/9 14:59
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
变量作用域：
变量的生效范围
作用域：
    全局作用域：函数外部都是全局作用域
    局部作用域：函数内部就是局部作用域
变量：
    全局变量：全局作用域中定义的变量
        可以在全局作用域中进行修改和访问，只能在局部作用域中访问,不能修改
    局部变量：局部作用域中定义的变量
        只能在局部作用域中进行修改和访问

global关键字:
    将变量声明为全局变量
"""

# 全局变量
num1 = 100


def fn1():
    # 局部变量
    global num1
    num1 = 200


print(num1)

fn1()

print(num1)


def fn2():
    name = 'hello'


fn2()

# print(name)
