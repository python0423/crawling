# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-23 07:38:52
# @Last Modified by:   admin
# @Last Modified time: 2018-03-23 13:35:20
# 这个模块练习request

import requests
import pickle
def method_get(url):
	# 使用get方法请求页面,获取相应属性
	r=requests.get(url)
	print "请求页面：",r.url
	# print "返回头信息：",r.headers
	print "返回服务器信息：",r.headers.get("server")
	print "编码：",r.encoding
	print "类型：",r.headers.get("content-type")
	print "状态码：",r.status_code
	print r.headers.get("user-agent") # 返回none 
	print r.headers
	# 以字节流的方式读取
	r=requests.get(url,stream=True)
	r.encoding="utf-8"
	byte=r.raw.read(20)
	print byte

def cookie_fuc(url):
	# 这个函数设置cookie
	# 首先收集cookie的值
	r=requests.get(url)
	for cookie in r.cookies.keys():
		print r.url
		print cookie+"-->"+r.cookies.get(cookie)
	# 自定义cookie，然后发送出去
	cookies={"BDORZ":"27315"}
	r_cookie=requests.get(url,cookies=cookies)
	print r_cookie.status_code
from urllib import urlencode
from bs4 import BeautifulSoup
def login_session(url):
	# 使用session进行登录，先从服务器获取一个session，然后访问登录页面时会自动把cookie带上
	s=requests.Session()
	# r=s.get(url,allow_redirects=True)
	data={"account":"trevor.fzp","pwd":"111111"}
	en_data=urlencode(data)
	s.post(url,data=en_data,allow_redirects=True)
	html=s.get("http://webiadmin.speakhi.com/bgmanagementadmin").content 
	soup=BeautifulSoup(html,"lxml")
	div=soup.find("div",_class="con")
	li=div.find("li",_class="u_name")
	print li.text
	


def param_get(url):
	# 使用get方法，并带有搜索参数
	payload={"ie":"utf-8","tn":"baidu","wd":u"zhiboba"}
	r=requests.get(url,params=payload)
	if r.status_code==200:
		print r.headers
	else:
		# 这个函数会在状态码为4xx或者5xx时抛出异常，2xx时返回none
		r.raise_for_status()


if __name__ == '__main__':
	url=["http://www.baidu.com","http://www.xynun.edu.cn","http://www.163.com","http://example.webscraping.com/","http://www.speakhi.com"]
	# for link in url:
	# 	method_get(link)
	# 	cookie_fuc(link)
	# param_get("http://www.baidu.com/s")
	# cookie_fuc("http://www.baidu.com")
	login_session("http://webiadmin.speakhi.com/bgmanagementadmin")

	