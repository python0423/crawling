# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-02-20 12:44:36
# @Last Modified by:   admin
# @Last Modified time: 2018-03-13 12:43:42
import itertools
def tmp1():
	for x in itertools.count(1):
		print x
		if x>5:
			break
def tmp2():
	import re
	url=["<a href= 'www.baidu.com'>"]
	regex="<a.href=['\"](.*?)['\"]"
	print re.findall(regex, url[0])

def tmp3():
	import urlparse
	print urlparse.urlparse("http://www.baidu.com").netloc
	import datetime
	print datetime.datetime.now()


# from chapter01 import download_agentname
from bs4 import BeautifulSoup
def scrap_school_link(url):
	html=download_agentname(url)
	soup=BeautifulSoup(html,"html5lib")
	div=soup.find("div",attrs={"id":"plink"})
	link=div.find_all("a")
	for linkname in link:
		print linkname

def scrap_sportnews_link(url):
	html=download_agentname(url)
	soup=BeautifulSoup(html,"html5lib")
	div=soup.find_all("div",attrs={"class":"left","id":"recommend"})
	for insert_div in div:
		link=insert_div.find_all("div",attrs={"class":"r_news right"})
		for linkname in link:
			a_href=linkname.find_all("a")
			print 
			for a_link in a_href:
				print a_link.text


#使用lxml进行爬取
import lxml.html
def lxml_sportnews_link(url):
	html=download_agentname(url)
	#构造完整的网页
	tree=lxml.html.fromstring(html)
	for link in tree.cssselect("div#recommend.left>div.r_news"):
		print link.text_content()


import urlparse
def urlparse_fuc(url):
	print urlparse.urlparse(url)
	print urlparse.urldefrag(url)



import Queue
def queue_fuc():
	queue=Queue.deque([1,2,3,4,5])
	print queue
	print queue.pop()
	print queue.popleft()
	queue.append(2)
	print queue

import re

def re_team():
	name='''
	曼城vs曼联
	曼联vs斯托克顿
	利物浦vs曼城
	曼联vs热刺
	热刺vs阿森纳
	'''

	cia='''
		nba: 123
		cba:12
		fifa:1235
		cia:123
		利物浦vs曼城
		曼联vs热刺
		热刺vs阿森纳

	'''
	myleg=re.compile(".*曼城.*")
	print myleg.findall(cia)[0].decode("utf-8")


if __name__ == '__main__':
	# tmp3()
	# scrap_school_link("http://www.xynun.edu.cn/")
	# scrap_sportnews_link("https://www.zhibo8.cc/")
	# lxml_sportnews_link("http://www.zhibo8.cc/")
	# urlparse_fuc("www.baidu.com/123/12?name=123&pwd=123")
	# queue_fuc()
	re_team()
