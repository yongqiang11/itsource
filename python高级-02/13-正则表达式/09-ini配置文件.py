# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 09-ini配置文件.py
# Time       ：2023/5/16 14:11
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
ini配置文件： windows操作系统下的一种配置数据的文件

用python代码去操作ini配置文件
"""

import  configparser

conf = configparser.ConfigParser()   # 实例化对象
conf.read('db.ini', encoding='utf8')  # 读取文件


# 获取所有的节
all_sections = conf.sections()
print(all_sections)

# 获取指定节下面所有的 键
keys = conf.options('database')
print(keys)

# 获取某个节下面指定的 键对应的值
value = conf.get('database', 'host')   # 获取database下面host对应的值
print(value)

# 获取指定节下面所有的键值对
items = conf.items('database')
print(items)
"""
脚本执行结果：
['database', 'qq']
['host', 'port', 'user', 'password']
localhost
[('host', 'localhost'), ('port', '3306'), ('user', 'root'), ('password', 'root')]
"""
print('==' * 20)


# 修改某个节 下面指定的 键对应的值
# 语法： conf.set('节点, '键', '新值')
conf.set('database', 'host', '172.168.1.1')  # 这个时候还没有写入

conf.write(open('db.ini', 'w')) # 将内容写入

"""
# 添加一个节
conf.add_section('love')
conf.write(open('db.ini','w'))  # 将节写入
"""

"""
# 删除一个节 
conf.remove_section('qq')   
conf.write(open('db.ini', 'w'))

"""
# 删除指定节中的键值对
conf.remove_option('database', 'user')  # 删除指定的database中的 user键值对
conf.write(open('db.ini', 'w'))

