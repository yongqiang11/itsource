# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-导入模块下的指定资源.py
# Time       ：2023/4/23 15:26
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
# 导入模块下的指定资源
from 模块名 import 资源名1 [as 别名], 资源名2, ...
"""

# 不仅可以引入函数，还可以引入一些全局变量、类等

# 导入module_a模块下的fn函数和类

from module_a import fn, Dome

fn()
print(Dome())
