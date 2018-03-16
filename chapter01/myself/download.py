# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-09 10:12:58
# @Last Modified by:   admin
# @Last Modified time: 2018-03-09 10:23:53
# 下载函数:传递url，下载页面内容
# 注意的点
# 捕获异常：如果遇到服务器错误(5xx)，则进行捕获
# 重试下载：遇到异常时，要进行判断，如果是服务器错误，则进行重试下载，重试次数为2
# 支持代理：设置用户代理，通过构造request请求，来支持user-agent代理下载
import urllib2

def download(url,user_agent="wxwp",num_retries=2):
	print "downloading :",url
	headers={"User-agent":user_agent}
	request=urllib2.Request(url,headers=headers)
	try:
		html=urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print "downloading error: ",e.reason
		html=None
		if num_retries>0:
			if hasattr(e,"code") and 500<=e.code<600 :
				download(url,user_agent,num_retries-1)
	return html

if __name__ == '__main__':
	pass

