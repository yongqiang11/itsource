# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : python基础.py
# Time       ：2023/3/17 11:15
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 定义变量   语法：变量名 = 变量值(数据)
variable = 'xixi'

# 查看变量的数据的内存地址    语法：id(变量名)

print(id(variable))

# 删除变量  语法：del python基础
# del variable
# print(variable)


# 变量的其他用法

'''
多个值赋值给多个变量  a, b, c = 1, 2, 3
交换变量的值  a, b = b, a
多个变量赋相同的值  a = b = c = 10
'''
a = 1
b = 2
a, b = b, a
print(a, b)
