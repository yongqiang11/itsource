# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 17-受保护权限.py
# Time       ：2023/4/19 14:57
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
python中没有严格的受保护权限
语法： _成员名
特点： 只能在类的内部个派生类中访问
"""


class Person:
    def __init__(self):
        self.name = 'hello'


print(Person().name)
