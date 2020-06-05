#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 17:52
# @Author  : Zhangyp
# @File    : run_slave.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from configuration.config import HOST, PORT


def start():
	import subprocess
	cli = "locust -f RegisterScenariosScript.py -H %s --slave --master-host=%s --loglevel=DEBUG" % (HOST, "192.168.1.21")
	# cli = "locust -f RegisterScenariosScript.py -H %s --slave --master-host=%s" % (HOST, "192.168.1.56")
	try:
		cl = subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
		print(cl.stdout.readlines())  # 打印控制台信息
	except Exception as e:
		raise str(e)


if __name__ == '__main__':
	start()
