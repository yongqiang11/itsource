# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06_01赋值.py
# Time       ：2023/5/9 14:12
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
    赋值: 数据在内存空间中的一个指向

    简单数据类型: 整数, 浮点数, 字符串, 布尔值
        特点: 简单数据类型, 值相同, 内存地址一定相同

    复杂数据类型: 列表, 字典, 元组, 集合      
        特点: 复杂数据类型, 值相同, 内存地址一定不同
        
    3.7之后元组的值相同，内存地址也相同    
"""
# 简单数据  ---> 数据的值相同, 内存地址一定相同
name1 = "张三"
name2 = "张三"

print(name1 == name2) # True
print(name1 is name2) # True

# 复杂数据  ---> 数据的值相同, 内存地址一定不同
li1 = [1, 2, 3, 4]
li2 = [1, 2, 3, 4]

print(li1 == li2)  # True
print(li1 is li2)  # False


# 元组
tuple1 = (1, 2, 'he', 1)
tuple2 = (1, 2, 'he', 1)
print(tuple1 == tuple2)  # True
print(tuple1 is tuple2)  # True