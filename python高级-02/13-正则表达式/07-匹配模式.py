# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 07-匹配模式.py
# Time       ：2023/5/16 10:39
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import re
# 正则表达式默认区分大小写
# TODO  re.I  (ignore)匹配正则不区分大小写
print(re.search('he[a-z]', 'hello').group())
print(re.search('he[a-z]', 'hEllo'))    # 返回None
print(re.search('he[a-z]', 'hEllo', re.I))   # 添加模式后，不区分大小写


print('--' * 20)
# TODO  re.S  使.这个通配符可以匹配换行

print(re.search('he.', 'he\nee'))
print(re.search('he.', 'he\nee', re.S))

"""
脚本执行结果：
hel
None
<re.Match object; span=(0, 3), match='hEl'>
----------------------------------------
None
<re.Match object; span=(0, 3), match='he\n'>
"""

