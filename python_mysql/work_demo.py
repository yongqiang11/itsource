# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : work_demo.py
# Time       ：2023/5/25 11:14
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import pymysql

class News:
    def __init__(self,):
        self.db = pymysql.connect(host='localhost',port=3306,
                             user='root', password='root',
                             database='test', charset='utf8')
        self.cursor = self.db.cursor()

    def add_file_data(self):
        """一次性添加5条记录"""
        try:
            for i in range(20, 25):
                sql = f"INSERT INTO student VALUES ({i},'{'stu'+str(i)}', '{'st'+str(i)}', {i})"
                print(sql)
                self.cursor.execute(sql)

        except Exception as e:
            print(e)
            self.db.rollback()
        else:
            self.db.commit()
    def del_data_tit(self):
        """根据用户输入的标题删除记录"""

    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    a = News()
    a.add_file_data()

