# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 12-时间模块.py
# Time       ：2023/5/8 16:44
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
时间戳: 从英国格里尼茨天文台1970年1月1日 00:00:00, 到现在的一个秒数
时区: 全球被分为24个时区, 我们在东8区

时间模块有两个:
        基本时间模块   ---->  import time
            特点: 从1970年1月1日 00:00:00 可以使用到 2038年1月1日 00:00:00  ---> 以32位来处理时间
        高级时间模块   ---->  import datetime
            特点: 从1970年1月1日 00:00:00 可以使用倒 9999年1月1日 00:00:00  ---> 以64位来处理时间
            
基础时间模块:
    1. time.time()  ---->  展示时间戳
    2. time.sleep(k)  ---->  让程序停留k秒钟
高级时间模块: ---> 原则: 操作的数据类型大部分都是时间对象
    1. 自定义一个时间对象   ---->  datetime.datetime(年, 月, 日....)
    2. 创建一个现在时间对象  ---->  datetime.datetime.now()
    3. 自定义时间块(一段时间)   ---> datetime.timedelta() 
      这个类的使用，一定要结合date类的对象 或 datetime类的对象使用。也就是说，一定是基于这两个类的对象，进行时间的加、减。

工作中, 通常要将时间对象转换成字符串
    将时间对象 --转换成--> 字符串   --->  datetime.datetime.strftime(时间对象, 格式)
    将字符串时间 -转换成-> 时间对象  --->  datetime.datetime.strptime(字符串, 格式)  注意: 格式一定要和字符串的格式一致

"""


# 引入模块
import time
import datetime

# 使用模块
"""查看时间戳"""
print(time.time())
time.sleep(3)
print(time.time())

print('--' * 20)

# 创建一个时间对象
tomorrow = datetime.datetime(2023, 5, 10, 10, 11, 55)
print(tomorrow)

# 获取当前的时间
now = datetime.datetime.now()
print(now)

print('--' * 20)
# 将当前时间转换为字符串
str_time = datetime.datetime.strftime(now, '%Y-%m-%d')
print(str_time)

# 字符串转换为时间对象
str1 = '2023-10-22'
time_object = datetime.datetime.strptime(str1, '%Y-%m-%d')
print(time_object)
print(type(time_object))

print('--' * 20)

# 创建一个5天的时间块
chunk_time = datetime.timedelta(days=5)
print(chunk_time)

# 计算520天之后是多久
# 创建当前时间对象
now_time2 = datetime.datetime.now()
# 创建520天的时间块
day_520 = datetime.timedelta(days=520)
# 计算求和
end_time = now_time2 + day_520
print(end_time)

