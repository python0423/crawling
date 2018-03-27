# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-23 11:44:10
# @Last Modified by:   admin
# @Last Modified time: 2018-03-23 12:00:37
# 这里探讨cookielib模块
import cookielib
import urllib2

def cookie_jar(url):
	# 捕捉内存cookie，使用cookiejar
	cookie=cookielib.CookieJar()
	handler=urllib2.HTTPCookieProcessor(cookie)
	# 自定义一个请求对象
	opener=urllib2.build_opener(handler)
	opener.open(url)
	for cookie_single in cookie:
		print "请求的cookie:",cookie_single
		print "cookie_single 名字",cookie_single.name 
		print "cookie值：",cookie_single.value
		print "cookie端口",cookie_single.port
		print "cookie路径",cookie_single.path
		print "cookie_single expires",cookie_single.expires
	


if __name__ == '__main__':
	cookie_jar("http://www.xynun.edu.cn")
