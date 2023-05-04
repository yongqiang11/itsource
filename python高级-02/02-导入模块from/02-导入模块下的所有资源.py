# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-导入模块下的所有资源.py
# Time       ：2023/4/23 15:33
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
# 导入模块下的所有资源
from 模块名 import *
"""

from module_a import *

print(name)
fn()
# print(Demo())  # 因为 module_a中__all__没有指定Demo，所以没有被导入
