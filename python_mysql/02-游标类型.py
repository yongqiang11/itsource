# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02-游标类型.py
# Time       ：2023/5/22 17:55
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# !/usr/bin/env python
# -*-coding:utf-8 -*-

import pymysql
# 1. 导入pymysql

# 2. 创建连接信息
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='root',
                     database='test', charset='utf8')
# 3. 获取游标对象  # 作用： 执行sql语句,获取查询结果集
# TODO 游标类型
# 元组游标：获取到的结果集类型就是元组
cursor = db.cursor(cursor=pymysql.cursors.Cursor)
# 字典游标：获取到的结果集类型是字典
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)


# TODO 4. 执行查询sql语句
# sql语句不需要分号
# 返回受影响的行数
rows = cursor.execute('select * from student')
print(f'受影响的行数:{rows}')
# 5. 获取结果集
# 游标的行只能获取一次结果集
# 1.获取单条记录
# one = cursor.fetchone()
# print(one)
# one = cursor.fetchone()
# print(one)
# 以上获取2条记录
# 2.获取指定的条数
many = cursor.fetchmany(2)  # 获取2条记录
print(many)
# 3.获取所有的条数
# all_data = cursor.fetchall()
# print(all_data)
# 6. 关闭游标对象
cursor.close()
# 7. 关闭连接对象
db.close()
