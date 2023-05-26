# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-上下文管理器.py
# Time       ：2023/5/26 10:11
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
概念：
    上下文管理器：帮助开发人员自动关闭文件 链接或操作
语法：
    with 文件或链接的操作  as  别名：
         文件或链接的其他操作
         
with关闭的时机：就是在with缩进体中的代码执行完毕，就关闭
"""

# 打开文件
# fp = open('10-三元运算符.py', 'r', encoding='utf-8')
# # 操作文件
# data = fp.readline()
# # 关闭文件
# fp.close()
#
# # 查看
# print(data)

with open('../10-三元运算符.py', 'r', encoding='utf-8') as fp:
    # 其他操作
    data = fp.readline()

# 查看
print(data)