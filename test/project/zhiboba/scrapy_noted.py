# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-26 14:44:19
# @Last Modified by:   admin
# @Last Modified time: 2018-03-27 11:26:39
# 爬去函数

import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import csv
import urlparse
from datetime import datetime 
import time
import string
import random
def scrapy_text(html):
	# 下载首页内容
	soup=BeautifulSoup(html,"lxml")
	soup_left_top=soup.find_all(attrs={"class":"r_video left"})[0]
	#匹配链接
	myteam=re.compile(u"曼城")
	myteam_list=[]
	if soup_left_top:
		for tag_a in soup_left_top.find_all("a"):
			# if myteam.findall(tag_a.text):
			# 	print "曼城新闻：",tag_a["href"]
			# else:
			# 	print tag_a.text

			# 返回所有的文本到一个列表当中去
			if tag_a.text:
				myteam_list.append(tag_a.text.encode("utf-8"))
		myteam_list.append("\n")
	soup_right_top=soup.find_all(attrs={"class":"r_news right"})[0]
	if soup_right_top:
		for tag_a in soup_right_top.find_all("a"):
			if tag_a.text:
				myteam_list.append(tag_a.text.encode("utf-8"))
		myteam_list.append("\n")
	soup_left_bottom=soup.find_all(attrs={"class":"r_video left"})[1]
	if soup_left_bottom:
		for tag_a in soup_left_bottom.find_all("a"):
			if tag_a.text:
				myteam_list.append(tag_a.text.encode("utf-8"))
		myteam_list.append("\n")

	soup_right_bottom=soup.find_all(attrs={"class":"r_news right"})[1]
	if soup_right_bottom:
		for tag_a in soup_right_bottom.find_all("a"):
			if tag_a.text:
				myteam_list.append(tag_a.text.encode("utf-8"))
	return myteam_list

def csv_file(data,filename):
	# data是一个列表，把数据写入列表中
	header=["id","news"]
	data_dict=[]
	with open(filename,"w") as f:
		f_csv=csv.DictWriter(f,header)
		f_csv.writeheader()
		for id in range(len(data)):
			f_csv.writerow({"id":id,"news":data[id]})
			print "第%d条新闻写入" %id

def scrapy_soccer(html):
	# 爬取足球新闻
	# div 名字是video v_change 有多个； 包含两部分：超链接和列表；
	# 超链接的文本是分开的，所以要合并
	# 列表的文本每个单独成行
	# 最后返回一个文本列表
	soup=BeautifulSoup(html,"lxml")
	news=[]
	tmp=""
	# 爬去新闻条目
	# divs=soup.select("div[class='video v_change'] div[class='content']")
	# for div in divs:
	# 	for li in div.select("li"):
	# 		news.append(li.text.encode("utf-8"))
	# 	news.append("\n")
	# return news

	# 只筛选去英超的新闻
	div=soup.select("div[class='video v_change'] div[class='content']")[1]
	for li in div.select("li"):
		news.append(li.text.encode("utf-8"))
	news.append("\n")
	return news
def img_download(html,url):
	# 下载图片到本地
	# 先获取图片地址
	img_list=[]
	soup=BeautifulSoup(html,"lxml")
	divs=soup.select("div[class='boxlist4-i']")
	for div in divs:
		a=div.select("a[class='pica1']")[0]
		# print "图片名称：",a.img["alt"]
		pic_link=a.img["data-original"]
		pic_link=normalize(url,pic_link)
		# print "图片地址:",pic_link
		img_list.append(pic_link)
	print len(img_list)
	img_dist={}
	num=100
	for addr in img_list:
		# 每个图片编号
		img_dist[num]=addr
		num+=1
	# 下载到本地
	for key in img_dist:
		urllib.urlretrieve(img_dist[key],filename=r"F:\code\python\crawling\test\project\csv\pics\%d.jpg" %key) 

def normalize(baseurl,url):
	# 绝对路径

	link,_=urlparse.urldefrag(url)
	return urlparse.urljoin(baseurl,url)


# 批量下载图片，爬去每个图片的地址，然后下载每个图片背后的组图
import random
class Throttle:
	"""# 添加延迟"""
	def __init__(self, delay):
		self.delay = delay
		self.domain={}
	def wait(self,url):
		domain=urlparse.urlparse(url).netloc
		last_accessed=self.domain.get(domain)
		if last_accessed is not None and self.delay>0:
			sleep_time=self.delay-(datetime.now()-last_accessed).seconds
			if sleep_time> 0:
				time.sleep(sleep_time)
		self.domain[domain]=datetime.now()



class ImgScrapy:
	"""docstring for ImgScrapy"""
	def __init__(self,url,delay=2):
		self.url=url
		self.dw=Download()
		self.throttle=Throttle(delay)

	def normalize(self,baseurl,url):
		# 绝对路径
		link,_=urlparse.urldefrag(url)
		return urlparse.urljoin(baseurl,url)

	def scrapy_thumb_addr(self,html):
		# 爬去每个缩略图的地址
		soup=BeautifulSoup(html,"lxml")
		divs=soup.select("div[class='boxlist4-i']")
		thumb_addr_dict={}
		for div in divs:
			a=div.select("p a")[0]
			a_link=a.get("href")
			# 得到绝对路径
			abs_link=normalize(self.url,a_link)
			thumb_addr_dict[a.text]=abs_link+"/"
		# 返回所有的由名称和地址构成的字典
		return thumb_addr_dict

	def iter_addrs(self,addr_dict):
		# 迭代每个地址，并把下载到的html返回
		# 交给下一个函数处理图片
		for name in addr_dict:
			# print addr_dict[name]
			for id in range(1,10):
				# 拼接下载地址，然后下载
				abspath=urlparse.urljoin(addr_dict[name],str(id))
				# print abspath
				self.throttle.wait(abspath)
				html=self.dw.download(abspath)
				# print len(html)
				fn="".join(random.sample(string.ascii_letters+string.digits,12))
				scrapy_img(html,fn)
			print name,"下载完成"

def scrapy_img(html,fn):
	# 接受传递来的文档
	# 解析出图片，并下载到本地
	soup=BeautifulSoup(html,"lxml")
	img=soup.select("div[id='image_wrap'] img")[0]
	# print img 
	# print img["src"]
	img['src']="https:"+img["src"]
	print img["src"]
	urllib.urlretrieve(img["src"],r"F:\code\python\crawling\test\project\csv\zhiboba\pics\%s.jpg" %fn)
	# pass

if __name__ == '__main__':
	# html=download("https://www.zhibo8.cc/")
	# print scrapy_text(html)
	# csv_file(scrapy_text(html))

	# 足球新闻
	# html=download("https://news.zhibo8.cc/zuqiu/")
	# scrapy_list=scrapy_soccer(html)
	# csv_file(scrapy_list,"soccer_news.csv")

	# 图片下载
	# 把图片下载到本地，存放在某个文件夹中
	# pic_addr="https://tu.zhibo8.cc/zuqiu"
	# html=download(pic_addr)
	# img_download(html,pic_addr)

	# 可变地址组图下载
	from download import Download 
	soccer_addr="https://tu.zhibo8.cc/zuqiu"
	pic_addr="https://tu.zhibo8.cc/"
	# 下载网页
	dw=Download()
	html=dw.download(soccer_addr)
	# 开始爬取
	imgsp=ImgScrapy(pic_addr)
	img_addr_dict=imgsp.scrapy_thumb_addr(html)   #得到由名称和跳转地址构成的页面
	# print img_addr_dict
	imgsp.iter_addrs(img_addr_dict)







