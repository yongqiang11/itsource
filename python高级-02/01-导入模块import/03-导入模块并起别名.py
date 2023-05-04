# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03-导入模块并起别名.py
# Time       ：2023/4/23 11:24
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
# 导入模块并起别名
import 模块名1 [as 模块1别名], 模块名2 [as 模块2别名,] ...

# 起别名的作用:
# 简化模块名
# 防止名字冲突
"""

import module_a as m1, module_b as m2

print(m1.name)
print(m2.name)

m1.fn()
m2.fn()

print(m1.Dome())
print(m2.Dome())
