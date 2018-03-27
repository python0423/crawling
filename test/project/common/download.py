# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-26 08:48:18
# @Last Modified by:   admin
# @Last Modified time: 2018-03-26 10:23:56
# 这里完成爬虫的下载器功能
# 具体要求：通过给定的连接，下载网页上的内容，并返回网页代码，传递到下一级
 
import urllib2

 # 默认使用浏览器代理
Browser_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"

class Download:
	"""html下载器"""
	def __init__(self,url):
		self.user_agent=Browser_agent
		self.url=url
	def download_html(self,user_agent,num_retries=2):
		# 默认遇到5xx的错误，会重试下载2次
		user_agent=self.user_agent
		headers={"User_Agent":user_agent}
		req=urllib2.Request(self.url,headers=headers)
		print "downloading-->",url
		try:
			html=urllib2.urlopen(req).read()
		except urllib2.URLError as e:
			print "download error:",e.reason
			html=None
			if num_retries>0:
				if hasattr(e,"code") and 500<=e.code<=600:
					return download_html(url,user_agent,num_retries-1)
		return html


def download_html(url,user_agent=Browser_agent,num_retries=2):
 	# 默认遇到5xx的错误，会重试下载2次
 	headers={"User_Agent":user_agent}
 	req=urllib2.Request(url,headers=headers)
 	print "downloading-->",url
 	try:
 		html=urllib2.urlopen(req).read()
 	except urllib2.URLError as e:
 		print "download error:",e.reason
 		html=None
 		if num_retries>0:
 			if hasattr(e,"code") and 500<=e.code<=600:
 				return download_html(url,user_agent,num_retries-1)
 	return html
 			
if __name__ == '__main__':
	pass

