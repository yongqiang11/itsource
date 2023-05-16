# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 15-迭代器.py
# Time       ：2023/5/16 15:19
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
容器是一种把多个元素组织在一起的数据结构  元组，列表，字典，集合，字符串
迭代器 对容器进行 迭代 的工具

语法：
    创建迭代器
        迭代器名 = iter(容器名)
    通过next迭代容器中的元素
        next(迭代器名)
"""


# 创建一个列表
list1 = [1, 2, 3]
# 遍历这个列表
# for i in list1:
#     print(i)

# 迭代这个列表 ?
my_iter = iter(list1)
# 使用迭代器
print(next(my_iter))   # 取第一个元素
print('很多行代码后')
print(next(my_iter))   # 取第二个元素
print(next(my_iter))   # 取第三个元素
# print(next(my_iter))   # 取第四个元素     元素取完了，报错StopIteration

# 比如在python中的列表和字典容器，要想获得他里面的数据？
# 一个是通过[]的语法获取其中一个，另外一个就是借助for…in的语法。
# 其实for…in就是一个隐式迭代器的使用方法。
