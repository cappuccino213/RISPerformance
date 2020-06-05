#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 10:40
# @Author  : Zhangyp
# @File    : ReportScript.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSet, task, constant, seq_task, TaskSequence
from configuration.config import HOST, TOKEN, USERINFO2, INTERVAL
import json
from locust.contrib.fasthttp import FastHttpLocust


class ReportTaskSet(TaskSequence):  # 定义任务
	"""获取报告工作列表接口"""
	
	@seq_task(4)
	@task(4)  # 任务装饰器
	def PageList(self):
		api_url = HOST + "/api/ReportList/PageList"
		header = {'content-type': 'application/octet-stream',  # 头信息
				  'Authorization': TOKEN,
				  'userinfo': USERINFO2}
		
		from report.proto_pb.ViOrderReportRequestPb_pb2 import ViOrderReportRequestPb
		ar_body = ViOrderReportRequestPb()
		"""对象入参赋值"""
		ar_body.observationEndDate = '2020-02-20 00:00:00|2020-02-24 23:59:59'
		ar_body.currentPage = 1
		ar_body.pageSize = 20
		ar_body = ar_body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		with self.client.request(method='POST', path=api_url, data=ar_body, headers=header, name='获取报告工作列表接口',
								 timeout=5,
								 catch_response=True) as ar_res:  # 通过使用catch_response参数和with语句，即使响应代码正确，也可以将请求标记为失败
			
			"""解析返回结果"""
			# print(ar_res)
			# print(ar_res.status_code)
			from report.proto_pb.PageResponsePb_pb2 import PageResponsePb
			ar_data = PageResponsePb()  # 创建返回参数pb对象
			res_str = ar_res.content  # 获取返回的正文
			# print(res_str)
			# print(ar_data)
			ar_data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
			from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
			from report.proto_pb.ReportListResponsePb_pb2 import ReportListResponsePb  # 导入返回参数中的相关pb
			ar_json = MessageToJson(ar_data)
			ar_dict = json.loads(ar_json.encode('utf-8').decode("unicode_escape"),
								 strict=False)  # 先处理unicode成中文，然后转化成字典
			# print(ar_json)
			# print(ar_data)
			"""校验结果是否正确"""
			if 'isSuccess' not in ar_dict.keys():  # 判断返回结果中是否有'isSuccess'，无，则一般是登录失败:
				ar_res.failure(ar_dict['resultDesc'])  # 将接口测试结果置为失败
				print(ar_dict['resultDesc'])
			elif ar_dict['isSuccess'] is False or ar_dict['data'] is None:  # 判断接口返回是否正确
				ar_res.failure("Got wrong response")  # 将接口测试结果置为失败
				print("Got wrong response")
			else:
				print(ar_dict)
	
	"""加载报告接口"""
	
	@seq_task(3)
	@task(1)  # 任务装饰器
	def Loading(self):
		api_url = HOST + "/api/Report/Loading"
		header = {'content-type': 'application/octet-stream',  # 头信息
				  'Authorization': TOKEN,
				  'userinfo': USERINFO2}
		
		from report.proto_pb.ReportRequestPb_pb2 import ReportRequestPb
		rr_body = ReportRequestPb()
		"""对象入参赋值"""
		rr_body.orderID = 'f0ec2f21-1bc9-4a31-8d80-ab6700ab7241'
		from report.proto_pb.OrderReportRequestPb_pb2 import OrderReportRequestPb
		orr_body = OrderReportRequestPb()
		orr_body.report.CopyFrom(rr_body)
		orr_body = orr_body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		with self.client.request(method='POST', path=api_url, data=orr_body, headers=header, name='加载报告接口',
								 catch_response=True) as ar_res:  # 通过使用catch_response参数和with语句，即使响应代码正确，也可以将请求标记为失败
			
			# ar_res = requests.request(method='POST', url=api_url, data=orr_body, headers=header,timeout=5)
			
			"""解析返回结果"""
			print(ar_res)
			from report.proto_pb.ReportWriteListResponsePb_pb2 import ReportWriteListResponsePb
			ar_data = ReportWriteListResponsePb()  # 创建返回参数pb对象
			res_str = ar_res.content  # 获取返回的正文
			print(res_str)
			print(ar_res.status_code)
	
	"""报告签名接口"""
	
	@seq_task(3)
	@task(1)  # 任务装饰器
	def Signature(self):
		api_url = HOST + "/api/Report/Signature"
		header = {'content-type': 'application/octet-stream',  # 头信息
				  'Authorization': TOKEN,
				  'userinfo': USERINFO2}
		
		from report.proto_pb.ReportRequestPb_pb2 import ReportRequestPb
		rr_body = ReportRequestPb()
		"""对象入参赋值"""
		rr_body.orderID = 'f0ec2f21-1bc9-4a31-8d80-ab6700ab7241'
		rr_body.reportID = 'dbedc9d1-3813-46e9-b69c-ab6700b19bc9'
		rr_body.abnormalFlag = '0'
		rr_body.imagingFinding = '两边见到了没什么东西'
		rr_body.imagingDiagnosis = '没问题'
		rr_body.isCheckedWriteAndAudit = 1
		from report.proto_pb.OrderReportRequestPb_pb2 import OrderReportRequestPb
		orr_body = OrderReportRequestPb()
		orr_body.report.CopyFrom(rr_body)
		orr_body = orr_body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		with self.client.request(method='POST', path=api_url, data=orr_body, headers=header, name='报告签名接口',
								 catch_response=True) as ar_res:  # 通过使用catch_response参数和with语句，即使响应代码正确，也可以将请求标记为失败
			
			"""解析返回结果"""
			print(ar_res)
			res_str = ar_res.content  # 获取返回的正文
			print(res_str)
	
	"""超时报告手动结果接口"""
	
	@task(1)  # 任务装饰器
	def TimeoutReport(self):
		api_url = HOST + "/api/TimeoutReport/PageList"
		header = {'content-type': 'application/octet-stream',  # 头信息
				  'Authorization': TOKEN,
				  'userinfo': USERINFO2}
		
		from report.proto_pb.ReportConditionRequestPb_pb2 import ReportConditionRequestPb
		rcr_body = ReportConditionRequestPb()
		"""对象入参赋值"""
		rcr_body.initiative = 1
		rcr_body.pageSize = 20
		rcr_body.pageIndex = 1
		rcr_body.gapTime = 30
		rcr_body.regDate = '2020-02-19 00:00:00|2020-02-25 23:59:59'
		rcr_body = rcr_body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		with self.client.request(method='POST', path=api_url, data=rcr_body, headers=header, name='超时报告手动结果接口',
								 catch_response=True) as ar_res:  # 通过使用catch_response参数和with语句，即使响应代码正确，也可以将请求标记为失败
			
			"""解析返回结果"""
			print(ar_res)
			from report.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb
			ar_data = ViOrderReportResponsePb()  # 创建返回参数pb对象
			res_str = ar_res.content  # 获取返回的正文
			print(res_str)
			print(ar_data)
			ar_data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
			from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
			ar_json = MessageToJson(ar_data)
			ar_dict = json.loads(ar_json.encode('utf-8').decode("unicode_escape"),
								 strict=False)  # 先处理unicode成中文，然后转化成字典
			print(ar_json)
			print(ar_data)
	
	# """校验结果是否正确"""
	# if 'isSuccess' not in ar_dict.keys():  # 判断返回结果中是否有'isSuccess'，无，则一般是登录失败:
	#     ar_res.failure(ar_dict['resultDesc'])  # 将接口测试结果置为失败
	#     print(ar_dict['resultDesc'])
	# elif ar_dict['isSuccess'] is False or ar_dict['data'] is None:  # 判断接口返回是否正确
	#     ar_res.failure("Got wrong response")  # 将接口测试结果置为失败
	#     print("Got wrong response")
	# else:
	#     print(ar_dict)
	
	"""超时报告被动结果接口"""
	
	@task(1)  # 任务装饰器
	def TimeoutReport2(self):
		api_url = HOST + "/api/TimeoutReport/PageList"
		header = {'content-type': 'application/octet-stream',  # 头信息
				  'Authorization': TOKEN,
				  'userinfo': USERINFO2}
		
		from report.proto_pb.ReportConditionRequestPb_pb2 import ReportConditionRequestPb
		rcr_body = ReportConditionRequestPb()
		"""对象入参赋值"""
		rcr_body.initiative = 0
		rcr_body.pageSize = 20
		rcr_body.pageIndex = 1
		rcr_body = rcr_body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		with self.client.request(method='POST', path=api_url, data=rcr_body, headers=header, name='超时报告被动结果接口',
								 catch_response=True) as ar_res:  # 通过使用catch_response参数和with语句，即使响应代码正确，也可以将请求标记为失败
			
			"""解析返回结果"""
			print(ar_res)
			from report.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb
			ar_data = ViOrderReportResponsePb()  # 创建返回参数pb对象
			res_str = ar_res.content  # 获取返回的正文
			print(res_str)
			print(ar_data)
			ar_data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
			from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
			ar_json = MessageToJson(ar_data)
			ar_dict = json.loads(ar_json.encode('utf-8').decode("unicode_escape"),
								 strict=False)  # 先处理unicode成中文，然后转化成字典
			print(ar_json)
			print(ar_data)


class User(FastHttpLocust):  # 模拟用户
	task_set = ReportTaskSet  # 设置用户任务
	# wait_time = between(1, 60)  # 模拟用户在每次执行任务后等待介于1~60s（最小值和最大值）之间的随机时间
	wait_time = constant(INTERVAL)  # 执行任务后等待3秒
