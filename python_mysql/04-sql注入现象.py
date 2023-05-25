# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-sql注入现象.py
# Time       ：2023/5/25 14:38
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 根据需求查询姓名

import pymysql

db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='root',
                     database='test', charset='utf8')
cursor = db.cursor()
# 获取输入
title = input('title:')
# 执行sql
# sql  = f"select * from student  where stu_name= '{title}' "

sql  = f'select * from student  where stu_name="" or 1 = 1 or ""'

cursor.execute(sql)
# 获取结果集
print(cursor.fetchall())

cursor.close()
db.cursor()

# sql注入  " or 1 = 1 or "
# sql  = f"select * from student  where stu_name="" or 1 = 1 or " "

# 用户提交带有恶意的数据与SQL语句进行字符串方式的拼接，从而影响了SQL语句的语义，最
# 终产生数据泄露的现象。

