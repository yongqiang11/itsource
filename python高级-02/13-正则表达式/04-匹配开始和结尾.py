# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-匹配开始和结尾.py
# Time       ：2023/5/12 11:48
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import re
"""
import re

phone = input('请输入手机号码:')

if re.search(r'1[3-9]\d{9}', phone):
    print('手机号正确')
else:
    print('手机号错误')
"""

# 限制开始 ^
"""

print(re.search('^hello', 'hello123'))
print(re.search('^hello', 'ahello123'))  # 匹配不到
"""

#  限制结尾 $
"""
print(re.search('hello$', 'hello123'))  # 匹配不到
print(re.search('hello$', '123hello'))
"""

# 限制开始 ^ 结合 限制结尾 $
"""
print(re.search('^hello$', 'hello1'))  # 匹配不到
print(re.search('^hello$', 'hello'))

"""

phone = input('请输入手机号码:')

if re.search('^1[3-9]\\d{9}$', phone):
    print('手机号正确')
else:
    print('手机号错误')