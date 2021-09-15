#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 21:49
# @Author  : Zhangyp
# @File    : GetIP.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import socket

# def local_ip():
# 	hostname = socket.gethostname()
# 	ip = socket.gethostbyname(hostname)
# 	return ip

def local_ip():
	try:
		csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		csock.connect(('8.8.8.8', 80))
		(addr, port) = csock.getsockname()
		csock.close()
		return addr
	except socket.error:
		return "127.0.0.1"


if __name__ == '__main__':
	print(local_ip())
