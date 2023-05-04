# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 29-异常finally.py
# Time       ：2023/4/22 13:51
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
# 异常的完整格式
try:
    可能发生异常的代码
except 异常类型:
    捕获异常执行的代码
except 异常类型:
    捕获异常执行的代码
else:
    没有异常的时候执行的代码
finally:
    无论是否异常都要执行的代码
"""


try:
    num = int(input('数字:'))
    result = 1/num
except ValueError:
    print('只能输入数字')
except ZeroDivisionError:
    print('0不能做除数')

else:
    print('成功')
finally:
    print('finally')