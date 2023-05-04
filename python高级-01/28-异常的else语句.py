# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 28-异常的else语句.py
# Time       ：2023/4/22 13:46
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
try:
    可能发生异常的代码
except Exception as result:
    发生异常执行的代码
else:
    没有异常的时候执行的代码
"""
"""

try:
    num = int(input('数字:'))
    result = 1/num
except Exception as e:
    print(e)
else:
    print('没问题')
"""

try:
    num = int(input('数字:'))
    result = 1/num
except ZeroDivisionError:
    print('0不能做除数')

else:
    print('成功')
