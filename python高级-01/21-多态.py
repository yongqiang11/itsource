# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 21-多态.py
# Time       ：2023/4/20 16:35
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
多态: 多个子类 同时继承 同一个父类, 并且重写了父类的 同一个方法, 这些方法表现出不同的效果
"""


# 创建一个动物类
class Animal(object):
    # 定义属性
    pass

    # 定义方法
    def run(self):
        print("动物都会跑...")


# 创建一个猫类
class Cat(Animal):
    # 定义属性
    pass

    # 定义方法
    def run(self):
        print("轻轻的跑...")


# 创建一个蛇类
class Snake(Animal):
    # 定义属性
    pass

    # 定义方法
    def run(self):
        print("嗦嗦的跑...")


# 创建一个鱼类
class Fish(Animal):
    # 定义属性
    pass

    # 定义方法
    def run(self):
        print("摆摆的跑...")


# 实例化对象
c1 = Cat()
s1 = Snake()
f1 = Fish()

# 使用对象
c1.run()
s1.run()
f1.run()
