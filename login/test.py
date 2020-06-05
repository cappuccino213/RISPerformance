#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 15:14
# @Author  : Zhangyp
# @File    : test.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from configuration.config import HOST, USERINFO, CONTENT_TYPE, TOKEN
from common.RandomData import REG,REGINFO
import requests
import json
def validate():
	api_url = HOST + "/api/Authorize/Validata"
	header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': USERINFO}
	print(header)
	from login.proto_pb.AuthorizeRequestPb_pb2 import AuthorizeRequestPb
	body = AuthorizeRequestPb()  # 声明入参对象
	"""对象入参赋值"""
	# print(REG)
	body.accountName = REG['accountName']
	body.userPassWord = REG['userPassWord']
	body.organizationID = '47D09C44-BCF7-40BB-AC88-AB7A009CB4B6'
	body.observationDeptID = '668F4A1C-537C-4C56-859E-AB7A009CCDE3'
	body = body.SerializeToString()  # 将对象转化成字符串
	
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
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
		return res_dict['data'][0]
	else:
		print(res.status_code, res_dict)
		return {}

def cache():
	api_url = HOST + '/api/Cache/List'
	header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
	from login.proto_pb.UserRequestPb_pb2 import UserRequestPb
	body = UserRequestPb()
	body.organizationID = REG['organizationID']
	body.observationDeptID = REG['observationDeptID']
	body.currentPage = 1
	body.pageSize = 10
	body = body.SerializeToString()
	res = requests.request(method='POST', url=api_url, data=body, headers=header)
	from login.proto_pb.PageResponsePb_pb2 import PageResponsePb
	data = PageResponsePb()
	data.ParseFromString(res.content)
	from google.protobuf.json_format import MessageToJson
	from login.proto_pb.CacheListResponsePb_pb2 import CacheListResponsePb
	rp_json = MessageToJson(data)
	print(res.status_code, rp_json.encode('utf-8').decode("unicode_escape"))

if __name__ == '__main__':
	# validate()
	cache()