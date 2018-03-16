# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-05 12:19:58
# @Last Modified by:   admin
# @Last Modified time: 2018-03-05 12:39:45
# 方法三：通过跟踪链接的方式，来访问下载内容
import re
from download_fuc import download
def link_crawler(seed_url,link_regex):
	# 通过正则表达式匹配链接，然后把链接爬取下来
	# 要爬取的列表
	crawl_queue=[seed_url]
	while crawl_queue:
		# 当爬取队列里有连接时，使用出栈方式逐个爬取
		url=crawl_queue.pop()
		html=download(url)
		# 匹配下载的页面的所有连接
		for link in get_links(html):
			if re.match(link_regex,link):
				crawl_queue.append(link)

def get_links(html):
	# 返回一个包含链接的列表
	webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']>',re.IGNORECASE)
	return webpage_regex.findall(html)

if __name__ == '__main__':
	link_crawler('http://example.webscraping.com', '/(index|view)')