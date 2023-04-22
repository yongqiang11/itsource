# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 27-捕获所有异常.py
# Time       ：2023/4/22 9:29
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 第一种[常用]
"""
try:
    可能发生异常的代码
except Exception as result:
    print(result)
"""

try:
    num = int(input('数字:'))
    result = 1/num
except Exception as e:
    print(e)

# TODO 第二种 不推荐使用
"""

try:
    num = int(input('数字:'))
    result = 1/num
except:
    print('Fail')
"""