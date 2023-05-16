# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-匹配单个字符.py
# Time       ：2023/5/10 19:19
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import re

# 原子符：匹配原生字符
# 元字符：具有特殊含义的字符

# 原子符
"""

print(re.search('a', 'haha').group())
print(re.search('c', 'haha'))  # 匹配不到返回None

"""

print('--' * 30)

# . 匹配任意1个字符（除了\n）
"""
print(re.search('.he', 'heheewuei'))
print(re.search('.hee', 'sheheewuei'))
print(re.search('s.e', 'sheheewuei'))
print(re.search('sh.', 'sh*heewuei'))
print(re.search('shrer.', 'sh*heewuei'))  # 匹配不到
print(re.search('ee.', 'shehee\nwuei'))  # 匹配不到
"""


# [ ]	匹配[ ]中列举的字符[0-9][a-z][A-Z][\u4e00-\u9fa5]
"""

print(re.search('[abcd]go', 'hdksdagodf'))
print(re.search('[abcd]go', 'hdksdbgodf'))
print(re.search('[abcd]go', 'hdksddgodf'))
print(re.search('[0-9]go', 'hdksd9go0f'))
print(re.search('[a-z]go', 'hdksdigo0f'))
print(re.search('[A-Z]go', 'hdksdFgo0f'))
print(re.search('[\u4e00-\u9fa5]go', 'hdks测试go0f'))
"""
# \d	匹配数字，即0-9    [0-9]
"""
print(re.search('\dgo', 'dsdkdsk2go'))
print(re.search('\dgo', 'dsdkdsk10go'))
print(re.search('\dgo', 'dsdkdsk@go'))  # 匹配不到
"""

# \D	匹配非数字，即不是数字
"""
print(re.search('\Dgo', 'dsdkdsk2go'))  # 匹配不到
print(re.search('\Dgo', 'dsdkdsk测试gore'))
print(re.search('\Dgo', 'dsdkdsk gore'))
print(re.search('\Dgo', 'dsdkdsk@go'))
"""

# \s	匹配空白，即 空格，tab键, \n
"""
print(re.search('\sgo', 'dshj go'))
print(re.search('\sgo', 'dshj go'))
print(re.search('\sgo', 'dshj\ngo')) 

str1 = '''
go
'''
print(re.search('\sgo', str1))  # 匹配不到
print(re.search('\sgo', 'hjhgo'))  
"""
# \S	匹配非空白
"""
print(re.search('\Sgo', 'dshj go'))  # 匹配不到
print(re.search('\Sgo', 'dshj go'))  # 匹配不到
print(re.search('\Sgo', 'dshj\ngo'))  # 匹配不到
str1 = '''
go
'''
print(re.search('\Sgo', str1))
print(re.search('\Sgo', 'hjhgo'))
"""
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字  [a-zA-Z0-9_\u4e00-\u9fa5]
"""
print(re.search('\wgo', 'dsdgo'))
print(re.search('\wgo', 'dsAgo'))
print(re.search('\wgo', 'ds8go'))
print(re.search('\wgo', 'ds_go'))
print(re.search('\wgo', 'ds测试go'))
print(re.search('\wgo', 'ds@go'))  # 匹配不到
"""
# \W	匹配特殊字符，即非字母、非数字、非汉字、非下划线
print(re.search('\Wgo', 'dsdgo'))  # 匹配不到
print(re.search('\Wgo', 'dsAgo'))  # 匹配不到
print(re.search('\Wgo', 'ds8go'))  # 匹配不到
print(re.search('\Wgo', 'ds_go'))  # 匹配不到
print(re.search('\Wgo', 'ds测试go'))  # 匹配不到
print(re.search('\\Wgo', 'ds@go'))