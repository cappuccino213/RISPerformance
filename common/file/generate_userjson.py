#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 14:58
# @Author  : Zhangyp
# @File    : generate_userjson.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from faker import Faker
fake = Faker('zh_CN')
import uuid
import json
import os

#生成user的id:name，兼职对数据，保存到当前目录的json文件下
def generate_user(num):
	userinfo = []
	for i in range(num):
		user = {}
		user['id']=str(uuid.uuid4())
		user['name']=fake.name()
		userinfo.append(user)
	# user_json =
	with open('%s/user.json'%os.getcwd(),'w+') as f:
		json.dump(userinfo,f,ensure_ascii=False)
		# f.write(userinfo)
		
		
if __name__=='__main__':
	generate_user(100)