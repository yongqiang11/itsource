# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-文件操作基础.py
# Time       ：2023/4/11 11:16
# Author     ：ant
# version    ：python 3.11
# Description：
"""

'''
步骤

1.打开文件
f(文件资源对象) = open('文件路径'，打开模式,encoding='utf8')
文件路径：文件存放的位置，可以是绝对路径也可以是相对路径
打开模式：默认r, 操作文件的方式  读read(r),写write(w),追加append(a)

w：如果文件不存在，会自动新建文件，存在覆盖原来内容
r：让字符串成为原生字符
2.操作文件
f.write(content)  写入
f.read()    读

3.关闭文件
f.close()
'''

file_path = r'D:\python\Project\itsource\文件和文件夹操作\demo.txt'
f = open(file_path, 'r', encoding='utf8')
content = f.read()
print(content)
f.close()
