# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 11-生成器.py
# Time       ：2023/5/16 15:58
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
概念：
    生成器：是一种特殊的迭代器，但是生成器比较优雅（在使用到具体的元素时，才会在内存中生成，不使用时不会占用内存）
    生成器的作用就是处理大数据
语法：
    列表名=(表达式 for i in 容器   简单判断]
    生成器名=(表达式 for i in容器 简单判断)
    
补充：
    在内存中看一个对象的大小
        import sys
        sys.getsizeof(对象)    ---> 在内存中看一个对象的大小
"""
import sys
# 利用列表推导式 实现[1, 2, 3, 4, 5]    -->生成的列表
list1 = [i for i in range(1, 600)]
print('列表在内存中的大小:', sys.getsizeof(list1))
sum1 = 0
for i in range(0, 600):     # 大数据直接报内存错误
    sum1 = sum1 + i
print(sum1)

print('--' * 20)

# 创建一个生成器     --->生成一个生成器
gen1 = (i for  i in range(1, 6))        # 生成的是一个对象
print('生成器在内存中的大小:', sys.getsizeof(gen1))
sum2 = 0
for j in range(0, 600):
    sum2 = sum2 + j
print(sum2)





