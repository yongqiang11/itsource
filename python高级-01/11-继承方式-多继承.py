# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 11-继承方式-多继承.py
# Time       ：2023/4/18 14:55
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 一个子类继承多个父类

# C继承了A类和B类
class A:

    def infoa(self):
        print('a')

class B:

    def infob(self):
        print('b')

class C(A, B):
    pass


c = C()
c.infoa()
c.infob()