# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-22 11:05:21
# @Last Modified by:   admin
# @Last Modified time: 2018-03-22 13:19:27
# 这个页面编写基于socket的客户端程序
import socket
import time
def client_fuc():
	# 这个函数基于tcp协议传输
	# 客户端的构建分为三步
	# 第一步：创建socket,链接服务器
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_addr=("192.168.100.101",30000)
	# server_addr=("localhost",10000)
	sock.connect(server_addr)
	print u"链接服务器%s" %server_addr[0]
	# 第二步：发送数据到服务器，并接受来自服务器的响应
	try:
		msg="say hello!!Mr.server"
		n=0
		while n<3:
			time.sleep(1)
			print u"开始发送数据"
			sock.sendall(msg)
			n+=1
			data=sock.recv(64)
			print u"已接收到数据"
			print data
	# 第三步：关闭链接
	finally:
		print u"关闭链接"
		sock.close()
		
def udp_fuc():
	# 这个程序基于udp传输
	sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_addr=("localhost",12000)
	msg="hello,this is a udp message"
	try:
		print "开始发送数据"
		sock.sendto(msg,server_addr)
		print "开始接受数据"
		data,server=sock.recvfrom(4096)
		print "接受到数据%s" %data
	finally:
		print "关闭连接"
		sock.close()



if __name__ == '__main__':
	# client_fuc()
	udp_fuc()