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

# 语法 字典.pop(key) 删除指定的key并返回相应的value，不存在就会报错

info = {'name': '李四', 'age': 20}
print(info.pop('name'))
print(info)

# 清空字典   字典.clear()
info = {'name': '李四', 'age': 20}
info.clear()
print(info)

