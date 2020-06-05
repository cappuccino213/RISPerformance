#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 11:14
# @Author  : Zhangyp
# @File    : LoginScript.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from locust import TaskSet, task, constant
from configuration.config import HOST, USERINFO, CONTENT_TYPE, INTERVAL, TOKEN
from locust.contrib.fasthttp import FastHttpLocust
from common.encryption import md5
import json


class LoginTaskSet(TaskSet):
	
	@task(1)  # 任务装饰器 括号里是执行权重为0时此任务不执行，不填默认为1，如@task则表示权重为1
	def login(self):
		api_url = HOST + "/api/Authorize/Validata"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': USERINFO}
		print(header)
		from login.proto_pb.AuthorizeRequestPb_pb2 import AuthorizeRequestPb
		ar_body = AuthorizeRequestPb()
		"""对象入参赋值"""
		ar_body.accountName = 'zyp'
		# ar_body.userPassWord = 'E10ADC3949BA59ABBE56E057F20F883E'
		ar_body.userPassWord = md5('123456')
		ar_body.organizationID = '93a6f377-717d-4dc3-a2ae-ab6600b6b2ab'
		ar_body.observationDeptID = 'aa688ecb-9f0c-439c-bcd1-ab6600b6edd9'
		ar_body = ar_body.SerializeToString()  # 将对象转化成字符串
		
		"""模拟客户端发出请求"""
		with self.client.request(method='POST', path=api_url, data=ar_body, headers=header, name='验证登录接口',
								 catch_response=True) as ar_res:  # 通过使用catch_response参数和with语句，即使响应代码正确，也可以将请求标记为失败
			
			"""解析返回结果"""
			from login.proto_pb.PageResponsePb_pb2 import PageResponsePb
			ar_data = PageResponsePb()  # 创建返回参数pb对象
			res_str = ar_res.content  # 获取返回的正文
			ar_data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
			from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
			from login.proto_pb.LoginUserInfoResponsePb_pb2 import LoginUserResponsePb  # 导入返回参数中的相关pb
			ar_json = MessageToJson(ar_data)
			ar_dict = json.loads(ar_json.encode('utf-8').decode("unicode_escape"))  # 先处理unicode成中文，然后转化成字典
			# print(ar_dict)
			"""校验结果是否正确"""
			if 'isSuccess' not in ar_dict.keys():  # 判断返回结果中是否有'isSuccess'，无，则一般是登录失败:
				ar_res.failure(ar_dict['resultDesc'])  # 将接口测试结果置为失败
				print(ar_dict['resultDesc'])
			elif ar_dict['isSuccess'] is False or ar_dict['data'] is None:  # 判断接口返回是否正确
				ar_res.failure("Got wrong response")  # 将接口测试结果置为失败
				print("Got wrong response")
			else:
				print(ar_res.status_code)
				print(ar_dict)
	
	@task(0)
	def cache(self):
		api_url = HOST + '/api/Cache/List'
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userinfo': USERINFO}
		from login.proto_pb.UserRequestPb_pb2 import UserRequestPb
		ur_body = UserRequestPb()
		ur_body.organizationID = '93a6f377-717d-4dc3-a2ae-ab6600b6b2ab'
		ur_body.observationDeptID = 'aa688ecb-9f0c-439c-bcd1-ab6600b6edd9'
		ur_body.currentPage = 1
		ur_body.pageSize = 10
		ur_body = ur_body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=ur_body, headers=header, name='缓存接口')
		
		from login.proto_pb.PageResponsePb_pb2 import PageResponsePb
		rp_data = PageResponsePb()
		rp_data.ParseFromString(res.content)
		
		from google.protobuf.json_format import MessageToJson
		from login.proto_pb.CacheListResponsePb_pb2 import CacheListResponsePb
		rp_json = MessageToJson(rp_data)
		print(res.status_code, rp_json.encode('utf-8').decode("unicode_escape"))


class User(FastHttpLocust):  # 模拟用户
	task_set = LoginTaskSet  # 设置用户任务
	wait_time = constant(INTERVAL)  # 执行任务后等待3秒
