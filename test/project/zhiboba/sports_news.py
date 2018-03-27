# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-13 11:24:29
# @Last Modified by:   admin
# @Last Modified time: 2018-03-26 11:17:52

import urllib2
from bs4 import BeautifulSoup
import re
BrowserAgent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
def download(url,user_agent=BrowserAgent,num_retry=2):
	# 下载网页
	headers={"User-Agent":user_agent}
	req=urllib2.Request(url,headers=headers)
	try:
		html=urllib2.urlopen(req).read()
	except urllib2.URLError as e:
		print "download error: ",e.reason
		html=None
		if hasattr(e,"code") and 500<=e.code<=600:
			download(url,user-agent,num_retry-1)
	return html


def scrapy_text(html):
	# 下载首页内容
	soup=BeautifulSoup(html,"lxml")
	soup_left_top=soup.find_all(attrs={"class":"r_video left"})[0]
	#匹配链接
	myteam=re.compile(u"曼城")
	myteam_list=[u"足球新闻"]
	if soup_left_top:
		for tag_a in soup_left_top.find_all("a"):
			# if myteam.findall(tag_a.text):
			# 	print "曼城新闻：",tag_a["href"]
			# else:
			# 	print tag_a.text

			# 返回所有的文本到一个列表当中去
			if tag_a.text:
				myteam_list.append(tag_a.text)
		return myteam_list

	print "="*20
	soup_right_top=soup.find_all(attrs={"class":"r_news right"})[0]
	if soup_right_top:
		for tag_a in soup_right_top.find_all("a"):
			print tag_a.text

	print "="*20
	soup_left_bottom=soup.find_all(attrs={"class":"r_video left"})[1]
	if soup_left_bottom:
		for tag_a in soup_left_bottom.find_all("a"):
			print tag_a.text

	print "="*20
	soup_right_bottom=soup.find_all(attrs={"class":"r_news right"})[1]
	if soup_right_bottom:
		for tag_a in soup_right_bottom.find_all("a"):
			print tag_a.text

from bs4 import SoupStrainer
def scrapy_title(html):
	# 这个函数用来联系bs的对于title和head的爬取
	# only_title=SoupStrainer("")
	# 告诉bs页面的编码方式
	soup=BeautifulSoup(html,"lxml",from_encoding="utf-8")
	# 设置页面被处理后的编码方式,prettify返回的是字符串
	# soup=soup.prettify("utf-8")
	print "标题： ",soup.title.name
	print "标题名字",soup.title.string
	metas=soup.find_all("meta")
	for meta in metas:
		# 打印属性如果使用attrs，则不支持中文显示，会以默认python编码打印；
		print meta
		print meta.attrs
	print soup.title.parent.name
	print soup.title.parent.string
	# 打印引用的js的地址
	for js in soup.head.find_all("script"):
		print js.attrs







def scrapt_body(html):
	soup=BeautifulSoup(html,"lxml",from_encoding="utf-8")
	# 这个函数联系body中的标签和筛选
	menu=soup.body.find("div",class_="menu")
	print "输出菜单里的所有链接"
	for link in menu.find_all("a"):
		if link.string:
			print link.string+"		>>>>>>>>>		"+link.get("href")
	print "另一种方法"
	# 使用strings可以返回一个包含子节点所有文档的列表
	# for link_string in menu.ul.strings:
	# 	if link_string != "\n":
	# 		print link_string
	# 去除空行的方法也可以采用stripped_strings
	print "去除空行"
	# for link_string in menu.ul.stripped_strings:
	# 	print link_string

def scrapy_child_parent(html):
	soup=BeautifulSoup(html,"lxml")
	recommend=soup.find("div",id="recommend")
	# 这个函数用来练习子节点与父节点

	# 对子节点进行跌代,children返回所有直接子节点,它返回字符串对象，不可以获取属性等方法
	# for child in recommend.children:
	# 	if child.name:
	# 		print child.name
	# 返回所有子孙节点
	desc=list(recommend.descendants)
	num=1
	# for child_son in desc:
	# 	# 迭代的时候会先返回空行，我也不知道为啥
	# 	# 所以在以后使用子孙节点时，一定要排除空行
	# 	if child_son.name:
	# 		print child_son
	# 		num+=1
	# 		if num>2:
	# 			break

	# 递归父元素
	for parent in recommend.parents:
		print parent.name
		print parent.string

def scrapy_search(html):
	soup=BeautifulSoup(html,"lxml",from_encoding="utf-8")
	# 这个函数联系搜索文档树的方法

	# 使用正则表达式来搜索
	menu=soup.find("div",class_="menu")
	# for link_li in menu.find_all(["a"]):
	# 	print link_li["href"]
	# 使用方法来搜索,实现更精确的查找
	# def has_href_and_has_title(tag):
	# 	return tag.has_attr("href") and tag.has_attr("title")
	# for title_link in soup.find_all(has_href_and_has_title):
	# 	print title_link

	# find_all输出方法的匹配
	for link in menu.find_all("a",title=True):
		print link
	for link in soup.find_all("a",text=re.compile(u"曼城|巴萨")):
		print link.string,link["href"]
	# 限制搜索的深度
	for news in soup.find_all(text=re.compile(u"曼城|巴萨|曼联|穆里尼奥"),limit=49):
		print news.string

	# css选择器
	


if __name__ == '__main__':
	html=download("https://www.zhibo8.cc/")
	print scrapy_text(html)
	# scrapy_title(html)
	# scrapt_body(html)
	# scrapy_child_parent(html)
	# scrapy_search(html)