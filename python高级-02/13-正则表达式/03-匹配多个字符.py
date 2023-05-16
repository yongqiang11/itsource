# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03-匹配多个字符.py
# Time       ：2023/5/12 10:26
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import re

# *	匹配前一个字符出现0次或者无限次  {0,}
"""
print(re.search('a*hj', 'hj'))
print(re.search('a*fd', 'afd'))
print(re.search('a*fdd', 'aafdd'))
print(re.search('a*ffd', 'aaaffd'))
"""
# +	匹配前一个字符出现1次或者无限次  {1,}
"""
print(re.search('\w+hj', '_hj'))
print(re.search('\d+fd', '34fd'))
print(re.search('\s+fdd', ' fdd'))
print(re.search('[a-z]+ffd', 'aaaffd'))
"""
# ?	匹配前一个字符出现1次或者0次 {0,1}
"""
print(re.search('a?hj', 'hj'))
print(re.search('a?fd', 'afd'))
print(re.search('a?fdd', 'aafdd'))
print(re.search('a?ffd', 'aakdfd'))  # 匹配不到
"""

# {m}	匹配前一个字符出现m次
"""
print(re.search('a{1}hj', 'ahj'))
print(re.search('\d{2}fd', '123fd'))
print(re.search('\w{3}fdd', 'awe_fdd'))
print(re.search('\s{2}ffd', '  ffd'))    # 2个空格
"""
# {m,n}	匹配前一个字符出现从m到n次
"""
print(re.search('a{1,2}hj', 'ahj'))
print(re.search('\d{2,3}fd', '123fd'))   
print(re.search('\s{1,5}ffd', '  ffd'))
"""
# {m,}	匹配前一个字符至少出现m次
"""
print(re.search('a{1,}hj', 'ahj'))
print(re.search('\d{2,}fd', '123fd'))
print(re.search('\s{1,}ffd', '  ffd'))
"""
