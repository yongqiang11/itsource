# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03-写入操作.py
# Time       ：2023/5/25 10:19
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# TODO 1.导入pymysql
import pymysql
# TODO 2.创建连接对象
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='root',
                     database='test', charset='utf8')
# TODO 3.获取游标对象
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
try:
    # TODO 4.执行sql语句

    # sql = "UPDATE student SET stu_name='haha' WHERE stu_id=1"
    sql = "insert into student values (10,'im-10','测试',12)"
    cursor.execute(sql)
# TODO 5.提交或者回滚
except Exception as e:
    print(e)
    db.rollback()   # 回顾
else:
    db.commit()    # 提交

# TODO 6.关闭游标对象
cursor.close()
# TODO 7.关闭连接对象
db.close()