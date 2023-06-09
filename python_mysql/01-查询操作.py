# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01-查询操作.py
# Time       ：2023/5/22 17:18
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# TODO 1. 导入pymysql
import pymysql
# TODO 2. 创建连接信息
"""
host:主机地址（域名|ip地址），默认值：Localhost
port:MySQL服务的端口号，默认值：3306
User:账号
password:密码
database:数据库
charset: 字符集
"""
db = pymysql.connect(host='localhost', port=3306,           # loccalhost=127.0.0.1更好，不需要域名解析，增加查询速度
                     user='root', password='root',
                     database='test', charset='utf8')
# TODO 3. 获取游标对象  # 作用： 执行sql语句,获取查询结果集    游标对象是连接对象创建的
cursor = db.cursor()
# TODO 4. 执行查询sql语句  通过游标对象执行
# sql语句不需要分号
# 返回受影响的行数
rows = cursor.execute('select * from student')
print(f'受影响的行数:{rows}')
# TODO 5. 获取结果集   通过游标对象执行
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
# TODO 6. 关闭游标对象
cursor.close()
# TODO 7. 关闭连接对象
db.close()


# for i in (all_data):
#     print(i[2])