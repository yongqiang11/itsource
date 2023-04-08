# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-列表.py
# Time       ：2023/3/19 9:26
# Author     ：ant
# version    ：python 3.11
# Description：
"""
'''
列表是具有顺序的数据容器。又称之为序列。该容器是可以修改的。
定义列表需要使用方括号，列表中的项目都包含在方括号中，项目之间使用逗号分隔列表中的数据可以是任意数据类型，甚至可以是不同类型的混合。通常存储同类型数据的‘
注意事项：
    1. 列表中的元素可以写任何数据类型
    2. 列表中数据的位置可以随意
    3. 列表中数据可以重复
语法：
    第一种（常用）
        list1 = []  # 空列表
        list2 = [1, 2, 3, 'abc', True, False]
    第二种
        list1 = list()  #空列表
        list2 = list('hello')

        
# 注意事项
    1.通过[] 定义一个列表或者使用list()内置方法生成。
    2.列表中每个数据也被称为元素，每个元素通过“，”分割。
    3.列表中的每个数据都有对应的索引，该索引就是元素在列表中的位置编号，索引也可以被称为下标,索引从0开始,依次递增。
'''

list2 = list('hello')
print(list2)

print('==' * 20)

# TODO 列表-增加
# list.insert(索引， 数据)  在指定的索引位置添加元素

list1 = ['python', 'linux', 'mysql']
list1.insert(1, 'shell')
print(list1)

# list.append()   将整个数据追加到列表末尾
list2 = ['python', 'linux', 'mysql']
list2.append('hello')
print(list2)
list2.append([1, 2, 3])
print(list2)

print('==' * 20)

# list.extend()  将数据（list|str）中的元素依次添加到列表末尾
list3 = ['python', 'linux', 'mysql']
list3.extend([1, 2, 3, ])
print(list3)
list3.extend('hello')
print(list3)
print('==' * 20)

# TODO 列表-删除

# del 列表[索引]删除指定索引的数据
list3 = ['python', 'linux', 'mysql']
del list3[-1]
print(list3)

# list.remove() 删除第一个出现的数据
list3 = ['python', 'linux', 'mysql', 'linux']
list3.remove('linux')
print(list3)

# list.pop([索引])  默认弹出列表末尾的数据，如果设置了索引就弹出指定数据 .  可以通过变量获取到弹出的数据


list3 = ['python', 'linux', 'mysql', 'shell']
num = list3.pop()
print(list3)
print(num)

num2 = list3.pop(-2)
print(list3)
print(num2)

# list.clear()  清空列表,返回空列表
list3 = ['python', 'linux', 'mysql', 'shell']
list3.clear()
print(list3)

# TODO 列表-查询

# list[索引] 通过索引获取数据
list3 = ['python', 'linux', 'mysql', 'shell']
print(list3[1])
print(list3[-3])

# list.index(数据)  查询数据第一次出现的索引，查询不到会抛出错误
list4 = ['python', 'linux', 'mysql', 'python']
print(list4.index('python'))

# print(list4.index('hel'))  # 查询不到会抛出错误

# len(列表)  查询列表的长度
list4 = ['python', 'linux', 'mysql', 'python']
list5 = list('hello')
print(len(list4))
print(len(list5))

# list.count(元素)  查询元素在列表中出现的次数

list4 = ['python', 'linux', 'mysql', 'python']
num = list4.count('python')
print(f'python在列表中出现的次数为：{num}')

print('==' * 20)
# TODO 列表-修改
# list[索引] = 新值   修改指定索引的值
list4 = ['python', 'linux', 'mysql', 'python']
list4[1] = 'shell'
print(list4)

print('==' * 20)

# TODO 列表-排序

# list.sort()  升序排序
list1 = ['q', 'a', 'w', 'd']
list1.sort()
print(list1)

# list.sort(reverse=True) 降序排列

list1.sort(reverse=True)
print(list1)

# list.reverse()  逆转
list1.reverse()
print(list1)
'''
排序是按照ASCII码进行的
print(ord('a'))
'''
print(ord('a'))

print('==' * 20)
# TODO 列表-切片
'''
切片作用：
利用索引范围返回多个元素的新列表
切片可以针对：列表，元组，字符串
切片特点：
切片返回的仍然是原数据类型
切片返回新的列表，不影响原列表
语法：
list1[start:end:step]
start:起始索引,默认0,可以为负数
end:结束索引，不包括结束位置（左闭右开），可以为负数.正数从左向右查，负数从右向左查
step:步长，默认为1，可以为负数。 负责方向：正数从左往右查，负数从右往左查
省略第一个索引值，切片从列表开始，省略第二个索引值，切片直到列表末端。
'''
# 正数
list1 = ['python', 'mysql', 'git', 'linux']
# 取['python', 'mysql']
print(list1[0:2])
print(list1[0:2:1])
print(list1[:2])
# 取['python', 'git']
print(list1[0:3:2])
print(list1[:3:2])

# 复制这个列表
list2 = list1[:]
print(list2)

print('==' * 20)
# 负数
list1 = ['python', 'mysql', 'git', 'linux']

# 取['python', 'mysql']
print(list1[-4:-2])
# 取['git', 'linux']
print(list1[-2:])
# 取['python', 'git']
print(list1[-4::2])
print(list1[-4:3:2])

# 取['linux', 'git']
print(list1[-1:-3:-1])

print('==' * 20)
# 列表反转  list.reverse()  # 改变原列表进行反转
# 列表反转： 返回新的列表
print(list1[::-1])
print('==' * 20)

# TODO 列表-遍历
'''
遍历 就是依次从列表中取出每一个元素
'''
#  while循环
'''
索引= 0
长度 = len(列表)
while 索引 < 长度:
    元素 = 列表[索引]
    索引+=1
'''

list1 = ['python', 'mysql', 'git', 'linux']
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print('==' * 20)

# for 循环
'''
for 临时变量 in 列表:
    循环体
'''
for value in list1:
    print(value)
'''
注意事项：
    1.for只能够通过从头到尾 依次 从 列表 中取出 每一个元素， 执行效率高。
    2.while可以控制索引灵活地从列表中取出元素
    3.如果依次从头到尾取出每个元素时，请优先选择for。否则使用while。
'''
str = 'hello world'
for item in str:
    print(item)
print('==' * 20)

# TODO  列表-嵌套
list1 = [
    ['python', 'mysql', 'Linux'],
    ['apple', 'pear', 'Lemon']
]

print(list1[0])  # 取['python', 'mysql', 'Linux']
print(list1[0][0])  # 取python
print('==' * 20)
# 需求
# 把这个列表中的所有元素都遍历出来
for i in list1:
    # print(i)
    for j in i:
        print(j)
# TODO # 列表拆包
# 嵌套元组拆包

info = ['abc', 'we']
num1, letter = info
print(letter)

