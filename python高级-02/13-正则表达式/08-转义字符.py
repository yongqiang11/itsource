# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 08-转义字符.py
# Time       ：2023/5/16 9:50
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# 需求：匹配文件名（完整文件名）
# 文件名： demo.txt   cat.jp xx.mp3  xx.mp4

import  re
filename = input('输入文件名:')
if re.search(r'^\w{1,20}.[a-zA-Z]{2,4}[34]?$',filename):
    print('文件格式正确')
else:
    print('文件格式错误')


# 如果不加r，只有.  demo+mp3执行是对的，需要使用r或在逗号前使用\ 进行转义

