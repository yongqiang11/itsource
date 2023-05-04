# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-导入单个指定模块.py
# Time       ：2023/4/23 10:47
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
# 导入单个指定模块
import 模块名
说明: 模块名就是没有后缀的文件名字
导入模块的目的： 导入模块之后可以使用模块中的资源
资源： 变量，函数，类
"""

# 导入module_a模块
import  module_a

print(module_a.name)

module_a.fn()
print(module_a.Dome())