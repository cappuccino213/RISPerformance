#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 13:58
# @Author  : Zhangyp
# @File    : TechinScript.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import seq_task, task, constant, TaskSequence, TaskSet
from locust.contrib.fasthttp import FastHttpLocust
from configuration.config import HOST, USERINFO, CONTENT_TYPE, TOKEN, INTERVAL
from common.DateTimeData import today_horizon2str
from google.protobuf.json_format import MessageToJson
import json
import requests
import random

# 声明头信息
header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': USERINFO}


class TechinTaskSet(TaskSequence):
	"""查询等待摄片列表"""
	
	@task(2)
	def wait_shoot_list(self):
		api_url = HOST + "/api/Technician/UnFinishList"
		from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		body.observationDate = today_horizon2str()
		body.observationLocationIDArray = 'E3773228-3C86-4CAE-AF22-AB6600E618D6'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='查询等待摄片列表')
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
				print(res.status_code, res_dict['data'][0]['unFinishList'])
			else:
				print(res.status_code, '无查询数据')
		else:
			print(res.status_code, res_dict)
	
	"""查询挂起列表"""
	
	@task(1)
	def hang_list(self):
		api_url = HOST + "/api/Technician/UnFinishList"
		from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		body.observationDate = today_horizon2str()
		body.observationLocationIDArray = 'E3773228-3C86-4CAE-AF22-AB6600E618D6'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='查询挂起列表')
		# 解析结果
		from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
		data = PageResponsePb()
		data.ParseFromString(res.content)
		# 结果转为json
		from techin.proto_pb.ObservationListResponsePb_pb2 import ObservationListResponsePb
		res_json = MessageToJson(data)
		res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
		if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
			if 'hangUpList' in res_dict['data'][0]:
				print(res.status_code, res_dict['data'][0]['hangUpList'])
			else:
				print(res.status_code, '无查询数据')
		else:
			print(res.status_code, res_dict)
	
	"""查询完成摄片列表"""
	
	@task(2)
	def finish_shoot_list(self):
		api_url = HOST + "/api/Technician/FinishList"
		from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		# body.observationEndDate = '2020-03-04 00:00:00|2020-03-04 23:59:59'  # 检查结束时间
		body.observationEndDate = today_horizon2str()  # 检查结束时间
		body.observationLocationIDArray = 'E3773228-3C86-4CAE-AF22-AB6600E618D6'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='查询完成列表')
		# 解析结果
		from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
		data = PageResponsePb()
		data.ParseFromString(res.content)
		# 结果转为json
		from techin.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb
		res_json = MessageToJson(data)
		res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
		if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
			print(res.status_code, res_dict['data'])
		else:
			print(res.status_code, res_dict)
	
	"""选呼-开始-完成"""
	
	@task(4)
	class CallTaskSet(TaskSequence):
		
		def __init__(self, parent):
			super().__init__(parent)
			self.orderID = self.get_orderID()
		
		# 获取列表的检查ID
		# @staticmethod
		def get_orderID(self):
			api_url = HOST + "/api/Technician/UnFinishList"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.observationDate = today_horizon2str()
			body.observationLocationIDArray = 'E3773228-3C86-4CAE-AF22-AB6600E618D6'
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
		
		@seq_task(1)
		# @task
		def call_shoot(self):
			api_url = HOST + "/api/Exam/Load"
			from techin.proto_pb.SimpleOrderRequestPb_pb2 import SimpleOrderRequestPb
			r_body = SimpleOrderRequestPb()
			r_body.orderID = self.orderID
			if r_body.orderID:
				from techin.proto_pb.SimpleOrderMessageRequestPb_pb2 import SimpleOrderMessageRequestPb
				mr_body = SimpleOrderMessageRequestPb()
				mr_body.order.CopyFrom(r_body)
				mr_body = mr_body.SerializeToString()
				res = self.client.request(method='POST', path=api_url, data=mr_body, headers=header, name='呼叫检查')
				# 解析结果
				from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
				data = PageResponsePb()
				data.ParseFromString(res.content)
				from techin.proto_pb.ExamLoadResponsePb_pb2 import ExamLoadResponsePb
				res_json = MessageToJson(data)
				res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
				if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
					if 'orderInfo' in res_dict['data'][0]:
						print(res.status_code, '呼叫成功', res_dict['data'][0]['orderInfo'])
					else:
						print(res.status_code, '呼叫失败')
				else:
					print(res.status_code, res_dict)
			else:
				print('当前没有检查可呼叫')
		
		@seq_task(2)
		# @task
		def exam_start(self):
			api_url = HOST + "/api/Exam/Start"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.orderID = self.orderID
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='开始检查')
			# 解析结果
			from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			# 结果转为json
			from techin.proto_pb.FinishExamResponsePb_pb2 import FinishExamResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
			if 'isSuccess' in res_dict.keys():
				if res_dict['isSuccess']:
					print(res.status_code, '检查开始成功', res_dict['isSuccess'])
			else:
				print(res.status_code, '检查开始失败')
		
		@seq_task(3)
		# @task
		def exam_end(self):
			api_url = HOST + "/api/Exam/Finish"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.orderID = self.orderID  # 从呼叫列表获取
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='检查完成')
			# 解析结果
			from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			# 结果转为json
			from techin.proto_pb.FinishExamResponsePb_pb2 import FinishExamResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
			if 'isSuccess' in res_dict.keys():
				if res_dict['isSuccess']:
					print(res.status_code, '完成检查', res_dict['isSuccess'])
			else:
				print(res.status_code, '检查完成失败')


class User(FastHttpLocust):  # 模拟用户
	task_set = TechinTaskSet  # 设置用户任务
	wait_time = constant(INTERVAL)  # 执行任务后等待3秒
