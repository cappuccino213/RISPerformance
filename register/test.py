#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 17:36
# @Author  : Zhangyp
# @File    : test.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from configuration.config import HOST,  CONTENT_TYPE, TOKEN, INTERVAL
from common.DateTimeData import today_horizon2str
from common.RandomData import REGINFO,REG
from common.DataWarehouse import PersonData, RISData
from requests import request, exceptions


def today_patient():
	api_url = HOST + "/api/Patient/PageList"
	header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO, 'Connection': 'close'}
	from register.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
	body = OrderSearchRequestPb()
	body.regDate = today_horizon2str()
	body.currentPage = 1
	body.pageSize = 10
	body = body.SerializeToString()
	try:
		res = request(method='POST', url=api_url, data=body, headers=header, timeout=10, stream=False)
		print('s今日登记患者查询-------')
		# from register.proto_pb.PageResponsePb_pb2 import PageResponsePb
		# data = PageResponsePb()
		# data.ParseFromString(res.content)
		# from register.proto_pb.OrderStaticListResponsePb_pb2 import OrderStaticListResponsePb
		# from google.protobuf.json_format import MessageToJson
		# res_json = MessageToJson(data)
		# print(res.status_code, res_json)
		print(res.status_code, res.content)
		print('RT: %ss' % res.elapsed.total_seconds())
	except exceptions.ConnectionError:
		status_code = "Connection refused"
		print('s今日登记患者查询-------')
		print(status_code)


def procedure_tree():
	api_url = HOST + "/api/Procedure/Tree"
	header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
	from register.proto_pb.ProcedureRequestPb_pb2 import ProcedureRequestPb
	body = ProcedureRequestPb()
	body.organizationID = REG['organizationID']
	body.observationDeptID = REG['observationDeptID']
	body = body.SerializeToString()
	res = request(method='POST', url=api_url, data=body, headers=header)
	print('p获取检查项目树--------')
	print('RT: %ss' % res.elapsed.total_seconds())
	print(res.status_code, res.content)

if __name__ == '__main__':
	today_patient()
	procedure_tree()
