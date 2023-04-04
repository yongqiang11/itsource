# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 08-公共方法.py
# Time       ：2023/3/23 22:17
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 内置函数
# len()  获取容器的长度    str,list,tuple,dict,set
print(len('hello'))
print(len((1, 2, 3, 4)))
print(len([1, 2, 3, 4]))
print(len({1, 2, 3, 4}))
print(len({'num': 1, 'num1': 2, 'num3': 3}))
# del()  删除变量
# max()   获取容器的最大值、
print(max([1, 2, 4]))
# min()   获取容器的最小值
print(min([1, 2, 4]))

# TODO 切片
# 字符串，列表，元组可以切片

# in 元素在容器中
# not in  元素不在容器中

# 在数据中存在返回True，否则返回Flase
print('python' in ['python', 'mysql'])
print('pyth' in ['python', 'mysql'])
print('pyth' not in ['python', 'mysql'])
print('python' not in ['python', 'mysql'])

# 配合循环使用else
# 当代码正常结束，执行else的内容，当循环是break结束就不执行else的内容
# while
i = 0
while i < 3:
    print(i)
    i += 1
    break
else:
    print('循环结束')

print('--' * 20)
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('循环结束')
print('--' * 20 )
# for
for i in range(1, 7):
    print(i)
else:
    print('循环结束')

print('--' * 20 )

for i in range(1, 7):
    print(i)
    break
else:
    print('循环结束')


# range函数配合for循环实现具体的循环次数
# range(start,stop,step)
# 返回的是一个可迭代列表
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
# 注意：range迭代对象遵循左闭右开的原则
print('--' * 20)
# 输出1~5数字
for i in range(1, 6):
    print(i)

# 循环打印5次
for i in range(4):
    print(f'hell0 world{i}')

print('--' * 20)

names = [['张飞', "刘备", "关羽"], ["曹操", "典韦", "司马懿"]]
li = []
for name_list in names:
    for name in name_list:
        li.append(name)
print(li)