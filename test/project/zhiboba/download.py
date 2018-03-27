# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-13 11:24:29
# @Last Modified by:   admin
# @Last Modified time: 2018-03-26 16:20:05

import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import csv
BrowserAgent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"

class Download:
	"""下载类"""
	def __init__(self, user_agent=BrowserAgent):
		self.user_agent = user_agent

	def download(self,url,user_agent=None,num_retry=2):
		# 下载网页
		headers={"User-Agent":self.user_agent}
		req=urllib2.Request(url,headers=headers)
		try:
			html=urllib2.urlopen(req).read()
		except urllib2.URLError as e:
			print "download error: ",e.reason
			html=None
			if hasattr(e,"code") and 500<=e.code<=600:
				download(url,user-agent,num_retry-1)
		return html

if __name__ == '__main__':
	# dw=Download()
	pass















	