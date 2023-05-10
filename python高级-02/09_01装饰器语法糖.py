# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 09_01装饰器语法糖.py
# Time       ：2023/5/10 14:56
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""

语法糖: 本身不会改变什么,只是让人类觉得代码更'甜蜜', 方便人类阅读

语法:
编写装饰器函数
        def 装饰器函数名(形参):
            def 内函数名():
                # 需要增加的功能代码块
                形参()  # 表示原函数在此处的调用
                # 需要增加的功能代码块
            return  内函数名
编写原函数
        @装饰器函数名       
        def 原函数():
            # 函数体
"""


# 定义装饰器函数
def zhuangxiu(function):
    def inner():
        print(1)  # 属于我新增的代码块
        print(2)
        function()  # 调用原函数
        print(3)
        print(4)

    return inner


# 定义原函数
@zhuangxiu
def longhu():
    print("这是毛坯房!")


"""几行代码就等于 longhu = zhuangxiu(longhu)"""


@zhuangxiu
def wangda():
    print("这个万达的毛坯房! ")


# 查看
longhu()
print('--' * 20)
wangda()
