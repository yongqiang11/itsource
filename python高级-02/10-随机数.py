# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 10-随机数.py
# Time       ：2023/5/8 15:26
# Author     ：ant
# version    ：python 3.11
# Description：
"""


"""
random模块用于生成随机数
 
random.random()  -->随机生成0~1的浮点数 [0, 1)不包含1
random.randit(a, b)  -->随机生成a~b的整数  [a, b]包含a,b  b>a 
random.choice(序列)    -->从序列中随机取一个元素
random.sample(序列， k)  --从一个序列中取出K个数据,k个元素以列表形式保存

"""
import random

print(random.random())
print(random.randint(1, 3))

list1 = ['hello', 1, 'mysql', '测试']
print(random.choice(list1))

print(random.sample(list1, 2))

print('--' * 20)

# 验证码问题   预期实现如：USD5
my_str = "DSKDJSK4343JFDSFLE242"
verify_num = random.sample(my_str, 4)
new_num = ''.join(verify_num)
print(new_num)