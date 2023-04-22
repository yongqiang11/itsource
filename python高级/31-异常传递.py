# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 31-异常传递.py
# Time       ：2023/4/22 20:58
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 函数嵌套
"""
def fn1():
    result = 1/0

def fn2():
    fn1()

def fn3():
    fn2()


try:
    fn3()
except ZeroDivisionError:
    print('Zore Fail')

"""

# 可以在fn3() 调用的时候抛出异常，也可以在任何函数下抛出异常

# 异常语句嵌套
try:
    try:
        try:
            result = 1/0
        except ValueError as e:
            print(e)
    except NameError as e:
        print(e)
except ZeroDivisionError as e:
    print(e)
