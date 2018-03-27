# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-20 12:13:34
# @Last Modified by:   admin
# @Last Modified time: 2018-03-20 12:33:32

# 此文件用来实现爬取页面
import urllib2
import re
import urlparse

def download1(url):
	# 返回爬取的网页数据,最原始版本
	return  urllib2.urlopen(url).read()

def download2(url):
	# 实现对异常的捕捉
	print "开始下载页面"
	try:
		html=urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print "下载错误",e.reason
	return html

def download3(url,num_retry=2):
	# 如果碰到5xx的错误，程序会进行重试下载，次数为2
	print "downloading: ",url
	try:
		html=urllib2.urlopen(url).read()
	except URLError as e:
		print "下载出错",e.reason
		html=None
		if num_retry>0:
			if hasattr(e,"code") and 500<=e.code<600:
				return download3(url,num_retry-1)
	return html

def download4(url,num_retry=2,user_agent="wswp"):
	# 增加用户代理，在此基础上进行爬取
	print "downloading: ",url
	headers={"User-agent":user_agent}
	request=urllib2.Request(url,headers=headers)
	try:
		html=urllib2.urlopen(request).read()																																																																																															
	except urllib2.URLError as e:																																												
		print "error: ",e.reason
		html=None
		if num_retry>0:
			if hasattr(e,"code") and 500<=e.code<600:
				return download4(url,num_retry-1,user_agent)
	return html

download=download4

if __name__ == '__main__':
	download("http://example.webscraping.com")