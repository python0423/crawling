# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-05 11:59:50
# @Last Modified by:   admin
# @Last Modified time: 2018-03-05 12:13:12
# 方法二： 使用id遍历爬虫
# 网页url中一般包含页面别名和id，可以通过找到id的规律，来爬取相应的页面
import itertools
from download_fuc import download

def id_itertool():
	for page in itertools.count(1):
		url="http://example.webscraping.com/view/-%d" %page
		html=download(url)
		if html is None:
			break
		else:
			# 表示下载成功，然后进行抽取
			print "%d is ok " %page

def id_itertool_error():
	# 当id不连续的的时候会终止程序，可以捕捉间隔，当发生多次下载错误时才会停止
	max_errors=8
	# 当前错误次数
	num_errors=0
	for page in itertools.count(1):
		url="http://example.webscraping.com/view/-%d" %page
		html=download(url)
		if html==None:
			num_errors+=1
			if num_errors==max_errors:
				break
		else:
			pass 
			num_errors=0

if __name__ == '__main__':
	id_itertool_error()


