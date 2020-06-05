#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 14:34
# @Author  : Zhangyp
# @File    : LoginScenariosScript.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSequence, seq_task, task, constant
from configuration.config import HOST, CONTENT_TYPE, INTERVAL, TOKEN
from common.RandomData import USERINFO, REG, REGINFO
from locust.contrib.fasthttp import FastHttpLocust
import json


class LoginTaskSet(TaskSequence):

	"""加载页面"""
	@task
	class LoginPageLoad(TaskSequence):
		"""获取机构"""
		@task
		def organization(self):
			pass
		
		"""获取科室"""
		
		@task
		def organization_dept(self):
			pass
		
	"""登录操作"""
	@task
	class Login(TaskSequence):
		
		"""登录验证"""
		
		@task(1)
		@seq_task(1)
		def validate(self):
			api_url = HOST + "/api/Authorize/Validata"
			header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': USERINFO}
			# print(USERINFO)
			from login.proto_pb.AuthorizeRequestPb_pb2 import AuthorizeRequestPb
			body = AuthorizeRequestPb()  # 声明入参对象
			"""对象入参赋值"""
			body.accountName = REG['accountName']
			body.userPassWord = REG['userPassWord']
			body.organizationID = REG['organizationID']
			body.observationDeptID = REG['observationDeptID']
			body = body.SerializeToString()  # 将对象转化成字符串
			"""发出请求"""
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='验证登录接口')
			"""解析返回结果"""
			from login.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()  # 创建返回参数pb对象
			res_str = res.content  # 获取返回的正文
			data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
			from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
			from login.proto_pb.LoginUserInfoResponsePb_pb2 import LoginUserResponsePb  # 导入返回参数中的相关pb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))  # 先处理unicode成中文，然后转化成字典
			if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
				print(res.status_code, res_dict['data'], '登录验证成功')
			# return res_dict['data'][0]
			else:
				print(res.status_code, res_dict)
			# return {}
		
		"""加载缓存"""
		
		@task(1)
		@seq_task(2)
		def cache(self):
			api_url = HOST + '/api/Cache/List'
			header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
			# print(REG)
			from login.proto_pb.UserRequestPb_pb2 import UserRequestPb
			body = UserRequestPb()
			body.organizationID = REG['organizationID']
			body.observationDeptID = REG['observationDeptID']
			body.currentPage = 1
			body.pageSize = 10
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='缓存接口')
			from login.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			from google.protobuf.json_format import MessageToJson
			from login.proto_pb.CacheListResponsePb_pb2 import CacheListResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json)
			if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
				print(res.status_code, res_dict['data'], '加载缓存成功')
			else:
				print(res.status_code, res_dict)


class User(FastHttpLocust):
	task_set = LoginTaskSet
	wait_time = constant(INTERVAL)
