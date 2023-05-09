# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06_04变量的使用顺序.py
# Time       ：2023/5/9 16:09
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
    变量的使用顺序: 称为变量的查找顺序
语法:
    局部变量 ---> 闭包变量  ---> 全局变量 ---> 内置变量 ---> name is not defind
"""

name = "曹操"   # 全局变量

def func1():
    # name = "刘备"   # 闭包变量
    def inner():
        pass
        # name = "张飞"  # 局部变量
        print(name)
    inner()
    # print(name)

# print(name)
func1()

