# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06-字典.py
# Time       ：2023/3/21 8:52
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 字典定义
'''
# 结构  
{key1:value1, key2:value2, key3:value3}
# 注意事项
1.key为不可变的数据类型，一般为字符串
2.value任何数据类型都可以
3.key值是唯一的
'''
# TODO 字典-修改
# 语法 字典[key] = value  如果key不存在，添加键值对，如果存在，修改value
info = {'name': '李四', 'age': 20}
print(info)

info['name'] = '豆豆'
print(info)
info['addr'] = '成都'
print(info)
print('==' * 20)

# 语法   字典.setdefault(key,value)  如果key存在返回key对应的value值，不存在，添加键值对
info = {'name': '李四', 'age': 20}
print(info.setdefault('name', '王五'))

info.setdefault('address', '上海')
print(info)

# 语法   字典.update(字典2)   将字典2的数据合并到字典
info = {'name': '李四', 'age': 20}
info1 = {'name': '王五', 'age': 18, 'address': '四川'}  # 如果key相同,会把相应的值覆盖。
info.update(info1)
print(info)

# TODO 字典-删除
# 语法 del 字典[key]  删除指定的key,不存在就会报错
info = {'name': '李四', 'age': 20}

del info['name']
print(info)

# 语法 字典.pop(key) 删除指定的key并弹出相应的value，不存在就会报错

info = {'name': '李四', 'age': 20}
print(info.pop('name'))
print(info)

# 清空字典   字典.clear()
info = {'name': '李四', 'age': 20}
info.clear()
print(info)
print('==' * 20)

# TODO 字典查询
# 字典[key]  通过key获取对应的值,如果不存在，就会报错
info1 = {'name': '李四', 'age': 20}
print(info1['age'])
# print(info1['addr'])

print('==' * 20)
# dict.get(key[, value]) 返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。
print(info1.get('name'))
print(info1.get('adr'))
print(info1.get('nam', '四川'))

# len(容器)  str, list, tuple, dict 获取容器的长度
print(len(info1))

print('--' * 30)
# dict.values()  获取字典的值
print(info1.values())
# dict.keys()   获取字典的键
print(info1.keys())
# dict.items()  获取所有的key和value
print(info1.items())

print('--' * 30)
# in 语句
# 元素是否在容器中 是就是True 否就是False
# 语法： 元素 in 容器
dict1 = {'name': 'hello', 'age': 18}
# 查看key在不在字典中
# 第一种
print('name' in dict1.keys())
# 第二种
print('name' in dict1)
# 查看value在不在字典中
print('hello' in dict1.values())

# list
print('hello' in ['hello', 'good'])
print('hello1' in ['hello', 'good'])

print('--' * 30)
# TODO 字典-遍历
# 遍历key
# di
dict1 = {'name': 'hello', 'age': 18}
# 第一种
for key in dict1.keys():
    print(key)

print('==' * 30)
# 第二种
for key in dict1:
    print(key)

print('==' * 30)

# 遍历value

for value in dict1.values():
    print(value)

print('==' * 30)

# 遍历value和key
# for item in dict1.items():
#     print(item)         无法实现，可以使用元组拆包

for key, value in dict1.items():
    print(key, value)