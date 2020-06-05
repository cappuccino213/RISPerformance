#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 10:56
# @Author  : Zhangyp
# @File    : table2json.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import pymssql
import json
import os
def table2json():
	try:
		# 数据库连接信息
		conn_info = {
			'host':"192.168.1.16",
			'user':"sa",
			'pwd':"p@ssw0rd",
			'db':"RISFactory",
			'charset':"utf8"
		}
	
		# 连接数据库
		conn = pymssql.connect(host=conn_info['host'],
							   user=conn_info['user'],
							   password=conn_info['pwd'],
							   database=conn_info['db'],
							   charset=conn_info['charset'])
		cur = conn.cursor()
		
		# 查询数据库语句
		sql = "SELECT  ProcedureID,ProcedureName,ExamBodyPartID,ExamBodyPart,ServiceSectID FROM D_Exam"
		cur.execute(sql)
		data = cur.fetchall()
		print(u'fetchall()返回的数据:',data)
		cur.close() #关闭游标
		conn.close()# 关闭连接
		json_list=[]
		# 读取元组数据
		for i in data:
			result = {}
			result['ProcedureID'] = i[0]
			result['ProcedureName'] = i[1]
			result['ExamBodyPartID'] = i[2]
			result['ExambodyPart']= i[3]
			result['ServiceSectID']= i[4]
			json_list.append(result)
			# print(u'转换为列表字典的原始数据:',json_list)
	except:
		print('MySQL connect fail...' )
	else:
		jsondatar = json.dumps(json_list, ensure_ascii=False)
		return jsondatar
	
if __name__=='__main__':
	json_data = table2json()
	print(u'转换为json格式的数据：',json_data )
	cur_path = os.path.abspath(os.path.dirname(__file__))
	with open('%s/exam.json'%cur_path,'w+') as f:
		f.write(json_data)