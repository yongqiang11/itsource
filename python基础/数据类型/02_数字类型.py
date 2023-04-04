# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02_数字类型.py
# Time       ：2023/3/17 16:21
# Author     ：ant
# version    ：python 3.11
# Description：
"""
'''
数字类型主要用于支持数学计算，包括整型（int）、浮点型（float）、布尔值（boolean）、复数（complex）。
Python 3中的int同时代表普通整型和长整型，float同时代表单精度和双精度浮点型。
Python中的int和float两种类型没有长度限制，其最大可支持的长度取决于运行的内存情况
'''
'''
boolean类型在什么情况下出现
1.直接赋值
2.逻辑运算,比较运算等操作的结果都是一个bool类型的值 
'''
flag = True  # 直接赋值
print(1 < 3)  # false 比较运算的返回值

