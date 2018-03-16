# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-09 10:24:20
# @Last Modified by:   admin
# @Last Modified time: 2018-03-09 16:52:05
# 爬取网页内容，抽取每个页面的链接以及相关网页的链接
# 注意的点
# 在每次爬取之间添加延迟，可以避免被封禁，延迟时间=设定的延迟-(两次访问的时间差)
# 传入地址，使用双向队列方式，从一边进入，另一边出来，
# 地址检查，使用seen字典来保证下载过的链接不会再次下载
# 正则表达式，设置设置匹配的链接
# 最大深度，设置爬取的链接的最大深度，只怕去有限个链接
# 最大url，设置爬取url的最大数目
# robot.txt 构造robot解析函数，查看是否允许爬取
# 构造header，用在robot上
# 用户代理，用在robot上


import re
import urllib2
import urlparse
from datetime import datetime
import time
import Queue
import robotparser
from download import download

def link_crawl(seed_url,link_regex,max_depth=3,max_url=4,user_agent="wxwp",headers=None):
	crawl_queue=Queue.deque([seed_url])
	seen={seed_url:0}
	num_url=0
	throttle=Throttle(delay=2)
	rp=get_robots(seed_url)
	headers=headers or {}
	if user_agent:
		headers["User-agent"]=user_agent
	while crawl_queue:
		url=crawl_queue.pop()
		if rp.can_fetch(user_agent,url):
			throttle.wait(url)
			html=download(url)
			links=[]
			depth=seen[url]
			if depth!=max_depth:
				if link_regex:
					links.extend(link for link in get_link(html) if re.match(link_regex,link))
					print links
				for link in links:
					link=normalize(seed_url,link)
					if link not in seen:
						seen[link]=depth+1
						crawl_queue.append(link)
						for x in crawl_queue:
							print x
			num_url+=1
			if num_url==max_url:
				break

		else:
			"robot文件不允许爬取此链接"

def get_robots(url):
	rp=robotparser.RobotFileParser(url)
	rp.set_url(urlparse.urljoin(url,"/robot.txt"))
	rp.read()
	return rp

def normalize(seed_url,link):
	link,_=urlparse.urldefrag(link)
	return urlparse.urljoin(seed_url, link)

def get_link(url):
	webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	return webpage_regex.findall(url)


class Throttle:
	"""添加延迟类"""
	def __init__(self, delay):
		
		self.delay = delay
		self.domain={}
	def wait(self,url):
		domain=urlparse.urlparse(url).netloc
		lastaccess_time=self.domain.get(domain)
		if lastaccess_time is not None and self.delay>0:
			time_sleep=self.delay-(datetime.now()-lastaccess_time).seconds
			if time_sleep>0:
				time.sleep(time_sleep)
		self.domain[domain]=datetime.now()

if __name__ == '__main__':
	link_crawl("http://example.webscraping.com", "/places")