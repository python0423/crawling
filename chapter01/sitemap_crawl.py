# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-05 11:51:29
# @Last Modified by:   admin
# @Last Modified time: 2018-03-05 11:55:51
# 方法一 爬取网站地图，使用rebot.txt中发现的网站地图来下载所有网页
import re
from download_fuc import download

def crawl_sitemap(url):
	# 这里的url是网站中rebot.txt的地址
	sitemap=download(url)
	# 把网页中的链接抽取出来
	links=re.findall("<loc>(.*?)</loc>", sitemap)
	# 下载每一个链接
	for link in links:
		html=download(link)
		# 开始爬取页面
		# 。。。

if __name__ == '__main__':
	print crawl_sitemap("http://example.webscraping.com/sitemap.xml")
