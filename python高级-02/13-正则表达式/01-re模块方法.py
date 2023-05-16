# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-re模块方法.py
# Time       ：2023/5/10 18:55
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import re
"""
pattern  匹配的正则表达式
string   要匹配的字符串
flags    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
"""

# TODO re.search(pattern, string[,flags])
# 在string中查找正则匹配的字符串，第一个匹配到的对象或者None.匹配到返回对象，匹配不到返回None

str1 = 'hello 232hello 123 hello'
# 原字符
match_obj = re.search('hello', str1)
print(match_obj)

print(match_obj.group())    # 提取匹配到的字符串

print('--' * 30)

# TODO re.findall(pattern, string[, flags])
# 列出字符串中模式的所有匹配项，所有匹配到的字符串列表
match_list = re.findall('hello', str1)
print(match_list)

