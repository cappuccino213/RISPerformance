#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 21:49
# @Author  : Zhangyp
# @File    : GetIP.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import socket


def local_ip():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	return ip


# print(local_ip())
