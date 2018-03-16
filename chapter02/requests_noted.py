# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-16 07:10:34
# @Last Modified by:   admin
# @Last Modified time: 2018-03-16 08:43:11
# 这个文档讲解requests模块

import requests

def request_method(url):
	# 返回的是一个服务器的响应对象
	r=requests.get(url)
	print r.url
	#打印出页面内容，相当于download函数
	# print r.text
	#打印文本内容，但是以非文本的方式(二进制方式)
	# print r.content
	# print type(r.content)

	# 打印服务器响应头，它会以python的字典形式返回
	# print r.headers
	# 访问某个字段,大小写无所谓
	print r.headers["status"]
	print r.headers["content-type"]

	# 打印使用的编码,这个值是可以修改的，如果被修改，每次访问r.text的都将采用此编码方式
	print r.encoding
	# r.encoding="utf-8"
	# print r.encoding

	# 检查返回状态码
	print r.status_code

	# 处理json数据，使用json方法，他是一个内置的解码器，如果没有json数据，则返回一个异常；
	# 但是不能凭借正确返回与否来判断请求是否成功，要通过检查返回状态码来判断
	print r.json()

	# 定制请求头部,但是头部设置不总是有效，它的优先级低于某些特定的信息源
	# 所有头部信息必须是字节流，字符串或者是unicode
	headers={"user-agent":"my-app/0.1.1"}
	r_header=requests.get(url,headers=headers)

	# 使用post构造一个表单请求，添加用户名和密码
	payload={"key1":"value1","key2":"value2"}
	r_post=requests.post("http://httpbin.org/post",data=payload)
	# 还可以传入一个元祖列表，当表单使用的是同一个键时，这种方式非常有效
	payload=({"key1":"value1"},{"key1","value2"})

	# 可以直接添加json数据进行请求
	payload={"some":"data"}
	r_json=requests.post(url,json=payload)

	# 抛出异常
	# 如果请求的状态码是4xx或者非2xx，可以使用raise_for_status来抛出异常
	# bad_r=requests.get("http://httpbin.org/status/404")
	# print bad_r.raise_for_status()

def request_cookie(url):
	# 这个函数用来介绍cookie
	r=requests.get(url)
	print r.cookies["logged_in"]
	# 如果想要发送cookie到服务器上，在reques请求中使用cookies参数
	r_cookie=requests.get(url,cookies={"logged_in":"username"})
	print r_cookie.text


def request_redirction(url):
	# 这个函数用来介绍重定向
	# 默认情况下会自动处理重定向，使用history来记录重定向的历史
	r=requests.get(url)
	print r.url
	print r.history
	# 可以禁用重定向，在allow_redirects中禁用
	r_bin=requests.get(url,allow_redirects=False)
	print r_bin.history

	#超时响应：在构造请求对象中使用timeout参数设置等待响应的时间
	# 这个参数基本是必须的
	r_time=requests.get(url,timeout=0.1)


# 一些异常错误
# 如果遇到dns查询失败，拒绝链接等，request会抛出ConnectionError 异常
# 如果http请求不成功，则返回一个 Response.raise_for_status() 会抛出一个 HTTPError 异常。
# 若请求超时，则抛出一个 Timeout 异常。
# 若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
# 所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。


# 主函数
if __name__ == '__main__':
	# request_method("https://github.com/timeline.json")
	# request_cookie("https://github.com/timeline.json")
	# request_redirction("http://zhibo8.cc")