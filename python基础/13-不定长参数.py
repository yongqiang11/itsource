# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 05-不定长参数.py
# Time       ：2023/4/7 16:43
# Author     ：ant
# version    ：python 3.11
# Description：
"""
'''
不定长参数(万能参数)：
    可以传入任意多个参数
不定长参数的分类：
    位置不定长：可以接收多个任意位置参数，会以元组类型将所有的参数打包在args变量中
    关键字不定长：可以接收多个任意关键字参数，会以字典类型将所有的参数打包在 kwagrs 变量中
'''

# TODO 位置不定长


def fn(*args):
    print(args)


fn('a', 122, 3, ['a', 'hell', '123'])
# TODO 关键字不定长


def fn1(**kwargs):
    print(kwargs)


fn1(name='lisi', age=12, class_name='测试')


# 混合使用


def fn3(*args, **kwargs):
    print(args)
    print(kwargs)


fn3(1, 2, 3, a=200, b=300)


print('--' * 20)
# 必填参数 默认参数 位置不定长 关键字不定长
# 顺序：必填参数> args  > 默认参数 > kwargs


def fn4(a, *args, b=10, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)


# fn4(2, 20, 22, name=12, age=10)
fn4(1, 2, 6)


def fn5(a, b, c=100):
    print(a, b, c)


fn5(1, 2, 3)
fn5(1, 2, c=3)
print('==' * 20)


def fn6(a, b=2, c=3):
    print(a, b, c)


fn6(1, c=33)


