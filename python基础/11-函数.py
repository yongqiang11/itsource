# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03-函数.py
# Time       ：2023/4/4 17:24
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# TODO 认识函数
'''
# python内置函数
print()  # 输出
len()    # 获取容器的长度
max()    # 获取容器中的最大值
min()    # 获取容器中的最小值

# 自定义函数
封装一个具有独特功能的代码集合，起一个名字。然后就可以重复通过名字调用而实现这个功能了。

# 函数是具有名字的可重复执行的代码块

定义语法：
def 函数名():
    代码块(函数体)

# 定义函数时，函数里面的代码块不会直接执行
# 调用函数时，函数里面的代码块才会执行

# 调用函数
函数名()

'''


def info():
    for i in range(3):
        print(i)


info()

# TODO 参数

'''
说明： 
    定义函数时，传入的参数叫做形式参数：形参
    调用函数时，传入的参数叫做实际参数：实参 
作用：
    让函数通用性更强 
'''
print('--' * 20)


def add(a, b):
    print(a + b)


add(1, 2)
add(3, 4)
print('--' * 20)

# TODO 函数返回
'''
语法：
def 函数名():
    代码块(函数体)
    return 表达式
说明：
1. 函数返回运行结果：return返回表达式运行的结果
2. 返回到函数调用的地方
3. 退出循环：return后面的代码不执行

'''


def add(a, b):
    result = a + b
    return result


def add1(a, b):
    return a + b


def add2(a, b):
    result = a + b
    return result
    print('hello')


print(add(10, 20))
print(add1(11, 22))
print(add2(12, 30))

print('--' * 20)

# TODO 代码块占位符

# if语句
if 1:
    pass

# 循环语句
# 函数定义
'''
pass是一个空的语句. 不做任何 事情，一般用做占位语句。是为了保持程序结构的完整性


在写代码的过程中为了程序的完整性从而不报错的一种临时写法. 
if True:
    pass

'''


