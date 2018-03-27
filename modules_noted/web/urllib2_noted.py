# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-23 11:27:42
# @Last Modified by:   admin
# @Last Modified time: 2018-03-23 15:48:51
# 这里研究urllib2模块
import urllib2
import urllib
def get_fuc(url):
	# get请求
	html=urllib2.urlopen(url)  # 这个html对象是可迭代的
	print html.geturl()
	# 打印头信息
	print html.info()
	# 打印页面文本
	print html.read(20)
	# 传递参数，使用urllib.encode先编码，然后构造url
	data={"name":"namestring","age":"16"}
	en_data=urllib.urlencode(data)
	url="http://www.baidu.com/?"+en_data
	html_data=urllib2.urlopen(url)

def post_fuc(url):
	# post请求
	data={"name":"123","pwd":"123"}
	en_data=urllib.urlencode(data)
	html=urllib2.urlopen(url,en_data).read()

def header_fuc(url):
	# 添加头信息
	request=urllib2.Request(url)
	request.add_header("user-agent":"firfox")
	html=urllib2.urlopen(request).read()



if __name__ == '__main__':
	get_fuc("http://example.webscraping.com/")