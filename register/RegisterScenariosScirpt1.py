#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 17:06
# @Author  : Zhangyp
# @File    : RegisterScenariosScirpt1.py.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from locust import TaskSequence, seq_task, task, between, TaskSet
from locust.contrib.fasthttp import FastHttpLocust
from configuration.config import HOST, CONTENT_TYPE, TOKEN, WEB
from common.RandomData import REGINFO, REG, SERVICESECTID, PROCINFO, ORDERID
from common.DateTimeData import today_horizon2str, within3days
from random import choice
import requests


class RegisterTaskSet(TaskSet):
	
	"""进入登记工作站预加载项目"""
	
	# @seq_task()
	"""获取急诊时间段"""
	
	@task(1)
	def emergency_period(self):
		api_url = HOST + "/api/EmergecyPeriod/List"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO, 'Content-Length': '0'}
		res = self.client.request(method='POST', path=api_url, data=None, headers=header, name='p获取急诊时间段')
		# from register.proto_pb.PageResponsePb_pb2 import PageResponsePb
		# data = PageResponsePb()
		# res_str = res.content
		# data.ParseFromString(res_str)
		# from google.protobuf.json_format import MessageToJson
		# from register.proto_pb.EmergecyPeriodResponsePb_pb2 import EmergecyPeriodResponsePb  # 导入返回参数中的相关pb
		# res_json = MessageToJson(data)
		# print(res.status_code, res_json)
		print(res.status_code, res.content)
	
	"""获取检查项目树"""
	
	@task(1)
	def procedure_tree(self):
		api_url = HOST + "/api/Procedure/Tree"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.ProcedureRequestPb_pb2 import ProcedureRequestPb
		body = ProcedureRequestPb()
		body.organizationID = REG['organizationID']
		body.observationDeptID = REG['observationDeptID']
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='p获取检查项目树')
		print(res.status_code, res.content)
	
	"""获取绑定机房"""
	
	@task(1)
	def location_bind(self):
		api_url = HOST + "/api/ObservationLocation/BindUsable"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.ObservationLocationRequestPb_pb2 import ObservationLocationRequestPb
		body = ObservationLocationRequestPb()
		body.organizationID = REG['organizationID']
		body.observationDeptID = REG['observationDeptID']
		body.serviceSectID = choice(SERVICESECTID)
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='p获取绑定机房')
		print(res.status_code, res.content)
	
	"""获取申请科室"""
	
	@task(1)
	def request_org(self):
		api_url = HOST + "/api/RequestOrg/List"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO, 'Content-Length': '0'}
		res = self.client.request(method='POST', path=api_url, data=None, headers=header, name='p获取申请科室')
		print(res.status_code, res.content)
	
	"""获取年龄单位"""
	
	@task(1)
	def age_unit(self):
		api_url = HOST + "/api/Order/AgeUnit"
		# header = {'content-type': 'application/octet-stream', 'Authorization': TOKEN, 'userInfo': REGINFO,
		# 		  'Content-Length': 0}
		header = {'content-type': 'application/octet-stream', 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.OrderRequestPb_pb2 import OrderRequestPb
		body = OrderRequestPb()
		body.organizationID = REG['organizationID']
		body.observationDeptID = REG['observationDeptID']
		body = body.SerializeToString()
		# s = self.client
		# s.keep_alive = False
		try:
			res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='p获取年龄单位',
									  timeout=10, stream=False)
			print('p获取年龄单位----------')
			print(res.status_code, res.content)
		except requests.exceptions.ConnectionError:
			status_code = "Connection refused"
			print('p获取年龄单位----------')
			print(status_code)
	
	"""获取号码类型"""
	
	@task(1)
	def number_type(self):
		api_url = HOST + "/api/Search/NumberType"
		header = {'content-type': 'application/octet-stream', 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.SearchTypeRequestPb_pb2 import SearchTypeRequestPb
		body = SearchTypeRequestPb()
		body.listName = 'ElectronicOrderList'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='p登记界面号码类型下拉列表',
								  timeout=10, stream=False)
		print('p登记界面号码类型下拉列表-------------')
		print(res.status_code, res.content)
	
	
	"""登记检查、取消检查"""

	"""改变检查类型"""
	
	# 快捷代码
	@task(0)
	def procedure_code(self):
		api_url = HOST + "/api/QuickProcedure/Get"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.ProcedureRequestPb_pb2 import ProcedureRequestPb
		body = ProcedureRequestPb()
		body.organizationID = REG['organizationID']
		body.observationDeptID = REG['observationDeptID']
		body.serviceSectID = choice(SERVICESECTID)
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='r获取检查项目快捷输入码接口',
								  timeout=10)
		print(res.status_code, res.content)
	
	# 检查机房
	@task(1)
	def valid_location(self):
		api_url = HOST + "/api/ObservationLocation/BindUsable"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.ObservationLocationRequestPb_pb2 import ObservationLocationRequestPb
		body = ObservationLocationRequestPb()
		body.organizationID = REG['organizationID']
		body.observationDeptID = REG['observationDeptID']
		body.serviceSectID = choice(SERVICESECTID)
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='r查找可用机房')
		print(res.status_code, res.content)
	
	"""登记检查信息"""
	
	@task(4)
	def register(self):
		api_url = HOST + "/api/Order/Create"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.OrderRequestPb_pb2 import OrderRequestPb
		"""导入两个造数据的类"""
		from common.DataWarehouse import PersonData, RISData
		person_data = PersonData()
		"""赋值第一层参数值"""
		body = OrderRequestPb()
		body.observationDeptID = REG['observationDeptID']
		body.organizationID = REG['organizationID']
		body.serviceSectID = choice(SERVICESECTID)
		body.name = person_data.name
		body.nameSpell = person_data.name_spell
		body.sex = person_data.sex
		body.birthDate = person_data.birth_date.strftime('%Y-%m-%d')
		body.patientClass = RISData.patient_class()
		body.age = person_data.age
		body.ageUnit = '岁'
		body.chargeFlag = 1
		body.charges = 60
		body.observationLocationID = PROCINFO['observationLocationID']
		body.observationLocation = PROCINFO['observationLocation']
		body.examBodyPart = PROCINFO['examBodyPart']
		body.examBodyPartID = PROCINFO['examBodyPartID']
		body.procedureID = PROCINFO['procedureID']
		body.procedureName = PROCINFO['procedureName']
		body.procedureWorkload = PROCINFO['procedureWorkload']
		body.diagnosticGroupID = PROCINFO['diagnosticGroupID']
		body.allProcedureName = PROCINFO['allProcedureName']
		"""追加第二层参数值"""
		from register.proto_pb.OrderListRequestPb_pb2 import OrderListRequestPb
		olr_body = OrderListRequestPb()
		olr_body.datas.append(body)
		olr_body = olr_body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=olr_body, headers=header, name='r新增患者信息',
								  timeout=10, stream=False)
		print('r新增患者信息---------')
		print(res.status_code, res.content)
	
	"""取消检查"""
	
	@task(0)
	def cancel(self):
		api_url = HOST + "/api/Order/Cancel"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.OrderCancelRequestPb_pb2 import OrderCancelRequestPb
		body = OrderCancelRequestPb()
		print(REG['organizationID'])
		body.orderID = ORDERID
		body.cancelReason = '接口测试'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='r取消检查')
		print(res.status_code, res.content)
	
	
	"""患者列表查询"""
	
	"""今日患者查询"""
	
	# @task()
	@task(2)
	def today_patient(self):
		api_url = HOST + "/api/Patient/PageList"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO, 'Connection': 'close'}
		from register.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		body.regDate = today_horizon2str()
		body.currentPage = 1
		body.pageSize = 10
		body = body.SerializeToString()
		try:
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='s今日登记患者查询',
									  timeout=10, stream=False)
			print('s今日登记患者查询-------')
			# from register.proto_pb.PageResponsePb_pb2 import PageResponsePb
			# data = PageResponsePb()
			# data.ParseFromString(res.content)
			# from register.proto_pb.OrderStaticListResponsePb_pb2 import OrderStaticListResponsePb
			# from google.protobuf.json_format import MessageToJson
			# res_json = MessageToJson(data)
			# print(res.status_code, res_json)
			print(res.status_code, res.content)
		except requests.exceptions.ConnectionError:
			status_code = "Connection refused"
			print('s今日登记患者查询-------')
			print(status_code)
	
	"""患者查询"""
	
	@task(2)
	# @task(0)
	def order_search(self):
		api_url = HOST + "/api/Order/PageList"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		body.regDate = today_horizon2str()
		# 预检时间、检查时间也可以查询
		# body.observationDate = '2020-03-18|2020-03-18'
		# body.observationEndDate = '2020-03-18|2020-03-18'
		body.currentPage = 1
		body.pageSize = 10
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='s患者查询', timeout=10,
								  stream=False)
		print('s患者查询----------')
		# from register.proto_pb.PageResponsePb_pb2 import PageResponsePb
		# data = PageResponsePb()
		# data.ParseFromString(res.content)
		# from register.proto_pb.OrderStaticListResponsePb_pb2 import OrderStaticListResponsePb
		# from google.protobuf.json_format import MessageToJson
		# res_json = MessageToJson(data)
		# print(res.status_code, res_json)
		print(res.status_code, res.content)
	
	"""机房统计"""
	
	@task(1)
	def examine_count(self):
		api_url = HOST + "/api/LocationStatic/ExamineCount"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REGINFO}
		from register.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		body.regStartDate = within3days().split("|")[0]  # 三天前
		body.regEndDate = within3days().split("|")[-1]  # 今天23点
		# body.serviceSectID = 'CT'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='s机房统计')
		# from register.proto_pb.PageResponsePb_pb2 import PageResponsePb
		# data = PageResponsePb()
		# data.ParseFromString(res.content)
		# from google.protobuf.json_format import MessageToJson
		# from register.proto_pb.LocationExamineCountListResponsePb_pb2 import LocationExamineCountListResponsePb
		# res_json = MessageToJson(data)
		# print(res.status_code)
		# print(res_json.encode('utf-8').decode("unicode_escape"))
		print(res.status_code, res.content)
	
	"""机房统计详情"""
	
	@task(1)
	def examine_details(self):
		api_url = HOST + "/api/LocationStatic/ExamineDetail"
		header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userinfo': REGINFO}
		from register.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
		body = OrderSearchRequestPb()
		body.regStartDate = within3days().split("|")[0]  # 三天前
		body.regEndDate = within3days().split("|")[-1]  # 今天23点
		body.observationLocationID = PROCINFO['observationLocationID']  # 检查机房
		# body.resultStatus = 0
		body.currentPage = 1
		body.pageSize = 10
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='s机房统计详情')
		# from register.proto_pb.PageResponsePb_pb2 import PageResponsePb
		# data = PageResponsePb()
		# data.ParseFromString(res.content)
		# from google.protobuf.json_format import MessageToJson
		# from register.proto_pb.OrderResponsePb_pb2 import OrderResponsePb
		# res_json = MessageToJson(data)
		# print(res.status_code)
		# print(res_json.encode('utf-8').decode("unicode_escape"))
		print(res.status_code, res.content)
	


class User(FastHttpLocust):
	task_set = RegisterTaskSet
	wait_time = between(3, 10)  # 思考时间3到10s之间


def start():
	import subprocess
	# cli = "locust -f %s -H %s --web-host %s -P %s" % (SCRIPT, HOST, WEB, PORT)
	cli = "locust -f RegisterScenariosScirpt1.py -H %s --master --web-host %s -P %s" % (HOST, WEB, 8188)
	try:
		cl = subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
		print(cl.stdout.readlines())  # 打印控制台信息
	except Exception as e:
		raise str(e)


if __name__ == '__main__':
	start()