# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-21 17:36:20
# @Last Modified by:   admin
# @Last Modified time: 2018-03-22 10:53:45
# 这里研究socket模块

import socket 
import urlparse
def hostname():
	# 这个函数获取主机名字等属性
	print "主机名字：",socket.gethostname()
	# 通过域名解析为ip
	domain=["www.baidu.com","163.com"]
	for addr in domain:
		print "%15s-->%s" %(addr,socket.gethostbyname(addr))
	#gethostbyname_ex返回一个规范的地址，别名，服务器名字
	for addr in domain:
		hostname,alias,ip=socket.gethostbyname_ex(addr)
		print "%10s-->%s" %("主机名",hostname)
		print "%10s-->%s" %("别名",alias)
		print "%10s-->%s" %("IP地址",ip)
	# 完全限定域名：主机名+域名
	# print "完全限定域名：",socket.getfqdn("163.com")
	# gethostbyaddr 执行反向查找，返回元祖----相当于执行PTR记录查找
	try:
		hostname,alias,ip=socket.gethostbyaddr("223.5.5.5")
		print "%10s-->%s" %("主机名",hostname)
		print "%10s-->%s" %("别名",alias)
		print "%10s-->%s" %("IP地址",ip)
	except socket.herror as e:
		print "下载错误，地址没有PTR记录"
	# 查看某个协议所使用的端口
	address=["http://www.baidu.com","ftp://www.123.com","smtp://132.com","icmp"]
	parsed_url=urlparse.urlparse(address[2])
	port=socket.getservbyname(parsed_url.scheme)
	print "%s --->%s" %(parsed_url.scheme,port)
	# 给定端口，查看属于哪个协议
	port=[80,113,21,20,22,443,2049]
	for num in port:
		print "%d --->%s" %(num,socket.getservbyport(num))

# 查看一个连接中的详细信息
def connection():
	# 这个函数处理一个连接中的详细信息
	# protocols=get_connect("IPPROTO_")
	# for name in ["tcp","icmp","udp"]:
	# 	proto_num=socket.getprotobyname(name)  # 返回的是协议号
	# 	# print proto_num
	# 	const_name=protocols[proto_num]
	# 	print const_name
	famlies=get_connect("AF_")
	types=get_connect("SOCK_")
	protocols=get_connect("IPPROTO_")
	# getaddrinfo 返回一个连接的详细信息
	for response in socket.getaddrinfo("www.python.org","http"):
		# print response
		family,socketype,proto,canoname,socketaddr=response
		print "ip协议类型(v4 or v6)：",famlies[family]
		print "socket类型：",types[socketype]
		print "传输层协议(tcp or udp)",protocols[proto]
		print "ip地址：",socketaddr

def get_connect(prefix):
	# 这个函数定义一个字典推导式，返回加前缀的协议名
	ip_dict={}
	for n in dir(socket):
		if n.startswith(prefix):
			ip_dict[getattr(socket,n)]=n
			# print getattr(socket,n) # 返回的是协议的编号
	return ip_dict
	# 使用字典推导式可以有另一种写法
	# return dict((getattr(socket,n),n) for n in dir(socket) if n.startswith(prefix)




if __name__ == '__main__':
	# hostname()
	# connection()
