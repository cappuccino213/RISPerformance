#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 14:44
# @Author  : Zhangyp
# @File    : IntegratedSearchScript.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from locust import TaskSet, task, constant
from locust.contrib.fasthttp import FastHttpLocust
from configuration.config import HOST, CONTENT_TYPE, USERINFO, TOKEN, INTERVAL


class SearchTaskSet(TaskSet):
	@task(1)
	def simple(self):  # 检查查询
		api_url = HOST + "/api/SimpleSearch/ObservationPageList"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': USERINFO}
		from search.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		"""对象入参赋值"""
		body.regDate = "2019-02-26|2020-02-25"
		# ar_body.observationEndDate = '1993-02-02|2020-03-17 23:59:55'
		body.currentPage = 1
		body.pageSize = 20
		body = body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='查询检查')
		
		"""解析返回结果"""
		print(res.status_code)
		from search.proto_pb.PageResponsePb_pb2 import PageResponsePb
		data = PageResponsePb()  # 创建返回参数pb对象
		res_str = res.content  # 获取返回的正文
		# print(res_str)
		data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
		from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
		from search.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb  # 导入返回参数中的相关pb
		res_json = MessageToJson(data)
		print(res_json.encode('utf-8').decode("unicode_escape"))
	
	@task(1)
	def report(self):  # 报告查询
		api_url = HOST + "/api/SimpleSearch/ReportPageList"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': USERINFO}
		from search.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		"""对象入参赋值"""
		body.preliminaryEndDate = "2019-02-26|2020-02-25"  # 报告书写时间
		# body.auditEndDate = "2019-02-26|2020-02-25"  # 审核时间
		body.currentPage = 1
		body.pageSize = 20
		body = body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='查询报告')
		"""解析返回结果"""
		print(res.status_code)
		from search.proto_pb.PageResponsePb_pb2 import PageResponsePb
		data = PageResponsePb()  # 创建返回参数pb对象
		res_str = res.content  # 获取返回的正文
		data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
		from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
		from search.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb  # 导入返回参数中的相关pb
		res_json = MessageToJson(data)
		print(res_json.encode('utf-8').decode("unicode_escape"))  # 宝
	
	@task(1)
	def defined(self):
		api_url = HOST + "/api/CustomSearch/List"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': USERINFO}
		
		from search.proto_pb.SysSearchDetailRequestPb_pb2 import SysSearchDetailRequestPb
		
		"""赋值第一层参数值"""
		ssdr_body = SysSearchDetailRequestPb()
		ssdr_body.detailID = "fbb4c43b-1f8f-4160-9226-ab6d00a83237"
		ssdr_body.solutionID = "14361cd1-2254-46da-a979-ab6d00a83201"
		ssdr_body.fieldName = "sex"
		ssdr_body.compareSign = "="
		ssdr_body.compareValue = "M"
		ssdr_body.compareValueType = "0"
		ssdr_body.fieldDisplayName = "性别"
		ssdr_body.fieldType = 3
		ssdr_body.inputStyle = 1
		ssdr_body.multiSelectFlag = True
		ssdr_body.dicCategory = "1080"
		ssdr_body.fieldSortNo = 1
		
		"""追加第二层参数值"""
		from search.proto_pb.SysSearchListRequestPb_pb2 import SysSearchListRequestPb
		sslr_body = SysSearchListRequestPb()
		sslr_body.details.append(ssdr_body)
		sslr_body = sslr_body.SerializeToString()
		
		res = self.client.request(method='POST', path=api_url, data=sslr_body, headers=header, name='自定义查询')
		olr_code = res.status_code
		olr_str = res.content
		print(olr_code, olr_str)


class User(FastHttpLocust):
	task_set = SearchTaskSet
	wait_time = constant(INTERVAL)
