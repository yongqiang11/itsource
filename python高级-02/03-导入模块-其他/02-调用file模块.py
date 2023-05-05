# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-调用file模块.py
# Time       ：2023/5/5 16:15
# Author     ：ant
# version    ：python 3.11
# Description：
"""
from file import File

file_obj = File()

print(file_obj.read('123.txt'))

