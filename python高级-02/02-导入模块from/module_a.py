# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : module_a.py
# Time       ：2023/4/23 10:43
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# 变量
name = 'module_a变量'


# 函数

def fn():
    print('module_a fn函数')


# 类

class Dome:
    def __str__(self):
        return  'module_a的类'


print(__name__)

# 模块中有个魔术变量__all__，其值为列表,可以限定通过 from 模块名 import * 导入的内容

# 注意：列表中写的时资源的字符串名称
__all__ = ['name', 'fn']
