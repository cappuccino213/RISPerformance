#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 9:53
# @Author  : Zhangyp
# @File    : TechinScenariosScript.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSequence, TaskSet, seq_task, task, between
from locust.contrib.fasthttp import FastHttpLocust
from configuration.config import HOST, CONTENT_TYPE, TOKEN
from common.RandomData import TECINFO, TEC, PROCINFO
from common.DateTimeData import today_horizon2str
from google.protobuf.json_format import MessageToJson
import json
from configuration.config import HOST, WEB

header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': TECINFO}
none_header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': TECINFO, 'Content-Length': '0'}


class TechinTaskSet(TaskSet):
	"""进入技师工作站初始化接口"""
	
	@task(1)
	class PreLoad(TaskSequence):
		
		@task
		def search_date_type(self):
			api_url = HOST + "/api/Search/DateType"
			from techin.proto_pb.SearchTypeRequestPb_pb2 import SearchTypeRequestPb
			body = SearchTypeRequestPb()
			body.listName = 'ReportList'
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='p完成列表时间类型下拉')
			print("search_date_type返回---------")
			print(res.status_code, res.content)
		
		@task
		def related_examine(self):
			api_url = HOST + "/api/RelatedExamine/Parameter"
			res = self.client.request(method='POST', path=api_url, headers=none_header, data=None, name='p相关检查参数')
			print("related_examine返回---------")
			print(res.status_code, res.content)
		
		@task
		def usable_room(self):
			api_url = HOST + "/api/Room/UsableList"
			from techin.proto_pb.UserRequestPb_pb2 import UserRequestPb
			body = UserRequestPb()
			body.userID = TEC['userID']
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='p获取可用机房列表')
			print("usable_room返回---------")
			print(res.status_code, res.content)
		
		@task
		def number_type(self):
			api_url = HOST + "/api/Search/NumberType"
			from techin.proto_pb.SearchTypeRequestPb_pb2 import SearchTypeRequestPb
			body = SearchTypeRequestPb()
			body.listName = 'UnFinishShootList'
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='p等待列表号码类型下拉')
			print("number_type返回---------")
			print(res.status_code, res.content)
		
		"""阻塞列表"""
		
		@task
		def block_list(self):
			api_url = HOST + "/api/ManualCompare/BlockList"
			# from techin.proto_pb.BlockRequestPb_pb2 import BlockRequestPb
			# body = BlockRequestPb()
			# body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, headers=none_header, data=None, name='p阻塞列表')
			print("block_list返回---------")
			print(res.status_code, res.content)
		
		@task
		def request_org(self):
			api_url = HOST + "/api/RequestOrg/List"
			res = self.client.request(method='POST', path=api_url, headers=none_header, data=None, name='p申请科室')
			print("request_org返回---------")
			print(res.status_code, res.content)
		
		@task(0)
		def procedure_tree(self):
			api_url = HOST + "/api/Procedure/Tree"
			header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': TECINFO}
			from register.proto_pb.ProcedureRequestPb_pb2 import ProcedureRequestPb
			body = ProcedureRequestPb()
			body.organizationID = TEC['organizationID']
			body.observationDeptID = TEC['observationDeptID']
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='p获取检查项目树')
			print("procedure_tree返回---------")
			print(res.status_code, res.content)
		
		@task
		def exit(self):
			self.interrupt()  # 跳出当前类的任务，以便其他类任务执行
	
	@task(2)
	class SwichRefreshList(TaskSequence):
		"""切换列表"""
		
		@task
		def switch_list(self):
			api_url = HOST + "/api/CustomColumn/List"
			from techin.proto_pb.SysColumnSolutionRequestPb_pb2 import SysColumnSolutionRequestPb
			body = SysColumnSolutionRequestPb()
			body.controlName = "unFinishShootList"
			body.pageName = "unFinishShootList"
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name="sr切换等待、挂起列表")
			print("swich_list返回---------")
			print(res.status_code, res.content)
		
		"""刷新等待列表"""
		
		@task
		def refresh_wait_list(self):
			api_url = HOST + "/api/Technician/UnFinishList"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.observationDate = today_horizon2str()
			body.observationLocationIDArray = PROCINFO['observationLocationID']
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='sr刷新摄片列表')
			from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			from techin.proto_pb.ObservationListResponsePb_pb2 import ObservationListResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
			print('refresh_wait_list返回---------')
			if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
				if 'unFinishList' in res_dict['data'][0]:
					print(res.status_code, res_dict['data'][0]['unFinishList'])
				else:
					print(res.status_code, '无查询数据')
			else:
				print(res.status_code, res_dict)
		
		"""刷新挂起列表"""
		
		@task
		def refresh_hangup_list(self):
			api_url = HOST + "/api/Technician/UnFinishList"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.observationDate = today_horizon2str()
			body.observationLocationIDArray = PROCINFO['observationLocationID']
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='sr刷新挂起列表')
			from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			from techin.proto_pb.ObservationListResponsePb_pb2 import ObservationListResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
			print('refresh_hangup_list返回---------')
			if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
				if 'hangUpList' in res_dict['data'][0]:
					print(res.status_code, res_dict['data'][0]['hangUpList'])
				else:
					print(res.status_code, '无查询数据')
			else:
				print(res.status_code, res_dict)
		
		"""刷新完成列表"""
		
		@task
		def refresh_finished_list(self):
			api_url = HOST + "/api/Technician/FinishList"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			# body.observationEndDate = '2020-03-04 00:00:00|2020-03-04 23:59:59'  # 检查结束时间
			body.observationEndDate = today_horizon2str()  # 检查结束时间
			body.observationLocationIDArray = PROCINFO['observationLocationID']
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='sr刷新完成列表')
			from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			from techin.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
			print('refresh_finished_list返回---------')
			if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
				print(res.status_code, res_dict['data'])
			else:
				print(res.status_code, res_dict)
		
		@task
		def exit(self):
			self.interrupt()  # 跳出当前类的任务，以便其他类任务执行
	
	"""技师操作"""
	
	@task(10)
	class TechinOperate(TaskSequence):
		
		def __init__(self, parent):
			super().__init__(parent)
			self.orderID = self.get_orderID()
		
		# 获取列表的检查ID
		# @staticmethod
		def get_orderID(self):
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
		
		"""呼叫、选呼、复呼"""
		
		# @seq_task(1)
		@task(10)
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
				res = self.client.request(method='POST', path=api_url, data=mr_body, headers=header,
										  name='to呼叫、选呼、复呼检查')
				from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
				data = PageResponsePb()
				data.ParseFromString(res.content)
				from techin.proto_pb.ExamLoadResponsePb_pb2 import ExamLoadResponsePb
				res_json = MessageToJson(data)
				res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
				print('call_shoot返回---------')
				if 'isSuccess' in res_dict.keys() and 'data' in res_dict.keys():
					if 'orderInfo' in res_dict['data'][0]:
						print(res.status_code, '呼叫成功', res_dict['data'][0]['orderInfo'])
					else:
						print(res.status_code, '呼叫失败')
				else:
					print(res.status_code, res_dict)
			else:
				print('当前没有检查可呼叫')
		
		"""开始摄片"""
		
		# @seq_task(2)
		@task(10)
		def start_shoot(self):
			api_url = HOST + "/api/Exam/Start"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.orderID = self.orderID
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='to开始摄片')
			from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			from techin.proto_pb.FinishExamResponsePb_pb2 import FinishExamResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
			print('start_shoot返回---------')
			if 'isSuccess' in res_dict.keys():
				if res_dict['isSuccess']:
					print(res.status_code, '检查开始成功', res_dict['isSuccess'])
			else:
				print(res.status_code, '检查开始失败')
		
		"""完成摄片"""
		
		# @seq_task(3)
		@task(10)
		def end_shoot(self):
			api_url = HOST + "/api/Exam/Finish"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.orderID = self.orderID  # 从呼叫列表获取
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='to检查完成')
			# 解析结果
			from techin.proto_pb.PageResponsePb_pb2 import PageResponsePb
			data = PageResponsePb()
			data.ParseFromString(res.content)
			# 结果转为json
			from techin.proto_pb.FinishExamResponsePb_pb2 import FinishExamResponsePb
			res_json = MessageToJson(data)
			res_dict = json.loads(res_json.encode('utf-8').decode("unicode_escape"))
			print('end_shoot返回---------')
			if 'isSuccess' in res_dict.keys():
				if res_dict['isSuccess']:
					print(res.status_code, '完成检查', res_dict['isSuccess'])
			else:
				print(res.status_code, '检查完成失败')
		
		"""挂起"""
		
		@task(1)
		def hangup(self):
			api_url = HOST + "/api/Exam/Handup"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.orderID = self.orderID
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='to挂起')
			print("hangup返回---------")
			print(res.status_code, res.content)
		
		"""推迟"""
		
		@task(1)
		def postpone(self):
			api_url = HOST + "/api/Exam/Postpone"
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.orderID = self.orderID
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='to推迟')
			print("postpone---------")
			print(res.status_code, res.content)
		
		"""关闭检查窗口"""
		
		@task(10)
		def close_exam(self):
			from techin.proto_pb.OrderSearchRequestPb_pb2 import OrderSearchRequestPb
			body = OrderSearchRequestPb()
			body.observationDate = today_horizon2str()
			body.observationLocationIDArray = PROCINFO['observationLocationID']
			body = body.SerializeToString()
			api_url = HOST + "/api/Technician/UnFinishList"
			un_res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='to关闭检查窗口-刷新等待列表')
			print(un_res.status_code, un_res.content)
			api_url = HOST + "/api/Technician/FinishList"
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='to关闭检查窗口-刷新完成列表')
			print(res.status_code, res.content)
		
		@task(1)
		def exit(self):
			self.interrupt()


class User(FastHttpLocust):
	task_set = TechinTaskSet
	wait_time = between(3, 5)

def start():
	import subprocess
	# cli = "locust -f TechinScript.py -H %s --web-host %s -P %s" % (HOST, WEB, PORT)
	cli = "locust -f TechinScenariosScript.py -H %s --web-host %s -P %s" % (HOST, WEB, 8187)
	try:
		cl = subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
		print(cl.stdout.readlines())  # 打印控制台信息
	except Exception as e:
		raise str(e)


if __name__ == '__main__':
	start()