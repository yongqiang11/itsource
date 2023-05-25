# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 06-数据库封装类.py
# Time       ：2023/5/25 15:44
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
思路：
类名：Database
方法：
    init: 连接
    read
    write
    del:关闭

"""
import pymysql
class Database:
    def __init__(self, user, password, database,
                 host='localhost', port=3306, charset='utf8', cursor=pymysql.cursors.Cursor):  # 必填参数写在默认参数前面
        self.db = pymysql.connect(host=host, port=port,
                                  user=user, password=password,
                                  database=database, charset=charset)
        self.cursor = self.db.cursor(cursor=cursor)

        # 三元运算符

        self.cursor_type = () if cursor == pymysql.cursors.Cursor else []

        # if cursor == pymysql.cursors.Cursor:
        #
        #     self.cursor_type = ()
        # else:
        #     self.cursor_type = []

    def read(self, sql, arges=None):
        """读操作"""
        try:
            rows = self.cursor.execute(sql, arges)
        except Exception as e:
            print(e)
            return 0, self.cursor_type       # 返回报错尽量返回相同的格式数据
        else:
            all_data = self.cursor.fetchall()
            return  rows, all_data

    def write(self, sql, args=None):
        """写操作"""
        try:
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            self.db.rollback()
            return 0
        else:
            self.db.commit()
            return rows

    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':

    database = Database('root', 'root', 'test', cursor=pymysql.cursors.DictCursor)
    # sql = 'select * from student where stu_name = %s'
    #
    # # print(database.read(sql, ['st22'])) # rows ,all_data
    #
    # rows, all_data = database.read(sql, ['st22'])
    # print(rows)
    # print(all_data)

# 实现了字典类型显示，就返回字典类型，但目前报错，没得实现返回字典，使用判断实现
    sql = "insert into student values (101,'st88','stu_1',101)"  # 正确
#     sql = 'delete  from  student where stu_id=1'   正确
    print(database.write(sql))

