# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-05 11:17:40
# @Last Modified by:   admin
# @Last Modified time: 2018-03-06 11:20:26
# 第一章 download函数
import urllib2
def download_first(url):
	# 使用urllib2模块下载网页
	return urllib2.urlopen(url).read()

def download_error(url):
	# 最初版本的下载函数无法捕捉错误，这里实现错误的异常处理
	print "downloading: ",url
	try:
		html=urllib2.urlopen(url).read()

	except urllib2.URLError as e:	
		print "download error",e.reason
		html=None
	return html

def download_retry(url,num_retries=2):
	# 支持异常处理的函数，如果碰到服务器错误，即5xx的错误，就会停止运行，这里给出解决方案，如果碰到
	# 5xx的错误，则进行重试，重试次数为2
	print "downloading ,",url
	try:
		html=urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print "download error",e.reason
		html=None
		if num_retries>0:
			if hasattr(e,"code") and 500<=e.code<600:
				# 重试下载，通过迭代的方式
				return download_retry(url,num_retries-1)
	return html
def download_useragent(url,user_agent="wswp",num_retries=2):
	# 这个版本支持设定用户代理，这个值可以是任意的，也可以根据网站的robot.txt来设置
	print "downloading",url
	headers={"User-agent":user_agent}
	# 构造request对象
	request=urllib2.Request(url,headers=headers)
	try:
		html=urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print "download error",e.reason
		html=None
		if num_retries>0:
			if hasattr(e,"code") and 500<=e.code<600:
				return download_useragent(url,user_agent,num_retries-1)
	return html
# download_agentname 这个函数实现了三个功能：捕获异常，重试下载，设置用户代理

def download_proxy(url,user_agent="wswp",proxy=None,num_retries=2):
	print "downloading: ",url 
	headers={"User-agent":user_agent}
	request=urllib2.Request(url,headers=headers)
	# 使用urllib2支持代理
	opener=urllib2.build_opener()
	if proxy:
		proxy_params={urlparse.urlparse(url).scheme:proxy}
		opener.add_handler(urllib2.ProxyHandler(proxy_params))
	try:
		html=opener.open(request).read()

	except urllib2.URLError as e:
		print "download error:",e.reason
		html=None
		if num_retries>0:
			if hasattr(e,"code") and 500<=e.code<600:
				html=download_proxy(url,user_agent,proxy,num_retries-1)
	return html


download=download_proxy

if __name__ == '__main__':
	print download("http://example.webscraping.com")
