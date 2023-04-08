# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-输入和输出.py
# Time       ：2023/3/17 11:04
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 输入input
# 语法： input('输入的时候的提示信息')

'''
input()函数使用规则 ：
- 等待输入，不输入就一直等待
- 用户的输入是以一个回车符结束
- 用户的输入作为返回值，给程序后面使用
- 返回都是字符串
'''

# 输出print
'''
语法：
print()
print(数据1, 数据2, 数据3)
print(数据, end="")  # 下一个print不换行，接着输出
print(数据1, 数据2, sep="")  # 自定义数据隔开的符号
'''

print(1, 2, 3 )
print(123, end='')
print(222)
print(123, 234, sep='@')
