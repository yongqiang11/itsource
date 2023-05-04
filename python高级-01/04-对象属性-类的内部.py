# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-对象属性-类的内部.py
# Time       ：2023/4/17 13:59
# Author     ：ant
# version    ：python 3.11
# Description：
"""


class Person:
    def fn1(self, name):
        # 设置属性
        self.name = name

    def fn2(self, name):
        # 修改属性
        self.name = name

    def fn3(self):
        # 获取属性
        print(self.name)

    def fn4(self):
        # 删除属性
        del self.name

# 创建对象


p1 = Person()
# 调用方法
p1.fn1('Lisi')

print(p1.name)

p1.fn2('hello')
print(p1.name)

p1.fn3()
p1.fn4()
# print(p1.name)
p1.fn3()