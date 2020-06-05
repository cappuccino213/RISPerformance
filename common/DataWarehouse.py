#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 14:45
# @Author  : Zhangyp
# @File    : generate_data.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""
生成数据
"""
from random import choice  # list随机取元素
import random
from faker import Faker
import uuid
import datetime
import json
import os
from pypinyin import pinyin, Style

fake = Faker('zh_CN')  # 指定中国区域（en_US 英语（美国）、en_GB 英语（英国）等）其他提供商见https://faker.readthedocs.io/en/master/


# from datetime import datetime


class PersonData:  # 人的基本信息相关
	
	def __init__(self):
		self.name = self.name()
		self.name_spell = self.name_spell()
		self.sex = self.sex()
		self.birth_date = self.birthday()
		self.age = self.age()
		self.address = self.address()
		self.company = self.company()
		self.job = self.job()
	
	# self.phone_number = self.phone()
	
	@staticmethod
	def name():  # 生成姓名
		return fake.name()
	
	def name_spell(self):
		pinyin_list = pinyin(self.name, style=Style.NORMAL)  # 通过pinyin函数将中文转换成list,结构[['zhong'], ['xin']]
		pinyin_str = ''
		for sub_list in pinyin_list:  # 遍历拼凑起来
			for spell in sub_list:
				pinyin_str = pinyin_str + spell.capitalize()  # 首字母大写处理
		return pinyin_str
	
	@staticmethod
	def name_by_sex(sex='F'):  # 根据性别生成姓名
		if sex == 'F':
			return fake.name_female()
		if sex == 'M':
			return fake.name_male()  # gen
	
	@staticmethod
	def birthday():  # 最大90岁的年龄
		return fake.date_of_birth(tzinfo=None, minimum_age=1, maximum_age=90)
	
	def age(self):
		return datetime.date.today().year - self.birth_date.year
	
	@staticmethod
	def sex():  # 随机生成性别
		return choice(['F', 'M'])
	
	@staticmethod
	def address():
		return fake.address()
	
	@staticmethod
	def company():
		return fake.company()
	
	@staticmethod
	def job():
		return fake.job()
	
	@staticmethod
	def phone(_type=1):  # 1表示移动电话，2表示固话
		if _type == 1:
			return fake.phone_number()
		if _type == 2:
			str1 = fake.msisdn()[0:4]
			str2 = fake.msisdn()[4:]
			return str1 + '-' + str2
	
	def generate_id(self):  # 身份证号
		pass


class DataType:
	def __init__(self):
		self.bool = fake.pybool()  # 布尔型
		self.int = fake.pyint(min=0, max=9999, step=1)  # 整型
		self.float = fake.pyfloat(left_digits=None, right_digits=None, positive=False, min_value=None,
								  max_value=None)  # 单精度浮点型
		"""
		还有其他类型，如pydecimal（定点数）、pylist（列表）、pystr（字符串）、pystruct（数据集）等
		"""


class RISData:  # 放射检查相关数据
	
	def __init__(self):
		self.OrderExtID = uuid.uuid4()
		self.OrderPKID = uuid.uuid4()
		self.OrderID = uuid.uuid1()
		self.organization_name = '**第一人民医院'
		self.organization_id = uuid.UUID('7D0F1193-1931-4F92-B80E-14F35B4D5B22')  # 将str转化成uid
		self.ObservationDeptID = uuid.UUID('994E9493-EC2D-4B1B-BAE7-D1E9D7B5ACB2')
		self.ObservationDeptName = '放射科'
		self.patient_class = self.patient_class()
		self.patient_type = self.patient_type()
		self.exams = self.examitem_dict()
		self.users = self.user_dict()
		self.times = self.random_times()
		self.ReportID = uuid.uuid4()
		self.ImagingFinding = fake.text()
		self.ImagingDiagnosis = fake.text()
		self.DiagnosticOrganization = uuid.UUID('7D0F1193-1931-4F92-B80E-14F35B4D5B22')
		self.DiagnosticOrganizationName = '**第一人民医院'
		self.Resultstatus = 3080
	
	@staticmethod
	def patient_class():
		return choice([1000, 2000, 3000, 4000])  # 1000门诊、2000住院、3000体检、4000急诊
	
	@staticmethod
	def patient_type():
		return choice(['普通', 'ICU'])
	
	def outpatient_no(self, num, digit=8):  # num为一个自增的数
		if self.patient_class == 1000:
			return 'MZ' + str(num).zfill(digit)
	
	def inpatient_no(self, num, digit=8):
		if self.patient_class == 2000:
			return 'ZY' + str(num).zfill(digit)
	
	def physical_no(self, num, digit=8):
		if self.patient_class == 3000:
			return 'TJ' + str(num).zfill(digit)
	
	@staticmethod
	def accession_number(num, digit=8):  # 根据指定位数自动补零
		n = str(num)
		return n.zfill(digit)
	
	def medrecno(self):
		pass
	
	@staticmethod
	def patientid(num):  # 患者编号根据时间+数字
		# import datetime
		time_no = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
		return time_no + str(num)
	
	@staticmethod
	def service_sect_id():
		return choice(['CR', 'DR', 'CT', 'MR', 'MG', 'RF', 'TJ', 'XA'])
	
	@staticmethod
	def examitem_dict():
		with open(r'%s/file/exam.json' % os.getcwd()) as f:  # 从file目录读取检查项目的模板
			items = json.load(f)  # 读取json文件
		item = choice(items)  # 随机选择一组检查项目数据
		# print(item)
		return item
	
	@staticmethod
	def random_times():  # 随机取近十年的时间
		# dt = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
		dt = fake.date_time_between(start_date="-5y", end_date="now", tzinfo=None) # 近5年到现在
		# time = dt.strftime("%Y-%m-%d %H:%M:%S")# 格式化时间
		times = {'RegDate': dt, 'ObservationDate': dt + datetime.timedelta(hours=0.5)}
		times['ObservationEndDate'] = times['ObservationDate'] + datetime.timedelta(minutes=10)  # 检查结束时间 ，10分钟一个检查
		times['QAachieveDate'] = times['ObservationEndDate'] + datetime.timedelta(minutes=5)  # 影像归档时间，5分钟
		times['PreliminaryDate'] = times['QAachieveDate'] + datetime.timedelta(minutes=20)  # 20分钟后开始写报告
		times['PreliminaryEndDate'] = times['PreliminaryDate'] + datetime.timedelta(minutes=2)  # 2分钟一份报告
		times['AuditDate'] = times['PreliminaryEndDate'] + datetime.timedelta(minutes=5)  # 5分钟后审核
		times['AuditEndDate'] = times['AuditDate'] + datetime.timedelta(minutes=2)  # 2分钟审核完成
		return times
	
	@staticmethod
	def user_dict():  # 用户id和用户（医生）
		with open(r'%s/file/user.json' % os.getcwd()) as f:
			users = json.load(f)
		return random.sample(users, 4)  # 随机选取4组数据


class FileData():  # 文件数据
	pass


class DcmImageData():  # DICOM影像数据
	pass


if __name__ == '__main__':
	# gd = PersonData()
	# print(gd.name,gd.name_spell,gd.birth_date.strftime('%Y-%m-%d'),gd.age)
	rd = RISData()
	for i in range(10):
		print(rd.random_times())
# dt = DataType()
# 	rs = RISData()
# 	p=rs.examitem_dict()
# 	print(p)
# l=rs.examitem_dict()['ExamBodyPart']
# print(l)
# print(rs.user_dict()[0])
# print(rs.ExamBodyPartID,rs.ExamBodyPart,rs.ProcedureID,rs.ProcedureName)
# print(gd.phone(2))
# print(type(dt.bool))
# num = 86000000
# for i in range(10):
# 	rs = RISData()
# 	ino=None
# 	out=None
# 	if rs.inpatient_no():
# 		ino= rs.inpatient_no()+str(num+i)
# 	if 	rs.outpatient_no():
# 		out= rs.outpatient_no()+str(num+i)
# 	print(rs.patient_class,ino,out)
# print(rs.patient_class1)

# for i in range(10):
# 	rs = RISData()
# 	print(rs.patientid(i))
