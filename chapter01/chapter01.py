# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-02-19 13:35:19
# @Last Modified by:   admin
# @Last Modified time: 2018-03-06 11:50:55
# 第一章内容

# builtwith 模块，解析url，返回该网站所使用的技术
import builtwith
url_list=["http://www.xynun.edu.cn","http://www.163.com","http://example.webscraping.com","http://www.szytz12.com/"]

def builtwith_fuc():
	for link in url_list:
		print "网站名----%s" %link
		print builtwith.parse(link) 
# builtwith_fuc()

# whois 模块，查询网站或者域名的所有者
import whois
def whois_fuc():
	for link in url_list:
		print "网站名----%s" %link
		print whois.whois(link)
# whois_fuc()

# 三种方法来爬去网站，爬取网站地图，遍历每个网页的id，跟踪网页链接


# 代理支持  下面是使用urllib2支持代理的方法
# 没看懂
def proxy_fuc():
	proxy="123"
	opener=urllib2.build_opener()
	proxy_params={urlparse.urlparse(url).scheme:proxy}
	opener.add_handler(urllib2.ProxyHandler(proxy_params))
	response=opener.open(request)

# 重写并整理下载的代码
# 写一个自己的下载函数



		