# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 08-闭包.py
# Time       ：2023/5/5 15:53
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
1. 在函数嵌套(函数里面再定义函数)的前提下
2. 内部函数使用了外部函数的变量(还包括外部函数的参数)
3. 外部函数返回了内部函数

函数可以当作参数被传入，也可以当作返回值被返回
"""


def wrapper():
    num = 100

    def inner():
        print(num)

    return inner


fn = wrapper()
fn()


def wrapper2(num):
    def inner():
        print(num)

    return inner


# 闭包的作用
"""
一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。
但是闭包是一种特殊情况，
如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
就把这个临时变量绑定给了内部函数，然后自己再结束。
"""