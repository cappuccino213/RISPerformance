#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 14:29
# @Author  : Zhangyp
# @File    : DateTimeData.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import datetime


def today_horizon2str():  # '2020-02-26 00:00:00|2020-02-26 23:59:59'
	now = datetime.datetime.now()  # 当前时间
	zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)  # 今天零点
	last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)
	return zero_today.strftime('%Y-%m-%d %H:%M:%S') + '|' + last_today.strftime('%Y-%m-%d %H:%M:%S')


def within3days():
	now = datetime.datetime.now()
	three_days = now - datetime.timedelta(days=3, hours=now.hour, minutes=now.minute, seconds=now.second)
	zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
	last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)
	return three_days.strftime('%Y-%m-%d %H:%M:%S') + '|' + last_today.strftime('%Y-%m-%d %H:%M:%S')
# print(today_horizon2str())

# print(within3days().split("|"))