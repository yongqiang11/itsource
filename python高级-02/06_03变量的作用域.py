# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06_03变量的作用域.py
# Time       ：2023/5/9 16:08
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
变量的作用域: 变量的使用范围

作用域的分类:
    1. 全局变量: 在函数外定义的变量,称为全局变量  --->  在代码的任意位置被使用
    2. 局部变量: 在函数内定义的变量,称为局部变量  --->  在当前函数的内部被使用
    3. 闭包变量: 一定是外函数里嵌套着内函数, 在外函数的内部,内函数的外部定义的变量, 称为闭包变量

局部变量转换成全局变量   ---> 关键字 global
局部变量转换成闭包变量   ---> 关键字 nonlocal

"""
# name = "曹操"  # 全局变量
#
# def show_me():
#     global name
#     name = "刘备"  # 局部变量 转换成 全局变量
#     print(name)
#
# print(name)
# show_me()
# print(name)

# name = "曹操" # 全局变量
#
# def func1():
#     name = "刘备"   # 闭包变量
#     def inner():
#         name = "张飞"  # 局部变量
#         print(name)
#     inner()
#     print(name)
#
# print(name)
# func1()

name = "曹操" # 全局变量

def func1():
    name = "刘备"   # 闭包变量
    def inner():
        nonlocal name
        name = "张飞"  # 局部变量转换成了闭包变量
        print(name)
    inner()
    print(name)

print(name)
func1()