# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-17 12:11:07
# @Last Modified by:   admin
# @Last Modified time: 2018-03-17 12:57:21
# 本程序用来联系requests模块，模仿简单的用户名和密码登录

import requests 

# 登录页面函数，返回登录状态码
def login_in(url):
	params={"phone":"13815508555","pwd":"wangxiao"}
	r=requests.post(url,data=params)

	print r.status_code
	print r.history[0].url
	# print r.text


if __name__ == '__main__':
	login_in("http://www.speakhi.com")
