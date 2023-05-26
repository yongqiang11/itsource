# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-pymysql上下文管理器.py
# Time       ：2023/5/26 10:22
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import pymysql
# 创建连接对象
cnn = pymysql.connect(host='127.0.0.1', port=3306,
                     user='root', password='root',
                     database='test', charset='utf8')
with cnn:
    with cnn.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        # 其他操作
        data = input('需要查询的字段:')
        sql = "select * from student  where stu_name = %s"
        cur.execute(sql, [data])
        result = cur.fetchall()
        print(result)