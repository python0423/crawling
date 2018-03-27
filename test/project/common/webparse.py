# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-26 09:16:51
# @Last Modified by:   admin
# @Last Modified time: 2018-03-26 10:57:24
# 这个文件编写文档解析器
# 具体要求：从下载器中获取已经下载的html网页，解析出新的url给url管理器
# 解析出有效的数据交给数据存储器
from download import Download 
from bs4 import BeautifulSoup
import urllib2
from robotparser import RobotFileParser
import urlparse
from datetime import datetime
import time
class Throttle:
	"""# 添加延迟"""
	def __init__(self, delay):
		self.delay = delay
		self.domain={}
	def wait(self,url):
		domain=urlparse.urlparse(url).netloc
		last_accessed=self.domain.get(domain)
		if last_accessed is not None and self.delay>0:
			sleep_time=self.delay-(datetime.now()-last_accessed).seconds
			if sleep_time> 0:
				time.sleep(sleep_time)
		self.domain[domain]=datetime.now()
		
		

class Scrapy_html:
	'''用不同的方法解析出不同的数据 '''
	def __init__(self,url):
		self.rp=RobotFileParser()
		self.url=url
	def getrobot(self,url):
		# 检查robot文件
		rp=RobotFileParser()
		rp.set_url(urlparse.urljoin(self.url,"/robot.txt"))
		rp.read()
		return rp
	def normalize(self,baseurl,url):
		# 绝对化路径
		link,_=urlparse.urldefrag(url)
		return urlparse.urljoin(baseurl,link)

	def scrapy_url(link_regex=None,delay=3,num_retry=2):
		# 筛选页面中所有的链接，返回一个未爬去的url的列表
		crawl_url=[self.url]
		throttle=Throttle(delay=3)
		while crawl_url:
			url=crawl_url.pop()
			rp=getrobot(url)
			# 如果允许爬取
			if rp.can_fetch():
				# 下载限速
				throttle.wait(url)
				html=Download(url).download_html()
				soup=BeautifulSoup(html,"lxml")
				if link_regex:
					# 如果有正则表达式
					for link in soup.select("a[href]"):
						if re.match(link_regex,link) 
							link=normalize(url,link)  # 如果匹配到则把这个连接改为绝对路径
							crawl_url.append(link)
							return crawl_url
				else:
					for link in soup.select("a[href]"):
						link=normalize(url,link)
						crawl_url.append(link)
						return crawl_url


# 可以进行扩展添加其他下载所需要的东西

						
						








	
		