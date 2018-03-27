# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-22 10:54:28
# @Last Modified by:   admin
# @Last Modified time: 2018-03-22 13:20:18
# 这个函数继续socket模块的内容，编写服务器代码
import socket
def server_fuc():
	# 这个函数实现tcp链接
	# 服务器构成分为四步
	# 第一步，构建socket,链接服务器地址和端口
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# server_addr=("localhost",10000)
	# server_addr=("192.168.100.101","10000")
	server_addr=("",10000)  # 使用空字符串来监听所有地址
	sock.bind(server_addr)
	print "服务器地址是%s" %server_addr[0]
	print "端口号为%d" %server_addr[1]
	# 第二步，启用监听模式，等待数据传入
	sock.listen(1)
	while True:
		print "启用监听,等待链接"
		connection,client_addr=sock.accept()
		try:
			# print "客户端地址为：%s" %client_addr
			# 第三步：接受数据，并发送响应给客户端
			while True:
				data=connection.recv(64)
				if data:
					print "已接受到数据：%s" %data
					connection.sendall("hello, Mr.client")
				else:
					print "no more data from",client_addr
					break
			
		finally:
			# 第四步，关闭链接
			connection.close()

def udp_fuc():
	#这个函数实现udp链接
	#由于udp不需要像tcp一样保证可靠性，所以不需要监听
	#基于udp的服务器需要两步即可
	#第一步：构建socket，使用bind关联服务器
	sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_addr=("localhost",12000)
	sock.bind(server_addr)
	while True:
		# 直接等待接受即可，接收后立即返回
		print "等待接受消息"
		data,cli_address=sock.recvfrom(4096)
		if data:
			print "已接受到来自",cli_address,"的消息"
			print data
			print "发送消息给客户端"
			sock.sendto("ok,you are client",cli_address)




if __name__ == '__main__':
	# server_fuc()
	udp_fuc()

