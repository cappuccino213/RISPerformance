#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 14:52
# @Author  : Zhangyp
# @File    : GetToken.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import requests


def get_token():
	header = {'Content-Type': 'application/json'}
	url = "http://192.168.1.18:8703/Token/Retrive"  # token服务器地址
	payload = {"requestIP": "192.168.1.56",  # 请求客户端
			   "audience": "eWordRIS",
			   "customData": {},
			   "expire": 240}
	res = requests.post(url, headers=header, json=payload)
	return res.json()['token']


if __name__ == '__main__':
	print(get_token())
