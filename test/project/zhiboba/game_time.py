# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-15 12:12:26
# @Last Modified by:   admin
# @Last Modified time: 2018-03-20 12:03:46
# 这个程序用来爬取关心的球队的比赛日期
# 足球队包括：巴萨，曼城，曼联
# 篮球队包括：马刺
import urllib2
from bs4 import BeautifulSoup
import re
from csv_noted import UnicodeWriter,writen_bask


# 下载页面函数
def download(url):
	# 下载网页
	html=urllib2.urlopen(url).read()
	return html

#筛选马刺比赛日期，包括对手，比赛时间
def scrapy_basketball(html):
	print "写入接下来二十天的马刺比赛："
	bask_text=[]
	soup=BeautifulSoup(html,"lxml",from_encoding="utf-8")
	li_basketball=soup.find_all("li",label=re.compile(u"马刺"))
	# 添加到csv文件中，使用追加模式
	for basketball_data in li_basketball:
		clear_text(basketball_data, "a")
		bask_text.append(basketball_data["data-time"])
		bask_text.append(basketball_data.text)
		print bask_text
		if bask_text:
			writen_bask("w_data.csv",bask_text)
		bask_text=[]
	return

#筛选足球队，包括对手，比赛日期
def scrapy_football(html):
	soup=BeautifulSoup(html,"lxml",from_encoding="utf-8")
	li_football=soup.find_all("li",label=re.compile(u"曼城|巴塞罗那|曼联|利物浦"))
	for football_data in li_football:
		clear_text(football_data, "a")
		foot_text=football_data["data-time"],"--->>>",football_data.text 
	return foot_text


# 清空列表的直接子节点的内容，只保留本身的文本
def clear_text(tag,tag_child):
	for tag in tag.find_all(tag_child):
		tag.string=""
	return 





#主函数，从直播吧筛选
if __name__ == '__main__':
	html=download("https://www.zhibo8.cc/")
	scrapy_basketball(html)
	# print ">"*40
	# print "接下来二十天关于足球的比赛"
	# scrapy_football(html)
