# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-20 12:13:34
# @Last Modified by:   admin
# @Last Modified time: 2018-03-20 18:55:38
# 这个文件用来实现爬取页面

# 把整个页面的链接全部下载下来
from download2 import download
import re
def scrapy_link1(seed_url,link_regex):
	# 把所有连接中含有/places的链接全部爬取下来
	# 我的思路：把所有链接下载下来，然后存放到一个列表中，使用循环进行爬取
	'''crawl_queue=[]
	html=download(seed_url)
	all_urls=get_regex().findall(html)
	for url in all_urls:
		if re.match(link_regex,url):
			crawl_queue.append(url)
	'''
	# 使用数据结构栈来更完整的实现，出栈的是要爬取的地址，入栈的是爬取后的结果
	crawl_queue=[seed_url]
	while crawl_queue:
		url=crawl_queue.pop()
		html=download(url)
		for link in get_regex(html):
			if re.match(link_regex,link):
				crawl_queue.append(link)

import urlparse
def scrapy_link2(seed_url,link_regex):
	# 得到的路径很多都是相对路径，要把它变为绝对路径
	# 我的思路：在筛选后使用urlparse.join方法进行拼接，然后返回栈中
	crawl_queue=[seed_url]
	while crawl_queue:
		url=crawl_queue.pop()
		html=download(url)
		for link in get_regex(html):
			if re.match(link_regex,link):
				absurl=urlparse.urljoin(seed_url,link)
				crawl_queue.append(absurl)

	# 他的思路：一致

def scrapy_link3(seed_url,link_regex):
	# 爬取的链接中可能会有已经爬取过的链接，避免重复爬取
	# 我的思路： 在最后入栈前加入一个唯一性检查，如果已存在，则禁止入栈
	'''crawl_queue=[seed_url]
	while crawl_queue:
		url=crawl_queue.pop()
		html=download(url)
		for link in get_regex(html):
			if re.match(link_regex,link):
				absurl=urlparse.urljoin(seed_url,link)
				if absurl not in crawl_queue:
					crawl_queue.append(absurl)
	'''
	# 他的思路：在最后的入场检查中加入集合，如果之前从来没有进入过，则放行，否则禁止
	# 但是我觉得这里没必要用集合，因为如果之前从来没有进入过，直接用not in检查即可，已经足够筛选出想要的结果
	# 我明白为甚要加入集合了，因为栈中的数据每次都会进入后再出栈，但是集合里的数据并没有动，这可以实现对链接的唯一性检查
	crawl_queue[seed_url]
	seen=set(crawl_queue)
	while crawl_queue:
		url=crawl_queue.pop()
		html=download(url)
		for link in get_regex(html):
			if re.match(link_regex,link):
				abslink=urlparse.urljoin(seed_url,link)
				if abslink not in seen:
					seen.add(abslink)
					crawl_queue.append(abslink)


def scrapy_link4(seed_url,link_regex):
	# 爬取页面前先检查robot函数，如果允许爬取，则执行后面的代码
	# 我的思路：使用robotparser模块的can_fetch函数来检查是否允许爬取
	crawl_queue=[seed_url]
	seen=set(crawl_queue)
	rp=get_robot(seed_url)
	while crawl_queue:
		url=crawl_queue.pop()
		if rp.can_fetch(url):
			html=download(url)
			for link in get_regex(html):
				if re.match(link_regex,link):
					abslink=urlparse.urljoin(seed_url,link)
					if abslink not in seen:
						seen.add(abslink)
						crawl_queue.append(abslink)
		else:
			print "不允许爬取此链接"

def scrapy_link5(seed_url,link_regex,max_depth=2):
	# 避免爬虫陷阱：当页面里含有指向下一个页面的链接时，会爬取下一个页面的链接，而下一个页面又会有指向
	# 再下一个页面的链接，这是就掉入了爬虫陷阱，如果想要避免陷阱，则需要记录每次爬取到的页面时第几个，这就是
	# 深度，如果超过深度，则停止爬取
	# 我的思路：用地址关联一个数字，初始为0，然后每爬取一次，下一个链接的数字增为1，如果到达最大深度，则停止
	crawl_queue=[seed_url]
	seen={seed_url:0}
	rp=get_robot(seed_url)
	while crawl_queue:
		url=crawl_queue.pop()
		if rp.can_fetch(url):
			depth=seen[url]
			if depth !=max_depth:
				html=download(url)
				for link in get_regex(html):
					if re.match(link_regex,link):
						abslink=urlparse.urljoin(seed_url,link)
						if abslink not in seen:
							seen[abslink]=depth+1
							crawl_queue.append(abslink)
		
		else:
			print "不允许爬取此链接"

	# 他的思路：一致

import time
def scrapy_link6(seed_url,link_regex,max_depth,delay=2):
	# 避免爬取数据的速度太快，在爬取两个页面间添加延时来实现限速
	# 我的思路：
	'''crawl_queue=[seed_url]
	seen={seed_url:0}
	rp=get_robot(seed_url)
	while crawl_queue:
		url=crawl_queue.pop()
		depth=seen[url]
		if rp.can_fetch(url):
			if depth!= max_depth:
				time.sleep(delay)
				html=download(url)
				for link in get_regex(html):
					if re.match(link_regex,link):
						abslink=urlparse.urljoin(seed_url,link)
						if abslink not in seen:
							seen[abslink]=depth + 1
							crawl_queue.append(abslink)
						
		else:
			print "不允许爬取此链接"
	'''
	
	# 他的思路：直接使用time.sleep没有伸缩性，他希望爬取过程中，速度如果过快，则放慢；反之，则加快速度
	# 通过一个类的方式来实现下载限速

def scrapy_link7(seed_url,link_regex,max_depth=2,delay=3,num_retry=3):
	# 这里实现添加重试参数给download，
	# 把改为绝对路径进行函数封装
	# 添加域名检查，防止爬取外部链接
	crawl_queue=[seed_url]
	seen={seed_url:0}
	throttle=Throttle(delay)
	while crawl_queue:
		url=crawl_queue.pop()
		if rp.can_fetch(url):
			depth=seen[url]
			throttle.wait(url)
			if depth!=max_depth:
				html=download(url,num_retry)
				for link in get_regex(html):
					if re.match(link_regex,link):
						abslink=normalize(seed_url,link)
						if abslink not in seen:
							seen[abslink]=depth+1
						if samedomain:
							crawl_queue.append(abslink)
				
		else:
			print "不允许爬取此链接"
			
def scrapy_link8(seed_url,link_regex,max_depth=2,max_url=5,delay=4,num_retry=2,scrapy_callback=None):
	# 增加最大链接数，满足最大链接数后就停止爬取
	# 我的思路，设置一个计数器，每次在入栈时进行加一，检查是否等于最大连接数
	crawl_queue=[seed_url]
	seen={seed_url:0}
	num_url=0
	throttle=Throttle(delay)
	while crawl_queue:
		url=crawl_queue.pop()
		if rp.can_fetch(url):
			depth=seen[url]
			if depth!=max_depth:
				throttle.wait()
				html=download(url,delay)
				links=[]
				# 这里调用callback函数，返回筛选后的列表
				if link_regex:
					# links.extend(link for link in get_regex(html) if re.match(link_regex,link))
					link.extend(scrapy_callback(url,html) or [])
					for link in links:
						abslink=normalize(link)
						if abslink not in crawl_queue:
							seen[abslink]=depth+1
						if samedomain:
							crawl_queue.append(abslink)
			num_url+=1
			if num_url==max_url:
				break

		else：
			print "不允许爬取此链接"


scrapy_link=scrapy_link8


# 检查是否为本网站链接
def samedomain(url1,url2):
	return urlparse.urlparse(url1).netloc==urlparse.urlparse(url2).netloc

# 改为绝对路径
def normalize(baseurl,url):
	link,_=urlparse.urldefrag(url)
	return urlparse.urljoin(baseurl,link)



from datetime import datetime
class Throttle():
	"""# 下载限速"""
	def __init__(self, delay):
		self.delay = delay
		self.domain={}
	def wait(self,url):
		domain=urlparse.urlparse(url).netloc
		last_accessed=self.domain.get(domain)
		if self.delay>0 and last_accessed is not None:
			sleep_sec=self.delay-(datetime.now()-last_accessed).seconds
			if sleep_sec>0:
				time.sleep(sleep_sec)
		self.domain[domain]=datetime.now()



import robotparser
def get_robot(url):
	# 这个函数返回robot文件的内容
	rp=robotparser.RobotFileParser()
	rp.set_url(url,"/robot.txt")
	rp.read()
	return rp



def get_regex(html):
	# 返回一个构造链接的正则对象
	# return re.compile('<a[^>]+href=["\'](.*?)["\']>',re.IGNORECASE)

	# 另一种方式
	web_regex=re.compile('<a[^>]+href=["\'](.*?)["\']>',re.IGNORECASE)
	return web_regex.findall(html)



if __name__ == '__main__':
	scrapy_link("http://example.webscraping.com","/places")