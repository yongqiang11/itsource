# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-函数加强.py
# Time       ：2023/4/7 16:41
# Author     ：ant
# version    ：python 3.11
# Description：
"""


# TODO 函数注释

def info(a, b):
    """

    :param a:
    :param b:
    :return:
    """

    return a + b


print(help(info))  # help查看函数的说明文档

print('--' * 20)

# TODO 函数加强
'''
定义函数-参数
1.必填参数(必须参数)
    # 必填参数-必须要传入必填的实参
2.默认参数
    # 带有默认值的参数就是默认参数

说明:
    必填参数放在默认参数的前面
'''


#  TODO 必填参数


def fn(a, b):
    print(a, b)


fn(1, 2)


# TODO 默认参数
# class_name就是默认参数
def fn2(name, age, class_name=1010):
    """

    :param name:姓名
    :param age:年龄
    :param class_name:班级名称
    :return:
    """
    print(name, age, class_name)


# fn2('李四', 18, 1010)
# fn2('王五', 20, 1010)
# fn2('小二', 17, 1010)


fn2('李四', 18)
fn2('王五', 20)
fn2('小二', 17)
fn2('小二', 17, 1111)

# TODO 调用函数
'''
位置参数：根据参数位置进行传参
关键字参数:根据形参的名字进行传参
'''

# 位置参数
fn(1, 2)
fn(2, 1)
# 关键字参数
fn(a=100, b=10)
fn(b=200, a=100)

