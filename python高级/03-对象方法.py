# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03-对象方法.py
# Time       ：2023/4/14 16:26
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 定义类
'''
对象方法：
1.对象方法在类的内部定义
2.必须要有一个参数self
3.其他和函数相同
'''


class Person:
    # TODO 对象方法的定义
    def eat(self):
        print(f'self:{self}')
        print('吃东西')

    def info(self, age, addr):
        self.age = age
        self.addr = addr


# TODO 对象方法的调用


p1 = Person()
print(f'p1:{p1}')
# 语法：obj.方法名()
p1.eat()

"""
p2 = Person()
print(f'p2:{p2}')
# 语法：obj.方法名()
p1.eat()
"""
p1.info(18, '成都')
print(p1.age)
print(p1.addr)

# TODO self
# self: 指向当前调用这个方法的对象
# self不需要手动传入，python解释器会自动把当前调用方法的对象传入

