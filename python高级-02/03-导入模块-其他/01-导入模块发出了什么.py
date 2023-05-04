# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-导入模块发出了什么.py
# Time       ：2023/4/23 22:31
# Author     ：ant
# version    ：python 3.11
# Description：
"""

import module_a

print(module_a.name)


# 因为import的功能是  引入模块并执行里面的代码
# 但是实际工作中测试代码应该是单独执行module_a.py文件时才应该执行的，当其他文件引入该模块文件时测试代码不应该执行。
# 为了解决这个问题，可以利用python在执行一个文件时有个魔术变量__name__

