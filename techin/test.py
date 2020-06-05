#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 17:10
# @Author  : Zhangyp
# @File    : test.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from configuration.config import HOST, USERINFO, CONTENT_TYPE, TOKEN
from common.DateTimeData import today_horizon2str
# 导入会公用到的pb文件
from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
from techin.proto_pb.SimpleOrderMessageRequestPb_pb2 import SimpleOrderMessageRequestPb
from techin.proto_pb.SimpleOrderRequestPb_pb2 import SimpleOrderRequestPb
from google.protobuf.json_format import MessageToJson
from techin.proto_pb.ExamLoadResponsePb_pb2 import ExamLoadResponsePb
from techin.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb
from techin.proto_pb.FinishExamResponsePb_pb2 import FinishExamResponsePb
from techin.proto_pb.ObservationListResponsePb_pb2 import ObservationListResponsePb
import requests
import json
from common.RandomData import TECINFO
# 声明头信息
header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': TECINFO}
none_header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': TECINFO, 'Content-Length': '0'}


def get_orderID():
	import requests
	import random
	api_url = HOST + "/api/Technician/UnFinishList"
	from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
	body = OrderSearchRequestPb()
	body.observationDate = today_horizon2str()
	from common.RandomData import OBSERVATIONLOCATIONID
	# body.observationLocationIDArray = PROCINFO['observationLocationID']
	body.observationLocationIDArray = str(random.choice(OBSERVATIONLOCATIONID)[0])
	body = body.SerializeToString()
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
	# 解析结果
	from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
	data = PageResponsePb()
	data.ParseFromString(res.content)
	# 结果转为json
	from techin.proto_pb.ObservationListResponsePb_pb2 import ObservationListResponsePb
	res_json = MessageToJson(data)
	res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
	if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
		if 'unFinishList' in res_dict['data'][0]:
			order_list = res_dict['data'][0]['unFinishList']
			order_choice = random.choice(order_list)  # 随机选择一个检查
			return order_choice['orderID']
		else:
			return ''
	else:
		return ''

OrderID = get_orderID()

def wait_shoot_list():
	api_url = HOST + "/api/Technician/UnFinishList"
	body = OrderSearchRequestPb()
	body.observationDate = today_horizon2str()
	body.observationLocationIDArray = 'E3773228-3C86-4CAE-AF22-AB6600E618D6'
	body = body.SerializeToString()
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
	
	# 解析结果
	data = PageResponsePb()
	data.ParseFromString(res.content)
	
	# 结果转为json
	res_json = MessageToJson(data)
	res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
	if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
		if 'unFinishList' in res_dict['data'][0]:
			print(res.status_code, res_dict['data'][0]['unFinishList'])
		else:
			print(res.status_code, 'unFinishList:[]')
	else:
		print(res.status_code)


def hang_list():
	api_url = HOST + "/api/Technician/UnFinishList"
	body = OrderSearchRequestPb()
	body.observationDate = today_horizon2str()
	body.observationLocationIDArray = 'E3773228-3C86-4CAE-AF22-AB6600E618D6'
	body = body.SerializeToString()
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
	
	# 解析结果
	data = PageResponsePb()
	data.ParseFromString(res.content)
	
	# 结果转为json
	res_json = MessageToJson(data)
	res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
	if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
		if 'hangUpList' in res_dict['data'][0]:
			print(res.status_code, res_dict['data'][0]['hangUpList'])
		else:
			print(res.status_code, 'hangUpList:[]')
	else:
		print(res.status_code, res_dict)


def finish_shoot_list():
	api_url = HOST + "/api/Technician/FinishList"
	body = OrderSearchRequestPb()
	body.observationEndDate = '2020-03-04 00:00:00|2020-03-04 23:59:59'  # 检查结束时间
	body.observationLocationIDArray = 'E3773228-3C86-4CAE-AF22-AB6600E618D6'
	body = body.SerializeToString()
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
	
	# 解析结果
	data = PageResponsePb()
	data.ParseFromString(res.content)
	
	# 结果转为json
	res_json = MessageToJson(data)
	res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
	if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
		print(res.status_code, res_dict['data'])
	else:
		print(res.status_code, 'data:[]')


def call_shoot():
	api_url = HOST + "/api/Exam/Load"
	r_body = SimpleOrderRequestPb()
	r_body.orderID = OrderID  # 从wait_shoot_list,获取
	if r_body.orderID:
		mr_body = SimpleOrderMessageRequestPb()
		mr_body.order.CopyFrom(r_body)
		mr_body = mr_body.SerializeToString()
		res = requests.request(method='POST', url=api_url, data=mr_body, headers=header)
		print('RT: %ss' % res.elapsed.total_seconds())
		# 解析结果
		data = PageResponsePb()
		data.ParseFromString(res.content)
		
		# 结果转为json
		res_json = MessageToJson(data)
		res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
		if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
			if 'orderInfo' in res_dict['data'][0]:
				print(res.status_code, res_dict['data'][0]['orderInfo'])
			else:
				print(res.status_code, 'orderInfo:[]')
		else:
			print(res.status_code, res_dict)
	else:
		pass


def shoot_start():
	api_url = HOST + "/api/Exam/Start"
	body = OrderSearchRequestPb()
	body.orderID = OrderID  # 从呼叫列表获取
	body = body.SerializeToString()
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
	print('RT: %ss' % res.elapsed.total_seconds())
	# 解析结果
	data = PageResponsePb()
	data.ParseFromString(res.content)
	
	# 结果转为json
	res_json = MessageToJson(data)
	res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
	if 'isSuccess' in res_dict.keys():
		if res_dict['isSuccess']:
			print(res.status_code, res_dict['isSuccess'])
	else:
		print(res.status_code, res_dict)


def shoot_finish():
	api_url = HOST + "/api/Exam/Finish"
	body = OrderSearchRequestPb()
	body.orderID = OrderID  # 从呼叫列表获取
	body = body.SerializeToString()
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
	print('RT: %ss' % res.elapsed.total_seconds())
	# 解析结果
	data = PageResponsePb()
	data.ParseFromString(res.content)
	
	# 结果转为json
	res_json = MessageToJson(data)
	res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
	if 'isSuccess' in res_dict.keys():
		if res_dict['isSuccess']:
			print(res.status_code, res_dict['isSuccess'])
	else:
		print(res.status_code, res_dict)


def permission():
	import json
	api_url = HOST + "/api/Organization/PermissionOrgList"
	body = {"organizationID": "0f4a7f80-b8ed-4d25-af02-ab7a009a7966",
			"observationDeptID": "f0ea6faf-dd09-43b6-bdd0-ab7a009b8633"}
	payload = json.dumps(body)
	res = requests.request(method='POST', url=api_url, headers=header, data=payload)
	print("permission返回---------")
	print(res.status_code, res.content)

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)


if __name__ == '__main__':
	# wait_shoot_list()
	# hang_list()
	call_shoot()
	shoot_start()
	shoot_finish()
	# permission()
	
	# print(curPath,rootPath,os.path.split(rootPath)[0])
	
