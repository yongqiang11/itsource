# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06-大文件复制.py
# Time       ：2023/4/14 11:31
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import os.path

# 源文件
file_name = input('需要复制的文件：')

# 构建目标文件名
file_prefix, file_postfix = os.path.splitext(file_name)
file_new = file_prefix + '-副本' + file_postfix

# 打开源文件， 目标文件
source_file = open(file_name, 'rb')
new_file = open(file_new, 'wb')

# 按照固定的大小循环写入内容
while True:
    content = source_file.read(1024)
    if not content:
        break
    new_file.write(content)

# 关闭文件
source_file.close()
new_file.close()