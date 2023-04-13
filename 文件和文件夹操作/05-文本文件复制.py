# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 05-文本文件复制.py
# Time       ：2023/4/13 17:43
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 获取之前文件的所有内容

file_name = input('输入你相应复制的文件名')


f = open(file_name, 'r', encoding='utf8')
content = f.read()

f.close()

# 构建新文件名
# 方法1：

# file_prefix, file_postfix = file_name.rsplit('.', 1)
# copy_file_name = file_prefix + '-副本.' + file_postfix
# print(copy_file_name)
# 方法2：
index_location = file_name.rindex('.')
file_prefix = file_name[:index_location]
file_postfix = file_name[index_location:]
copy_file_name = file_prefix + '-副本' + file_postfix

# 将原文件内容放入新文件

f_new = open(copy_file_name, 'w', encoding='utf8')
f_new.write(content)
f.close()