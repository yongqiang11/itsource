# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 11-哈希散列.py
# Time       ：2023/5/8 16:26
# Author     ：ant
# version    ：python 3.11
# Description：
"""
"""
    哈希散列: 加密数据的一种方式
    加密方式: 将原数据加密成 16进制 的加密数据(8位, 16位, 32位...)

    md5: 属于哈希散列的一种
    sha2: 比md5加密的长度更长

语法:
    使用步骤:
        1. 引入模块  ----> import hashlib
        2. 使用md5
            md5的加密数据 = hashlib.md5(需要加密的原数据).hexdigest()

    注意事项:
        1. 需要加密的原数据, 必须是二进制数据类型
            1.1 通过 b'' 将数据转换成二进制   ---->  ASCII码转换成二进制
            1.2 通过encode() 将数据转换成二进制  ---> 都能用
        2. 原数据无论加密多少次, 值是固定不变的
        3. 原数据的大小无论多长, 得到的加密长度都是一样长
        4. 加密数据是不可逆的(不可解密)
"""

import  hashlib

num1 = b'12345'
num2 = '我去取一壶茶'
num3 = num2.encode()

# 加密
key1 = hashlib.md5(num1).hexdigest()
print(key1)

print('--' * 20)

# key2 = hashlib.md5(num3).hexdigest()
key2 = hashlib.md5(num2.encode()).hexdigest()
print(key2)
