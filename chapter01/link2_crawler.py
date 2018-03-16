# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-05 12:41:27
# @Last Modified by:   admin
# @Last Modified time: 2018-03-05 12:57:02
# 使用绝对路径来处理相关网页
import urlparse,re
from download_fuc import download

def link_crawler(seed_url,link_regex):
	crawl_queue=[seed_url]
	# 用集合存放链接，后面检查一下链接是否已被爬取过，集合是有唯一性
	seen=set(crawl_queue)
	while crawl_queue:
		url=crawl_queue.pop()
		html=download(url)
		for link in get_links(html):
			if re.match(link_regex,link):
				link=urlparse.urljoin(seed_url, link)
				# 如果链接不在集合里，加入进去；如果链接在集合里，则直接舍弃
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)

def get_links(html):
    """Return a list of links from html 
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

if __name__ == '__main__':
	link_crawler('http://example.webscraping.com', '/places/')