#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 10:40
# @Author  : Zhangyp
# @File    : run_master.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from configuration.config import HOST, WEB


def start():
	import subprocess
	# cli = "locust -f TechinScript.py -H %s --web-host %s -P %s" % (HOST, WEB, PORT)
	cli = "locust -f TechinScenariosScript.py -H %s --web-host %s -P %s" % (HOST, WEB, 8187)
	try:
		cl = subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
		print(cl.stdout.readlines())  # 打印控制台信息
	except Exception as e:
		raise str(e)


if __name__ == '__main__':
	start()
