# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06-findall使用.py
# Time       ：2023/5/16 10:20
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# findall  按照正则表达式，匹配所有的匹配项，返回列表

import  re
# 匹配成功
list1 = re.findall('he\w{3}', 'hellodsdsdllhead1,fdfdfhead3')
print(list1)
# 匹配失败
list2 = re.findall('ha\w{3}', 'hellodsdsdllhead1,fdfdfhead3')
print(list2)

print(re.search('he\w{3}', 'hellodsdsdllhead1,fdfdfhead3'))   # 匹配成功
print(re.search('ha\w{3}', 'hellodsdsdllhead1,fdfdfhead3'))   # 匹配失败
# search 第一个匹配到的对象或在None,匹配到返回对象，没有匹配到返回None

"""
脚本执行结果:
['hello', 'head1', 'head3']
[]
<re.Match object; span=(0, 5), match='hello'>
None

"""