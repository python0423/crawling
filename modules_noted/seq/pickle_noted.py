# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-20 19:19:16
# @Last Modified by:   admin
# @Last Modified time: 2018-03-20 19:51:56
# 这里探讨序列化操作
# 序列化：把数据保存为字节流的过程称为序列化；因为当需要网络传输或者储存python对象时，不能直接保存，需要转换为字节流
# 比如内存中的变量，一旦关闭程序，变量就会被回收；所以可以通过序列化的方式，把变量存放到本地文件中，这个过程就成为序列化
# 反之，就是反序列化
# python序列化后的对象不能被其他编程语言使用；如果要实现跨编程语言传递对象，json是更好的选择
# python的序列化使用可打印的ascll来表示，不是二进制方式；这样做的原因是可以用文本编辑器来阅读内容

# 尽量使用cPickle，因为它更快
import cPickle as pickle
def version(num):
	# 这个函数设置pickle使用哪种版本协议
	# 0 表示最早的ascll协议；1表示二进制协议；2表示最新的协议；如果没有指定，默认使用0
	pickle.HIGHEST_PROTOCOL=2

def dump_fuc(obj):
	# dumps 返回一个序列化后的字节流
	pik_dumps=pickle.dumps(obj)
	print "序列化后的字节流：",pik_dumps
	fw=open("pick.txt","w")
	# dump 返回一个序列化的对象，并提供文件对象参数，可以直接写入文件
	pik_dump=pickle.dump(obj,fw)
	if pik_dump:
		print "dump返回值：",pik_dump
	else:
		print "dump方法不返回值"
	return pik_dumps

def load_fuc(obj):
	# load实现反序列化，它可以自动确定打开的字节流是否为二进制
	fw=open("pick.txt","r")
	unpick=pickle.load(fw)
	if unpick:
		print "反序列化后的值：",unpick
	else:
		print "load不返回值"
	# loads方法将一个传入的序列化进行反向操作
	pick_dump=pickle.dumps(obj)
	print "反向序列后的字符串："
	print pickle.loads(pick_dump)


def error_fuc():
	# 这个函数总结模块中的异常
	# pickle.PickleError是通用基类
	pass



if __name__ == '__main__':
	li=["one","two","three","four",None,True]
	# dump_fuc(li)
	load_fuc(li)