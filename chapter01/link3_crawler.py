# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-06 11:11:51
# @Last Modified by:   admin
# @Last Modified time: 2018-03-06 12:53:41

# 完整的爬虫代码
import re
import urlparse
import urllib2
import robotparser
import Queue
import time
from datetime import datetime
from download_fuc import download
class Throttle():
	"""在两次爬虫之间添加延时，以避免被封禁或者服务器过载"""
	def __init__(self, delay):
		self.delay = delay
		self.domains={}
	def wait(self,url):
		# netloc返回的是域名
		domain=urlparse.urlparse(url).netloc
		last_accessed=self.domains.get(domain)

		if self.delay>0 and last_accessed is not None:
			sleep_secs=self.delay-(datetime.now()-last_accessed).seconds
			if sleep_secs>0:
				time.sleep(sleep_secs)
		self.domains[domain]=datetime.now()


def link_crawler(seed_url,link_regex,delay=3,max_depth=-1,max_urls=-1,headers=None,user_agent="wxwp",proxy=None,num_retries=2):
	# seed_url是传入的地址；link_regex是正则表达式，匹配所修的网页；delay是设定的延迟时间
	# max_depth是设定的最大深度，-1表示无限制；max_urls 不知道
	# headers是设定代理时构造的浏览器头文件；user_agent是设定用户代理名；proxy是支持代理
	# num_retries是设定重试下载的次数

	# deque创建一个双向队列，返回的是一个队列对象，里面存放的是爬取的地址队列
	crawler_queue=Queue.deque([seed_url])
	# seen变量检查哪些地址已经被下载过
	seen={seed_url:0}
	# 追踪已经下载了多少个地址
	num_urls=0
	# 检查robot文件，依照robot设定的来爬取，rp返回的是robot文件的内容
	rp=get_robots(seed_url)
	throttle=Throttle(delay=5)
	headers=headers or {}
	# 如果用户代理存在，则构造头文件,使用代理
	if user_agent:
		headers["User_agent"]=user_agent
	while crawler_queue:
		# 逐个取出队列中的地址
		url=crawler_queue.pop()
		# 检查robot文件限制，看看是否允许爬取
		if rp.can_fetch(user_agent,url):
			#设置爬取速度的限制，每一个地址都要等待几秒钟再进行爬取
			throttle.wait(url)
			#使用download函数下载网页内容
			html=download(url,headers,proxy=proxy,num_retries=2)
			links=[]
			# 获取爬取深度设置
			depth=seen[url]
			if depth != max_depth:
				# 如果没达到最大深度，则继续爬取
				if link_regex:
					# 如果正则表达式存在，则通过get_links函数过滤出所需要的链接，添加到links列表中
					# links列表中存放的是页面的所有链接，包括相对路径的，也有绝对路径的
					links.extend(link for link in get_links(html) if re.match(link_regex,link))
				for link in links:
					# 标准化这个链接，因为是相对链接，所以要拼接一下
					link=normalize(seed_url,link)
					# 检查是否已经爬取过这个链接
					if link not in seen:
						seen[link]=depth+1
						# 检查一下是否是同一个域名下的链接，防止爬取外部链接
						if same_domain(seed_url,link):
							crawler_queue.append(link)
			num_urls+=1
			if num_urls==max_urls:
				# 如果爬取链接的数量达到最大链接，则停止
				break 
		else:
			print "robot不允许爬取此链接"


def get_robots(url):
	# 返回的是robot文件的内容
	rp=robotparser.RobotFileParser()
	rp.set_url(urlparse.urljoin(url,"/robots.txt"))
	rp.read()
	return rp

def get_links(html):
    """Return a list of links from html 
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

def same_domain(url1,url2):
	return urlparse.urlparse(url1).netloc==urlparse.urlparse(url2).netloc

def normalize(seed_url,link):
	# 把爬取到的链接全部改为绝对路径
	link,_=urlparse.urldefrag(link)
	return urlparse.urljoin(seed_url, link)


if __name__ == '__main__':
	# link_crawler("http://example.webscraping.com", "/places",delay=1,num_retries=2,user_agent="BadCrawler",max_depth=1)
		link_crawler("http://example.webscraping.com", "/places",delay=1,num_retries=2,user_agent="BadCrawler",max_urls=8)