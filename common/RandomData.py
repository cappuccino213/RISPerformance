#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 14:10
# @Author  : Zhangyp
# @File    : RandomData.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from random import choice

"""随机取用户信息的body"""
from common.DataFromDB import reg_user, tec_user, rep_user


def user_dict(users):
	user_data = choice(users)
	return {"userID": str(user_data[0]), "accountName": user_data[1], "userPassWord": user_data[2],
			"organizationID": str(user_data[3]), "observationDeptID": str(user_data[4])}


REG = user_dict(reg_user)
TEC1 = user_dict(tec_user)
REP = user_dict(rep_user)

TEC = {"userID": "3B1FB493-7999-484A-8C27-AB7A00A911DC", "accountName": "dyjs",
	   "userPassWord": "E10ADC3949BA59ABBE56E057F20F883E",
	   "organizationID": "0F4A7F80-B8ED-4D25-AF02-AB7A009A7966",
	   "observationDeptID": "F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633"}

REP1 = {"userID": "D1EBDDFB-A4E8-4942-B916-AB7A00AA0639", "accountName": "dysh",
		"userPassWord": "E10ADC3949BA59ABBE56E057F20F883E",
		"organizationID": "0F4A7F80-B8ED-4D25-AF02-AB7A009A7966",
		"observationDeptID": "F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633"}

"""用于模块功能的header"""
# 无用户信息
USERINFO = {"clientAuthCode": "", "useScenario": "1",
			"cookieRequest": {"printTaskSolution": "00000000-0000-0000-0000-000000000001",
							  "printerSolution": "00000000-0000-0000-0000-000000000002", "equipSolution": ""}}

# 各功能模块的userInfo
import json

reg_dict = {"userID": REG['userID'], "organizationID": REG['organizationID'],
			"observationDeptID": REG['observationDeptID']}
# reg_dict.update(USERINFO)
reg_dict = {**reg_dict, **USERINFO}  # 合并字典

tec_dict = {"userID": TEC['userID'], "organizationID": TEC['organizationID'],
			"observationDeptID": TEC['observationDeptID']}
tec_dict = {**tec_dict, **USERINFO}

rep_dict = {"userID": REP['userID'], "organizationID": REP['organizationID'],
			"observationDeptID": REP['observationDeptID']}
rep_dict = {**rep_dict, **USERINFO}

REGINFO = json.dumps(reg_dict)
TECINFO = json.dumps(tec_dict)
REPINFO = json.dumps(rep_dict)

"""可用检查类型"""
# ServiceSectID = choice(['CR', 'MR', 'TJ', 'CT', 'DX', 'MG', 'XA'])
SERVICESECTID = ['CR', 'MR', 'TJ', 'CT', 'DX', 'MG', 'XA']

"""根据检查类型，获取可用机房，检查项目"""
from common.DataFromDB import order_data

proc_info = choice(order_data(REG['organizationID'], REG['observationDeptID'], choice(SERVICESECTID)))
PROCINFO = {"observationLocationID": str(proc_info[0]), "observationLocation": proc_info[1],
			"examBodyPart": proc_info[2],
			"examBodyPartID": str(proc_info[3]), "procedureName": proc_info[4], "procedureID": str(proc_info[5]),
			"procedureWorkload": str(proc_info[6]), "diagnosticGroupID": str(proc_info[7]),
			"allProcedureName": proc_info[4]}

"""取消检查的ID"""
from common.DataFromDB import cancel_data

ORDERID = str(choice(cancel_data(REG['organizationID'], REG['observationDeptID']))[0])

"""当天可用于技师检查的数据"""
from common.DataFromDB import exam_data

OBSERVATIONLOCATIONID = exam_data()

"""报告签名id"""
from common.DataFromDB import report_data

# REPORTID = str(choice(report_data("0F4A7F80-B8ED-4D25-AF02-AB7A009A7966", "F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633"))[0])
REPORTDATA = report_data("0F4A7F80-B8ED-4D25-AF02-AB7A009A7966", "F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633")
# rORDERID = str(choice(report_data("0F4A7F80-B8ED-4D25-AF02-AB7A009A7966", "F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633"))[1])
# rORDERID = report_data("0F4A7F80-B8ED-4D25-AF02-AB7A009A7966", "F0EA6FAF-DD09-43B6-BDD0-AB7A009B8633")


"""机房的ID"""

""""""
if __name__ == '__main__':
	print(type(REGINFO))
	print(REGINFO)
