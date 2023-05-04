# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-导入多个指定模块.py
# Time       ：2023/4/23 11:16
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
导入多个指定模块
import  模块名1， 模块名2， 模块名3
"""

# 导入模块

import module_a, module_b

print(module_a.name)
print(module_b.name)

module_a.fn()
module_b.fn()

print(module_a.Dome())
print(module_b.Dome())
