# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-sql注入现象.py
# Time       ：2023/5/25 14:38
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""

sq注入解决
    SQL语句中的参数使用%s来占位，此处不是python中的字符串格式化操作
    将SQL语句中%s占位所需要的参数存在一个列表中，把参数列表传递给execute方法中第二个参数

"""
import pymysql
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='root',
                     database='test', charset='utf8')
cursor = db.cursor()
# 获取输入
title = input('title:')
stu = input('stu:')
# 执行sql
sql = 'select * from student  where stu_name = %s or stu_id = %s'

cursor.execute(sql, [title, stu])
# 获取结果集st1
print(cursor.fetchall())
cursor.close()
db.cursor()


