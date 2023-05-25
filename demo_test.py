# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : demo_test.py
# Time       ：2023/5/23 8:51
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import random


def fun1():
    def fun2():
        print('测试')
    return fun2


fun = fun1()
fun()

# 过程： fun()-->fun1()()-->return fun2-->fun2()--> print('测试')

print('--' * 20)


def outer(multiplier=1):

    def inner(num):
        return num * multiplier
    return inner


double = outer(2)
print(double(3))


# 执行过程：outer(2)-->return inner --> inner(3)-->return num * multiplier

print('--' * 20)

"""
包含外函数和内函数
外函数包含内函数
内函数引用外函数的局部变量
外函数返回内函数的引用
"""


def one_floor():
    a = 78

    def inner(num):
        return num + a
    return inner


fo = one_floor()
print(fo(4))


print('---' * 20)

# 任意取4个数
str = 'DSEW3HDKJOEWOJWE344'
st1 = random.sample(str, 4)
st2 = ''.join(st1)
print(st2)