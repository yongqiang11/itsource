# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : OS库的操作.py
# Time       ：2023/4/13 22:11
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 导入os模块
import os

# TODO os.rename("文件名","新的文件名")  文件重命名
# demo.txt my_demo.txt
"""
os.rename('resource/demo.txt', 'resource/my_demo.txt')
"""

# TODO os.remove ("文件名") 删除文件
"""
os.remove('del_demo.txt')
os.remove('my_demo.txt')
"""

# TODO os.mkdir ("文件夹的名字") 创建文件夹
"""
os.mkdir('resource/dir1')
"""

# TODO  os.getcwd()  获取当前目录路径
"""
print(os.getcwd())
"""

# TODO  os.chdir ()  切换目录
"""
# 切换到resource
os.chdir('resource')
# 新建一个demo6.txt
f = open('demo6.txt', 'w', encoding='utf8')
f.close()
"""

# TODO os.listdir("目录路径")  列出目录下的资源
"""
print(os.listdir())
print(os.listdir('resource'))
"""

# TODO os.rmdir('目录路径') 删除空目录
"""
os.rmdir('resource/dir1')  # 空目录可以删除
os.rmdir('resource')  # 有内容删除不了
"""

#  TODO os.path.isdir("目录路径") 判断资源是文件夹
"""
print(os.path.isdir('resource'))
print(os.path.isdir('resource/demo1.txt'))
"""

# TODO os.path.isfile("文件路径") 判断资源是文件
"""
print(os.path.isfile('resource'))
print(os.path.isfile('resource/demo1.txt'))
"""

# TODO os.path.splitext('文件路径')  extension: 扩展 获取文件扩展
# 返回：（文件名, 后缀） -> (‘user’, ‘.txt’)
filename, extension = os.path.splitext('01-文件基本操作.py')
print(filename)
print(extension)
