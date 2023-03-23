# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 05-元组.py
# Time       ：2023/3/19 15:54
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 认识元组
'''
1. 简单方式
    tuple = ()
    tuple = (1, 2, True, 'abc', ['abc', 'we'])
2. 函数形式
    tuple = tuple()
# 元组的特点：
    1.可以存放任何数据
    2.元组也是有序的，可以使用索引下标获取
    3.通过切片获取新的元组,和列表相同
    4.元组不可以修改(和列表的区别)
'''
t1 = ('hello')    # 这种不是元组，
# 注意： 只有一个元素时，都要都逗号，否则就是字符串
t1 = ('hello')
print(type(tuple))
t2 = ('hello',)
print(type(t2))

print('==' * 20)

tuple1 = tuple('hello')
print(tuple1)
tuple2 = tuple(['abc', 2, 3])
print(tuple2)

# TODO  元组-索引/切片
tuple = (1, 2, True, 'abc', ['abc', 'we'])
# 索引下标
print(tuple[2])
# 切片   取 True, 'abc'
print(tuple[2:4])
print('==' * 20)
# TODO 元组不能被修改
tuple = (1, 2, True, 'abc', ['abc', 'we'])
# tuple[0] = 2
# print(tuple)  TypeError: 'tuple' object does not support item assignment

# 得到列表之后 ，就可以修改元组中的数据
tuple[-1][0] = 'hello'
print(tuple)
print('=='* 20 )

# TODO 元组拆包

tuple1 = (1, 'abc', ['abc', 'we'])
# 拆包
num1, str, list1 = tuple1
print(num1)
print(list)

# 列表拆包
info = ['abc', 'we']
num1, letter = info
print(letter)

# 注意元素的个数和元素个数一一对应
print('==' * 20)

# 元组遍历
tuple1 = (1, 'abc', ['abc', 'we'])
for i in tuple1:
    print(i)

# 元组查询
tuple1 = (1, 'abc', ['abc', 'abc'], 1)

print(tuple1.count(1))

print(dir(()))  # dir()查询对象的属性和方法
print(dir([]))  # dir()查询对象的属性和方法