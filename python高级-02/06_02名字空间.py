# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06_02名字空间.py
# Time       ：2023/5/9 15:21
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
名字: 变量名, 函数名, 类名
名字空间: 存放变量名, 函数名和类名的地方
名字空间的分类:
    1. 全局名字空间: 在函数外定义的名字,放置在全局名字空间   ----> globals()
    2. 局部名字空间: 在函数内定义的名字,放置在局部名字空间  ---> locals()
    3. 内置名字空间: python内置的名字存放的位置  ---> dir(__builtins__)
名字空间是特定格式, 这个格式就是字典, 其中键就是名,  值就是具体数据
    {键1:值1, 键2:值....}
名字空间的作用:
    1. 在同一个名字空间中, 不允许重名, 如果重名就以最后加载入内存的为主
    2. 在不同的名字空间中, 可以重名
"""

# 定义变量
name = "张三"


# name = "王二麻子"

# 定义函数
def show_me():
    print("我的名字叫小马哥")


# 定义类
class Student:
    # 定义属性
    pass
    # 定义方法
    pass


print(globals())


print('--' * 20)
# 定义一个外函数


def func1():
    name = "李四"

    print(name)  # 在不同的名字空间中, 可以重名

    def inner():
        pass

    print(locals())


# 调用函数
func1()
print(name)

# # 查看内置名字空间
# print(dir(__builtins__))
