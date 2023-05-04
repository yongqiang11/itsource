# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06-列表推导式.py
# Time       ：2023/5/4 17:07
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# 需求:列表中有1-100的元素[1, 2, 3, 4, .....]
"""
list_new = []
for i in range(1, 101):
    list_new.append(i)

print(list_new)

"""

# TODO 列表推导式
"""
说明：快速生成列表表达式
特点：生成列表语法简洁，效率高
语法： [生成元素的表达式  控制元素生成个数的表达式]
"""

# 需求1；列表中有1-100的元素[1, 2, 3, 4, .....]


list_new1 = [i for i in range(1, 101)]
print(list_new1)

# 需求：生成1~10的奇数
# 第一种
odd_list1 = [i for i in range(1, 11, 2)]
print(odd_list1)

# 第二种
odd_list2 = []
for i in range(1, 11):
    if i % 2 != 0:
        odd_list2.append(i)

print(odd_list2)

# 第三种

odd_list3 = [i for i in range(1, 11) if i % 2 != 0]
print(odd_list3)


