# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 05-贪婪模式和非贪婪模式.py
# Time       ：2023/5/12 17:21
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# 贪婪模式： 默认正则表达式，灰尽可能多的匹配
# 非贪婪模式： 在进行匹配的时候，尽可能少的匹配

import  re

# 贪婪模式（默认）
print(re.search('he\w+', 'hello').group())
print(re.search('he\w+', 'hellorerwerwerewre').group())

print('--' * 20)
# 非贪婪模式
print(re.search('he\w+?', 'hello').group())
print(re.search('he\w+?', 'hellorwerere').group())

"""
脚本执行结果:
hello
hellorerwerwerewre
----------------------------------------
hel
hel
"""

