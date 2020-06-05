#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 9:32
# @Author  : Zhangyp
# @File    : encryption.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

import hashlib

"""md5数据加密"""
def md5(plain_text):
	m = hashlib.md5(plain_text.encode())
	return m.hexdigest()

# print(md5('xxy'))