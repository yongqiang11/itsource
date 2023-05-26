# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03-优化pymsql ini脚本.py
# Time       ：2023/5/26 10:59
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import pymysql
import  configparser

# 引入ini配置文件信息
conf = configparser.ConfigParser()
conf.read('./db.ini', encoding='utf8')
ini_sqldb = dict(conf.items('my_sqldb'))  # 获取节点的数据并转化为字典
ini_sqldb['port'] = 3306 # 将port修改为整型
# print(ini_sqldb)
# 创建连接对象
cnn = pymysql.connect(**ini_sqldb)
with cnn:
    with cnn.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        # 其他操作
        sql = "select * from student "
        cur.execute(sql)
        result = cur.fetchall()
# 查看结果
print(result)


"""
事务：一组有关联关系的SL语句，要么全部执行成功，要么全部执行失败
事务步骤：
    1,将一组sgL语句定义为事务===>游标对象.begin()
    2,将sgL语句放置在内存中进行执行
        2,1如果全部执行成功，提交到硬盘上  -->连接对象.commit()
        2,2如果有一条执行失败，就将内存中的执行结果清空   --->连接对象.rollback()
在pymysql使用事务，默认不需要在自己去定义事务
"""