# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-17 12:11:07
# @Last Modified by:   admin
# @Last Modified time: 2018-03-23 15:11:00
# 本程序用来模仿简单的登录
import requests
import urllib2
from urllib import urlencode
import cookielib
from bs4 import BeautifulSoup
def login_example(url):
	# 登录example
	data={"email":"cia@qq.com","password":"ciacia"}
	en_data=urlencode(data)
	req=urllib2.Request(url)
	req.add_data(en_data)
	response=urllib2.urlopen(req)
	print response.geturl()

def login_example2(url):
	# 登录example，传递formkey
	data=print_input(url)
	data["email"]="cia@qq.com"
	data["password"]="ciacia"
	en_data=urlencode(data)
	req=urllib2.Request(url,en_data)
	response=urllib2.urlopen(req)
	print response.geturl()


def login_example3(url):
	# 把formkey添加到cookie中
	cj=cookielib.CookieJar()
	# 构造一个opener对象
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	html=opener.open(url).read()
	data=print_input(html)
	data["email"]="cia@qq.com"
	data["password"]="ciacia"
	en_data=urlencode(data)
	req=urllib2.Request(url,en_data)
	# 这里要用opener来请求，否则没有cookie
	response=opener.open(req)
	print response.geturl()

def login_hi_houbai(url):
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	html=opener.open(url).read()
	data=print_input(html)
	#添加信息
	data["account"]="trevor.fzp"
	data["pwd"]="111111"
	en_data=urlencode(data)
	# 构造请求
	req=urllib2.Request(url,en_data)
	html=opener.open(req).read()
	soup=BeautifulSoup(html,"lxml")
	div=soup.find("div",_class="con")
	li=div.find("li",_class="u_name")
	print li.text


def renren_login(url):
	# 登录人人
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	html=opener.open(url).read()
	data=print_input(html)
	#添加信息
	email="18785922485"
	password="ciaciaf"
	data[None]=data.get(None).encode("utf-8")
	data["email"]=email
	data["password"]=password
	en_data=urlencode(data)
	header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
	req=urllib2.Request(url,headers=header,data=en_data)
	response=opener.open(req)
	print response.geturl()
	
def spurs(url):
	# 登录园艺论坛  失败，因为无法绕过验证码
	username="viber123"
	password="ciacia123"
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	html=opener.open(url).read()
	data=print_input(html)
	data["username"]=username
	data["password"]=password
	data["srchtxt"]=data.get("srchtxt").encode("utf-8")
	en_data=urlencode(data)
	req=urllib2.Request(url,en_data)
	response=opener.open(req)
	print response.geturl()





def print_input(html):
	# 打印页面的所有input标签中的name和value
	soup=BeautifulSoup(html,"lxml")
	forms=soup.find_all("form")
	da_dict={}
	for form in forms:
		inputs=form.find_all("input")
		for input in inputs:
			da_dict[input.get("name")]=input.get("value")

	return da_dict


if __name__ == '__main__':
	# url="http://example.webscraping.com/places/default/user/login"
	# login_example("http://example.webscraping.com/places/default/user/login")
	# print_input("http://example.webscraping.com/places/default/user/login")
	# login_example2(url)
	# login_example3(url)

	# 登录人人  失败
	# html=urllib2.urlopen("http://zhan.renren.com/login").read()
	# print print_input(html)
	# renren_login("http://zhan.renren.com/login")

	# 登录马刺论坛
	# 先判断表单里有什么
	# html=urllib2.urlopen("http://www.spursgo.com/").read()
	# print print_input(html)
	# 失败

	# 登录园艺论坛
	# html=urllib2.urlopen("http://www.mshua.net/bbs/member.php?mod=logging&action=login").read()
	# print print_input(html)
	# 第二步：构造cookie，尝试登录
	spurs("http://www.mshua.net/bbs/member.php?mod=logging&action=login")



	# 打印头信息
	# r=requests.get("http://webiadmin.speakhi.com/bgmanagementadmin")
	# print r.headers


