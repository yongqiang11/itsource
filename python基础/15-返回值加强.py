# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 07-返回值加强.py
# Time       ：2023/4/7 21:32
# Author     ：ant
# version    ：python 3.11
# Description：
"""
'''

# return的作用：
    1.将数据返回到函数的调用位置
    2.退出函数
'''


# TODO 函数返回None的情况
# 第一种：函数没有显示的写return


def fn(a, b):
    print(a)
    print(b)


print(fn(1, 2))

print('--' * 20)

# 第二种  return 后面什么都不写


def fn2(a, b):
    print(a)
    print(b)
    return


print(fn2(1, 2))

# 第三种 return None
print('--' * 20)


def fn3(a, b):
    print(a)
    print(b)
    return None


print(fn3(1, 2))

# TODO 同时返回多个值

