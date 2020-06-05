#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 10:04
# @Author  : Zhangyp
# @File    : DataFromDB.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import pymssql

"""
pymssql工作原理
①、使用connect创建连接对象；
②、connect.cursor创建游标对象，SQL语句的执行在游标上执行；
③、cursor.execute()方法执行SQL语句，cursor.fetch()方法获取查询结果；
④、调用close方法关闭游标cursor和数据库连接；
"""


class SQLServer:
	def __init__(self, host, user, password, database, character):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		self.character = character
	
	def __connect(self):
		if not self.database:
			raise (NameError, "找不到数据库：%s" % self.database)
		self.conn = pymssql.connect(server=self.host, user=self.user, password=self.password, database=self.database,
									charset=self.character)
		cur = self.conn.cursor()
		if not cur:
			raise (NameError, "连接数据失败")
		else:
			return cur
	
	def query(self, sql):
		"""
		执行查询语句
		返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
		"""
		cur = self.__connect()
		cur.execute(sql)
		result = cur.fetchall()
		self.conn.close()
		return result


# 查询数据
def get_data(sql):
	# msg = SQLServer(host="192.168.1.16", user="sa", password="p@ssw0rd", database="eWordRIS", character="utf8")
	msg = SQLServer(host="192.168.1.26", user="sa", password="p@ssw0rd", database="eWordRIS_300W", character="utf8")
	result = msg.query(sql)
	return result


"""根据实际数据需要从数据库查询"""
# 不同角色用户
reg_user = get_data(
	"select UserID,AccountName,UserPassWord,OrganizationID,ObservationDeptID  from Vi_UserGroup WHERE UserGroupCode = '1002' And OrganizationID='0f4a7f80-b8ed-4d25-af02-ab7a009a7966'")
# "select UserID,AccountName,UserPassWord,OrganizationID,ObservationDeptID  from Vi_UserGroup WHERE UserGroupCode = '1002'")
tec_user = get_data(
	"select UserID,AccountName,UserPassWord,OrganizationID,ObservationDeptID  from Vi_UserGroup WHERE UserGroupCode = '1003' And OrganizationID='0f4a7f80-b8ed-4d25-af02-ab7a009a7966'")
rep_user = get_data(
	"select UserID,AccountName,UserPassWord,OrganizationID,ObservationDeptID  from Vi_UserGroup WHERE UserGroupCode = '1001' And OrganizationID='0f4a7f80-b8ed-4d25-af02-ab7a009a7966'")


# 登记需要的检查信息
def order_data(oid, odid, ssid):
	sql = """SELECT
	l.ObservationLocationID,l.ObservationLocation,ExamBodyPartName,ExamBodyPartID,ProcedureName,ProcedureID,ProcedureWorkload,DiagnosticGroupID
FROM
	Vi_ExamProcedure e INNER JOIN B_ObservationLocation l ON e.OrganizationID=l.OrganizationID AND e.ObservationDeptID=l.ObservationDeptID
WHERE
	l.OrganizationID = '%s'
	AND
	l.ObservationDeptID='%s'
	AND
	l.ServiceSectID='%s'""" % (oid, odid, ssid)
	return get_data(sql)


# 取消检查需要的信息
def cancel_data(oid, odid):
	sql = """SELECT TOP
	1000 OrderID
FROM
	Vi_Order
WHERE
	OrganizationID = '%s'
	AND ObservationDeptID = '%s'
	AND ResultStatus =1020""" % (oid, odid)
	return get_data(sql)


# 开始检查需要的信息
def exam_data():
	sql = """select DISTINCT ObservationLocationID FROM
	M_Order
WHERE
	ResultStatus = 1020
	AND RegDate >= CONVERT ( VARCHAR, GETDATE( ), 23 )
	AND OrganizationID='0f4a7f80-b8ed-4d25-af02-ab7a009a7966'"""
	return get_data(sql)


# 报告签名需要的信息
def report_data(oid, odid):
	sql = """SELECT TOP
	1000 reportid,
	OrderID
FROM
	Vi_OrderReport
WHERE
	ResultStatus BETWEEN 2090
	AND 4030
	AND OrganizationID = '%s'
	AND ObservationDeptID = '%s'""" % (oid, odid)
	return get_data(sql)


if __name__ == '__main__':
	from random import choice
	r1 = exam_data()
	print(str(choice(r1)[0]))
