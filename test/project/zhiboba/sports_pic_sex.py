# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-15 16:24:21
# @Last Modified by:   admin
# @Last Modified time: 2018-03-15 17:09:08
# 爬取直播吧的图片，找到以下关键字的参数所在的图片，下载图片地址和文本内容

# 导入模块
import re
import urllib2
from bs4 import BeautifulSoup
import urlparse
# 下载函数
def download(html):
	html=urllib2.urlopen(html).read()
	return html

# 爬取函数
def scrapy_pic(html):
	# 下载关键字所在的图片
	# 关键字包括人妻，美女，女神，性感，美腿，网红，宝贝，青春，健身，写真
	soup=BeautifulSoup(html,"lxml")
	word_regex=re.compile(u".*(美腿|女神|性感|网红|宝贝|青春|健身|写真)")
	tag_div=soup.find_all("div",class_=re.compile("boxlist"))
	for link in tag_div:
		if word_regex.match(link.img.get("alt")):
			print "图片地址：",abs_path("https://tu.zhibo8.cc/", link.a.get("href"))
			print "图片内容：",link.img.get("alt")
	return

def abs_path(domain,url):
	return urlparse.urljoin(domain, url)

# 主函数
if __name__ == '__main__':
	html=download("https://tu.zhibo8.cc/")
	scrapy_pic(html)
