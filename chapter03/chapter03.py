# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-01 10:44:59
# @Last Modified by:   admin
# @Last Modified time: 2018-03-01 11:25:42
# 构建缓存技术

# 重写下载函数，构建成一个类
import random,urllib2
from chapter01 import Throttle,robot_fuc
class Downloader:
	def __init__(self, delay=5,user_agent="wswp",proxies=None,num_retries=1,cache=None):
		self.throttle=Throttle(delay)
		self.user_agent = user_agent
		self.proxies=proxies
		self.num_retries=num_retries
		self.cache=cache
	def __call__(self,url):
		result=None
		# 先检查缓存是否已被定义，然后检查定义的缓存中是否有指定的url
		if self.cache:
			try:
				result=self.cache[url]
			except KeyError :
				# url没在缓存中
				pass
		else:
			# 如果缓存没有被定义，则检查是否遇到了服务器错误
			if self.num_retries>0 and 500<=result["code"]<600:
				# 服务器错误，忽略缓存结果，然后重新下载
				result=None
		# 如果url已经被缓存，但是没有被找到，则检查是否下载中遇到了服务器错误
		if result is None:
			# 表示没有缓存载入，需要重新下载
			self.throttle.wait(url)
			if self.proxies:
				proxy=random.choice(self.proxies)
			else:
				proxy=None
			headers={"User-agent":self.user_agent}
			result=self.download(url,headers,proxy,self.num_retries)
			if self.cache:
				# 如果缓存已经被定义，则把result中的结果写入缓存中
				self.cache[url]=result
		return result["html"]
	# 这里的下载函数代码不正确，完整的在网站上下载
	def download(self,url,headers,proxy,num_retries,data=None):
		print "downloading",url
		# 在request中构造代理用户名
		headers={"Usr=agent":user_agent}
		request=urllib2.Request(url,headers=headers)
		try:
			html=urllib2.urlopen(url).read()
		except urllib2.URLError as e:
			print "download error: ",e.reason
			html=None
			if num_retries>0:
				if hasattr(e,"code") and 500<=e.code<=600:
					return download_agentname(url,user_agent,num_retries-1)
		return {"html":html,"code":code}

def link_crawler(seed_url,link_regex,cache=None):
	crawl_queue=[seed_url]
	seen={seed_url:0}
	num_urls=0
	rp=robots_fuc(seed_url)
	D=Downloader(delay=delay,)
