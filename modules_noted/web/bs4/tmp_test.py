# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-23 15:51:46
# @Last Modified by:   admin
# @Last Modified time: 2018-03-26 16:35:23
from bs4 import BeautifulSoup
from alice_html import alice_docu
html=alice_docu()
def css_select(html):
	soup=BeautifulSoup(html,"lxml",from_encoding="utf-8")
	a=soup.select("body a")[0]
	print a.geturl

	# for label in p:
	# 	print label.text
	# 	print label.select("a[href]")
	# print soup.select(".sister")
	# # print soup.select("p a[href]=#")
	# print "空行"
	# li=soup.select("body a[href='#']")
	# print li
	# print "表格"
	# table=soup.select("div table th")
	# print table
	# a_text=soup.find_all("a")
	# tmp=""
	# for x in a_text:
	# 	tmp+=x.text
	# print tmp
	# print soup.select("a")




import urllib	
def retur(url):
	# urllib.urlretrieve(url,filename=r"F:\code\python\crawling\test\project\csv\pics\01.jpg")
	# print "ok "
	imgdict={}
	num=1
	imgdict[0]="helloworkd"
	print imgdict
	imgdict={1:"one",2:"two",3:"three"}
	for keyvalue in imgdict:
		print key,"-->",value
import urlparse
def urlretrieve_noted():
	# urllib.urlretrieve("https://imgcdn.zhibo8.cc/2018/03/24/cad41628c3c395862e39d588f8dc3f8d.jpg",r"F:\code\python\crawling\test\project\csv\zhiboba\pics\12.jpg")

	abspath=urlparse.urljoin("www.baidu.com/123/","456")
	print abspath
	print "ok "



import urllib2
def scrapy_img(html):
	# 接受传递来的文档
	# 解析出图片，并下载到本地
	soup=BeautifulSoup(html,"lxml")
	img=soup.select("div[id='image_wrap'] img")[0]
	print img
	# print img 
	urllib.urlretrieve("//imgcdn.zhibo8.cc/2018/03/24/9aedc958fb963e62ec2c684a79226d8a.jpg",r"F:\code\python\crawling\test\project\csv\zhiboba\pics\1.jpg" )
	# pass




if __name__ == '__main__':
	# css_select(html)
	# retur("https://tu.zhibo8.cc/uploads/2018/03/24/3d9db787d926592df3916d505ada3afb_thumb.jpg")
	# urlretrieve_noted()
	html=urllib2.urlopen("https://tu.zhibo8.cc/home/album/39852/2").read()
	scrapy_img(html)