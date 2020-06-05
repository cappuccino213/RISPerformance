#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 10:47
# @Author  : Zhangyp
# @File    : configuration.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from configuration.GetIP import local_ip
"""locust相关"""
# HOST = "http://192.168.1.32:8602"  # 测试接口host
# HOST = "http://192.168.1.8:8141"  # 测试接口host
HOST = "http://192.168.1.18:8141"  # 测试接口host
# HOST = "http://192.168.1.123:7200"  # 测试接口host

# WEB = "192.168.1.56"  # 网页运行地址
WEB = local_ip()  # 当前运行机器的地址

PORT = 8186  # 网页运行端口

SCRIPT = "test.py"  # 需要执行的脚本名字,登记模块
# SCRIPT = "ReportScript.py"  # 需要执行的脚本名字，报告模块
# SCRIPT = "IntegratedSearchScript.py"  # 需要执行的脚本名字，综合查询

INTERVAL = 3  # 任务间隔时间

"""header相关"""
# 内容类型
CONTENT_TYPE = 'application/octet-stream'

# 不含用户信息的
USERINFO = '{"clientAuthCode":"","useScenario":"1","cookieRequest":{"printTaskSolution":"00000000-0000-0000-0000-000000000001","printerSolution":"00000000-0000-0000-0000-000000000002","equipSolution":""}}'

# 指定用户
USERINFO1 = '{"userID":"e2820f93-cf2f-4172-a9f7-ab6600e3a181","organizationID":"c9e6267a-dc60-4548-a6cb-ab6600da2bff","observationDeptID":"bc05c243-761f-4f6f-9e44-ab6600dabe33","clientAuthCode":"","useScenario":"1","cookieRequest":{"printTaskSolution":"00000000-0000-0000-0000-000000000001","printerSolution":"00000000-0000-0000-0000-000000000002","equipSolution":""}}'

USERINFO2 = '{"userID":"b2c84def-4526-4dd1-8348-ab66010f3652","organizationID":"93a6f377-717d-4dc3-a2ae-ab6600b6b2ab",' \
			'"observationDeptID":"aa688ecb-9f0c-439c-bcd1-ab6600b6edd9","clientAuthCode":"","useScenario":"1",' \
			'"cookieRequest":{"printTaskSolution":"00000000-0000-0000-0000-000000000001","printerSolution":"00000000-0000-0000-0000-000000000002",' \
			'"equipSolution":"dea00d0d-dbe2-4179-8dc4-ab6700ee1b99"}}'


"""Token相关"""


def if_token(flag):
	if flag:
		from configuration.GetToken import get_token
		return get_token()
	else:
		return "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IlFXWUhaWUZaWCIsIkN1c3RvbURhdGEiOiJ7fSIsImp0aSI6IjU3MTNmY2VlLTAwZTAtNDM1OC05MmNkLTA1NTgwNTVmNzA3NCIsImlhdCI6IjIwMjAvMy80IDExOjM3OjM3IiwiZXhwIjoxNTgzMjkzMTc3LCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUklTIn0.Tdkf7M4vMh3K5BYQq9t02WFbw2UTusR9ULEVL5UYyMs"


TOKEN = if_token(0)  # 是否调用token，0不开启

