# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04-登录案例.py
# Time       ：2023/4/11 21:15
# Author     ：ant
# version    ：python 3.11
# Description：
"""

# 选择功能

code = input('请选择你的功能[1注册 2登录]:')

if code == '1':
    user = input('输入你需要注册的用户名')
    passwd = input('输入你的密码')
    f = open('users.txt', 'a', encoding='utf8')
    f.write(f'{user},{passwd}\n')
    f.close()
    print(f'{user}注册成功')

#
# elif code == '2':
#     # 接收信息
#     user = input('输入你需要登录的用户名')
#     passwd = input('输入你的密码')
#     # 获取信息
#     f = open('users.txt', 'r', encoding='utf8')
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         # 获取用户名和密码  'hell0,123\n' --> 'hell0,123' --> ['hello','123']
#         sys_user, sys_passwd = line.rstrip('\n').split(',')
#         # 判断用户输入和系统中的用户信息是否匹配
#         if sys_user == user and sys_passwd == passwd:
#             print('登录成功')
# #             break
# #     f.close()
#
# else:
#     print('没有这个功能')


# 方法二

elif code == '2':
    # 接收信息
    user = input('输入你需要登录的用户名')
    passwd = input('输入你的密码')
    # 获取信息
    f = open('users.txt', 'r', encoding='utf8')
    while True:
        line = f.readlines()
        if not line:
            break
        for i in line:
            sys_user, sys_passwd = i.rstrip('\n').split(',')
            if sys_user == user and sys_passwd == passwd:
                print('登录成功')
                break
        # # 获取用户名和密码  'hell0,123\n' --> 'hell0,123' --> ['hello','123']
        # sys_user, sys_passwd = line.rstrip('\n').split(',')
        # 判断用户输入和系统中的用户信息是否匹配
        # if sys_user == user and sys_passwd == passwd:
        #     print('登录成功')
        #     break
    f.close()
else:
    print('没有这个功能')
