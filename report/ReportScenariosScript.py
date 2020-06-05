#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:09
# @Author  : Zhangyp
# @File    : ReportScenariosScript.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSet, between, task, TaskSequence, seq_task
from locust.contrib.fasthttp import FastHttpLocust
from configuration.config import HOST, CONTENT_TYPE, TOKEN
from common.RandomData import REPINFO, SERVICESECTID, REPORTDATA
from common.DateTimeData import today_horizon2str, within3days
from random import choice
from configuration.config import HOST, WEB

header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REPINFO}
none_header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REPINFO, 'Content-Length': '0'}


class ReportTaskSet(TaskSequence):
	# header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REPINFO}
	# none_header = {'content-type': CONTENT_TYPE, 'Authorization': TOKEN, 'userInfo': REPINFO, 'Content-Length': '0'}
	
	"""一些接口可能会多次被调用，写成公用的调用方法"""
	
	# 号码类型
	def number_type(self):
		api_url = HOST + "/api/Search/NumberType"
		from techin.proto_pb.SearchTypeRequestPb_pb2 import SearchTypeRequestPb
		body = SearchTypeRequestPb()
		body.listName = 'ReportList'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='报告列表号码类型下拉')
		print("number_type返回---------")
		print(res.status_code, res.content)
	
	# 报告列表日期条件
	def search_date_type(self):
		api_url = HOST + "/api/Search/DateType"
		from report.proto_pb.SearchTypeRequestPb_pb2 import SearchTypeRequestPb
		body = SearchTypeRequestPb()
		body.listName = 'ReportList'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='报告列表日期条件')
		print("search_date_type返回---------")
		print(res.status_code, res.content)
	
	# 检查科室下拉列表
	def dept_drop_down_list(self):
		api_url = HOST + "/api/ObservationDept/DropDownList"
		from report.proto_pb.DropDownParamRequestPb_pb2 import DropDownParamRequestPb
		body = DropDownParamRequestPb()
		body.organizationID.append('0f4a7f80-b8ed-4d25-af02-ab7a009a7966')
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, headers=header, data=body, name='检查科室下拉列表')
		print("dept_drop_down_list返回---------")
		print(res.status_code, res.content)
	
	# 自定义列
	def custom_column(self):
		api_url = HOST + "/api/CustomColumn/List"
		from techin.proto_pb.SysColumnSolutionRequestPb_pb2 import SysColumnSolutionRequestPb
		body = SysColumnSolutionRequestPb()
		body.controlName = "reportList"
		body.pageName = "reportList"
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name="自定义列")
		print("custom_column返回---------")
		print(res.status_code, res.content)
	
	# 检查状态枚举
	def common_enum(self, para):
		api_url = HOST + "/api/CommonEnum/List"
		from report.proto_pb.CommonTypeRequestPb_pb2 import CommonTypeRequestPb
		body = CommonTypeRequestPb()
		# body.paramType = 'ResultStatus'
		body.paramType = para
		body.organizationID.extend(['0f4a7f80-b8ed-4d25-af02-ab7a009a7966'])
		body.observationDeptID.extend(['f0ea6faf-dd09-43b6-bdd0-ab7a009b8633'])
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header,
								  name="%s枚举" % ('检查状态' if para == 'ResultStatus' else '会诊状态'))
		print("common_enum返回---------")
		print(res.status_code, res.content)
	
	# 机构权限
	def permission(self):
		import json
		api_url = HOST + "/api/Organization/PermissionOrgList"
		body = {"organizationID": "0f4a7f80-b8ed-4d25-af02-ab7a009a7966",
				"observationDeptID": "f0ea6faf-dd09-43b6-bdd0-ab7a009b8633"}
		payload = json.dumps(body)
		res = self.client.request(method='POST', path=api_url, headers=header, data=payload, name='加载机构权限信息')
		print("permission返回---------")
		print(res.status_code, res.content)
	
	# 就诊类别
	def patient_class(self):
		api_url = HOST + "/api/PatientClass/List"
		from report.proto_pb.PatientClassRequestPb_pb2 import PatientClassRequestPb
		body = PatientClassRequestPb()
		body.organizationID = '0f4a7f80-b8ed-4d25-af02-ab7a009a7966'
		body.observationDeptID = 'f0ea6faf-dd09-43b6-bdd0-ab7a009b8633'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name="就诊类别")
		print("patient_class返回---------")
		print(res.status_code, res.content)
	
	# 相关检查参数
	def relate_examine_parameter(self):
		api_url = HOST + "/api/RelatedExamine/Parameter"
		res = self.client.request(method='POST', path=api_url, data=None, headers=none_header, name="相关检查参数")
		print("relate_examine_parameter返回---------")
		print(res.status_code, res.content)
	
	# 检查机房
	def observation_location(self):
		api_url = HOST + "/api/ObservationLocation/DropDownList"
		from report.proto_pb.ObservationLocationRequestPb_pb2 import ObservationLocationRequestPb
		body = ObservationLocationRequestPb()
		body.organizationID = '0f4a7f80-b8ed-4d25-af02-ab7a009a7966'
		body.observationDeptID = 'f0ea6faf-dd09-43b6-bdd0-ab7a009b8633'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name="检查机房下拉")
		print("observation_location返回---------")
		print(res.status_code, res.content)
	
	# 报告刷新列表
	def refresh_list(self):
		api_url = HOST + "/api/ReportList/PageList"
		from report.proto_pb.ViOrderReportRequestPb_pb2 import ViOrderReportRequestPb
		body = ViOrderReportRequestPb()
		body.observationEndDate = today_horizon2str()
		body.currentPage = 1
		body.pageSize = 10
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='刷新报告列表')
		print("refresh_list返回------------")
		print(res.status_code, res.content)
	
	# 报告模板树加载
	def report_template(self, flag):
		api_url = HOST + "/api/ReportTemplate/Tree"
		from report.proto_pb.ReportTemplateTreeRequestPb_pb2 import ReportTemplateTreeRequestPb
		body = ReportTemplateTreeRequestPb()
		body.serviceSectID = choice(SERVICESECTID)
		# body.serviceSectID = 'CT'
		# body.examBodyPartID = ''
		body.privateFlag = flag  # 0 是共有；1 是私有
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header,
								  name='%s获取报告模板树' % ('私有' if flag == 1 else '公有'))
		print("report_template返回-----------")
		print(res.status_code, res.content)
	
	# 关键字加载
	def key_word(self):
		api_url = HOST + "/api/KeyWord/List"
		from report.proto_pb.KeyWordRequestPb_pb2 import KeyWordRequestPb
		body = KeyWordRequestPb()
		body.keyTypeArray.extend(['1002', '1005'])
		# body.keyType = '1005'
		body.organizationID = '0F4A7F80-B8ED-4D25-AF02-AB7A009A7966'
		body.observationDeptID = 'F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633'
		body.currentPage = 1
		body.pageSize = 10
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='关键词')
		print("related_examine返回------------")
		print(res.status_code, res.content)
	
	# 相关检查加载
	def related_examine(self):
		api_url = HOST + "/api/RelatedExamine/List"
		from report.proto_pb.ViOrderReportRequestPb_pb2 import ViOrderReportRequestPb
		body = ViOrderReportRequestPb()
		"""对象入参赋值"""
		body.medrecNo = '0000119'
		body.orderID = '049573B2-046C-4DF2-9ACE-AB8900B55D0F'
		body.ageArray = '23|25'
		body.ageUnit = '岁'
		body.organizationID = '0F4A7F80-B8ED-4D25-AF02-AB7A009A7966'
		body.observationDeptID = 'F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633'
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='相关检查查询')
		print("related_examine返回------------")
		print(res.status_code, res.content)
	
	# 电子申请单调阅
	def apply_bill(self):
		api_url = HOST + "/api/ApplyBill/Detail"
		from report.proto_pb.OrderRequestPb_pb2 import OrderRequestPb
		body = OrderRequestPb()
		# body.orderID = 'dee4f558-c38b-49e3-a056-ab7c00e35b38'
		body.orderID = str(choice(REPORTDATA)[1])
		# print(body.orderID)
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='调用电子申请单')
		print("apply_bill返回-----------")
		print(res.status_code, res.content)
	
	# 注意事项
	def work_flow(self):
		api_url = HOST + "/api/WorkFlow/List"
		from report.proto_pb.WorkFlowRemarkRequestPb_pb2 import WorkFlowRemarkRequestPb
		body = WorkFlowRemarkRequestPb()
		body.linkOrderID = '0000119'
		body = body.SerializeToString()  # 将对象转化成字符串
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='注意事项')
		print("work_flow返回-----------")
		print(res.status_code, res.content)
	
	# 图文报告
	def down_image(self):
		api_url = HOST + "/api/Report/DownImage"
		from report.proto_pb.ViOrderReportRequestPb_pb2 import ViOrderReportRequestPb
		body = ViOrderReportRequestPb()
		body.observationEndDate = '2020-02-25 00:00:00|2020-02-26 23:59:59'
		body.accessionNumber = '00340167'
		body.organizationID = '0F4A7F80-B8ED-4D25-AF02-AB7A009A7966'
		body.observationDeptID = 'F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633'
		body = body.SerializeToString()  # 将对象转化成字符串
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='图文报告下载')
		# from report.proto_pb.ViOrderReportResponsePb_pb2 import ViOrderReportResponsePb
		print("down_image返回-----------")
		print(res.status_code, res.content)
	
	# 特殊符号
	def special_char_info(self):
		api_url = HOST + "/api/SpecialCharInfo/List"
		from report.proto_pb.ViSpecialCharInfoRequestPb_pb2 import ViSpecialCharInfoRequestPb
		body = ViSpecialCharInfoRequestPb()
		body.organizationID = '0F4A7F80-B8ED-4D25-AF02-AB7A009A7966'
		body.observationDeptID = 'F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633'
		body = body.SerializeToString()  # 将对象转化成字符串
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='特殊符号加载')
		print("special_char_info返回-----------")
		print(res.status_code, res.content)
	
	# 影像调阅
	def image_view(self):
		api_url = HOST + "/api/Address/ImageView"
		from report.proto_pb.ImageViewRequestPb_pb2 import ImageViewRequestPb
		body = ImageViewRequestPb()
		body.orderID.append(str(choice(REPORTDATA)[1]))
		body = body.SerializeToString()  # 将对象转化成字符串
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='影像调阅地址')
		print("image_view返回-----------")
		print(res.status_code, res.content)
	
	# 报告书写界面加载
	def report_load(self):
		api_url = HOST + "/api/Report/Loading"
		from report.proto_pb.ReportRequestPb_pb2 import ReportRequestPb
		body = ReportRequestPb()
		"""对象入参赋值"""
		# body.orderID = '7E348EE3-F4F6-41C0-8332-AB80011CED89'
		# print(rORDERID)
		body.orderID = str(choice(REPORTDATA)[1])
		from report.proto_pb.OrderReportRequestPb_pb2 import OrderReportRequestPb
		orr_body = OrderReportRequestPb()
		orr_body.report.CopyFrom(body)
		orr_body = orr_body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=orr_body, headers=header, name='加载报告接口')
		print("report_load返回------------")
		print(res.status_code, res.content)
	
	"""进入报告工作站的加载项"""
	
	@task(1)
	def station_load(self):
		self.search_date_type()
		self.number_type()
		self.permission()
		self.key_word()
		self.dept_drop_down_list()
		self.observation_location()
		self.common_enum('ResultStatus')
		self.common_enum('ConsultStatus')
		self.patient_class()
		self.relate_examine_parameter()
		self.refresh_list()
	
	"""自动触发超时报告查询"""
	
	@task(0)
	def timeout_list(self):
		api_url = HOST + "/api/TimeoutReport/PageList"
		from report.proto_pb.ReportConditionRequestPb_pb2 import ReportConditionRequestPb
		body = ReportConditionRequestPb()
		"""对象入参赋值"""
		body.initiative = 0
		body.pageSize = 20
		body.pageIndex = 1
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='自动超时报告')
		print("timeout_list返回------------")
		print(res.status_code, res.content)
	
	"""手动超时报告查询"""
	
	@task(0)
	def manual_timeout_list(self):
		api_url = HOST + "/api/TimeoutReport/PageList"
		from report.proto_pb.ReportConditionRequestPb_pb2 import ReportConditionRequestPb
		body = ReportConditionRequestPb()
		"""对象入参赋值"""
		body.initiative = 1
		body.pageSize = 10
		body.pageIndex = 1
		body.gapTime = 30
		body.regDate = within3days()
		body = body.SerializeToString()
		res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='手动超时报告')
		print("manual_timeout_list返回------------")
		print(res.status_code, res.content)
	
	"""进入报告书写界面"""
	
	@task(2)
	def report_edit_load(self):
		self.report_load()
		self.refresh_list()
		self.report_template(0)
		self.report_template(1)
		self.related_examine()
		self.down_image()
		self.key_word()
		self.work_flow()
		self.image_view()
		self.apply_bill()
	
	"""报告医生操作"""
	
	#  问题 'ReportOperate' object has no attribute 'header'
	@task(5)
	class ReportOperate(TaskSequence):
		# # 执行任务前随机选取orderID
		# 		# order_id = ''
		# 		#
		# 		# def on_start(self):
		# 		# 	self.order_id = str(choice(REPORTDATA)[1])
		# 		# 	print('执行start')
		
		def __init__(self, parent):
			super().__init__(parent)
		
		"""查看申请单"""
		
		@seq_task(1)
		@task(1)
		def apply_bill(self):
			api_url = HOST + "/api/ApplyBill/Detail"
			from report.proto_pb.OrderRequestPb_pb2 import OrderRequestPb
			body = OrderRequestPb()
			body.orderID = str(choice(REPORTDATA)[1])
			# print(body.orderID)
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='ro调用电子申请单')
			print("apply_bill返回-----------")
			print(res.status_code, res.content)
		
		"""选中报告模板"""
		
		@seq_task(2)
		@task(1)
		def report_template(self):
			api_url = HOST + "/api/ReportTemplate/Tree"
			from report.proto_pb.ReportTemplateTreeRequestPb_pb2 import ReportTemplateTreeRequestPb
			body = ReportTemplateTreeRequestPb()
			body.serviceSectID = choice(SERVICESECTID)
			# body.examBodyPartID = ''
			body.privateFlag = 0
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='ro获取报告模板树')
			print("report_template返回-----------")
			print(res.status_code, res.content)
		
		"""危急值"""
		
		@seq_task(3)
		@task(1)
		def critical_report(self):
			api_url = HOST + "/api/CriticalReport/Detail"
			from report.proto_pb.CriticalReportRequestPb_pb2 import CriticalReportRequestPb
			body = CriticalReportRequestPb()
			body.criticalID = 'e7f0e599-50c7-450a-afe3-ab8200ebf529'
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='ro危急值报告')
			print("critical_report返回-----------")
			print(res.status_code, res.content)
		
		"""签名"""
		
		@seq_task(4)
		@task(1)
		def signature(self):
			api_url = HOST + "/api/Report/Signature"
			from report.proto_pb.ReportRequestPb_pb2 import ReportRequestPb
			rr_body = ReportRequestPb()
			# rr_body.orderID = 'A1E3EB87-ACB5-4B21-BC1E-7EE8D04323A1'
			report_id = choice(REPORTDATA)
			rr_body.orderID = str(report_id[1])
			# print(rr_body.orderID)
			rr_body.reportID = str(report_id[0])
			# rr_body.reportID = 'B9200ADE-2AB7-4766-B85E-54B970B106D5'
			rr_body.abnormalFlag = '0'
			rr_body.imagingFinding = '影像所见压力测试写入'
			rr_body.imagingDiagnosis = '影像诊断压力测试写入'
			rr_body.isCheckedWriteAndAudit = 1
			from report.proto_pb.OrderReportRequestPb_pb2 import OrderReportRequestPb
			orr_body = OrderReportRequestPb()
			orr_body.report.CopyFrom(rr_body)
			orr_body = orr_body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=orr_body, headers=header, name='ro报告签名')
			print("signature返回-----------")
			print(res.status_code, res.content)
		
		@seq_task(5)
		@task
		def refresh(self):
			api_url = HOST + "/api/ReportList/PageList"
			from report.proto_pb.ViOrderReportRequestPb_pb2 import ViOrderReportRequestPb
			body = ViOrderReportRequestPb()
			body.observationEndDate = today_horizon2str()
			body.currentPage = 1
			body.pageSize = 10
			body = body.SerializeToString()
			res = self.client.request(method='POST', path=api_url, data=body, headers=header, name='ro刷新报告列表')
			print("refresh_list返回------------")
			print(res.status_code, res.content)
		
		# """报告打印"""
		#
		# def report_print(self):
		# 	api_url = HOST + "/api/Report/Print"
		# 	pass
		#
		# """暂存"""
		#
		# def temporary_storage(self):
		# 	api_url = HOST + "/api/Report/TemporaryStorage"
		# 	pass
		#
		@seq_task(6)
		@task
		def exit(self):
			self.interrupt()
			print('退出报告')


class ReportUser(FastHttpLocust):
	task_set = ReportTaskSet
	wait_time = between(3, 5)


def start():
	import subprocess
	# cli = "locust -f %s -H %s --web-host %s -P %s" % (SCRIPT,HOST, WEB, PORT)
	cli = "locust -f ReportScenariosScript.py -H %s --web-host %s -P %s" % (HOST, WEB, 8186)
	try:
		cl = subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
		print(cl.stdout.readlines())  # 打印控制台信息
	except Exception as e:
		raise str(e)


if __name__ == '__main__':
	start()
