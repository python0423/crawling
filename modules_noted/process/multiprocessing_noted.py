# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-20 19:55:20
# @Last Modified by:   admin
# @Last Modified time: 2018-03-21 17:29:23
# 这里讲解多进程在python中的实现
# 多进程的实现在python中有两种方式，os.fork和mulprocessing模块
# 前者只支持类Unix系统，后者可以跨平台
# 这里只讲解mulprocessing模块

import multiprocessing
import time

# ===================================================================
# 文档研究
from multiprocessing import Pool
# pool提供了一种方式，并行打印
def f(x):
	return x*x
def main_f():
	p=Pool(5)
	print p.map(f,[1,2,3])

# 最简单实现多进程的方式是使用process类，并调用start方法
# 上面的例子已经实现，这里不做表述

# 这个模块支持两个进程之间的通信
from multiprocessing import Queue
def f_queue(q):
	q.put([42,None,"hello"])
def main_f_queue():
	q=Queue()
	p=multiprocessing.Process(target=f_queue,args=(q,))
	p.start()
	print q.get()
	p.join()

# 也支持管道模式，从管道的一段进入，另一端送出数据
# 不能同时从管道的一头同时进行数据的发送和修改
from multiprocessing import Pipe,Process
def f_pipe(conn):
	# 每个管道对象都有send和recv方法
	conn.send([42,None,"hello"])
	conn.close()
def main_f_pipe():
	p_in,p_out=Pipe()
	p=Process(target=f_pipe,args=(p_in,))
	p.start()
	print p_out.recv()
	p.join()

# 通过调用进程锁的方式，让同一时间只要一个进程在打印输出
from multiprocessing import Lock
def f_lock(l,i):
	# 调用锁
	l.acquire()
	print "hello,world",i 
	# 释放锁
	l.release()
def main_f_lock():
	#生成锁
	l=Lock()
	for num in xrange(1,10):
		Process(target=f_lock,args=(l,num)).start()

# 进程池pool：通过构造进程池，让多个进程可以同时执行
# 打印cpu核数
from multiprocessing import Pool
def pool_fuc_task(num):
	# 这是个执行函数，要放在进程池里
	return num*num
def pool_fuc():
	print "cpu 核心数：",multiprocessing.cpu_count()
	# 创建进程池的方式
	pool=Pool(processes=8)  # 指定核心数目，最好和硬件相同
	results=[]
	for x in xrange(1,8):
		result=pool.apply_async(pool_fuc_task,args=(x,))  # apply_async是表示多个进程同时进行，apply是指进程依次进行
		results.append(result)
	pool.close()
	pool.join()
	for result in results:
		print result.get()


#=========================================================
# 实例
def worker():
	# 这是原始进程
	print 'work'
	return 
def copy_process():
	# 最简单的方式就是直接复制一个进程，使用start打开进程
	job=[]
	for x in range(5):
		p=multiprocessing.Process(target=worker)
		job.append(p)
		print job
		p.start()

# 使用带参数的原始进程
def worker_num(num):
	# 这是带参数的处理函数
	print "worker-->>",num
	return 
def copy_process_num():
	# 可以在原始进程中传递参数，参数的传递必须经过pickle模块
	# 传递的参数必须是元祖
	jobs=[]
	for x in range(5):
		p=multiprocessing.Process(target=worker_num,args=(x,))
		p.start()


# 通过打印名字，pid来确定正在执行的进程
def my_service():
	# 进程一
	p=multiprocessing.current_process()
	# 可以打印pid，name等属性
	print p.name,"starting"
	print "进程号：",p.pid
	time.sleep(2)
	print p.name,"exiting"
def worker_name():
	# 进程二
	p=multiprocessing.current_process()
	print p.name,"starting"
	print "进程号：",p.pid
	time.sleep(2)
	print p.name,"exiting"
	
def main_start():
	# 当有不同的进程要切换时，通过打印进程名字来实现确定当前进程
	# 打印的顺序可能会不一致，取决于机器执行
	service=multiprocessing.Process(target=my_service,name="my_service")
	worker_1=multiprocessing.Process(target=worker_name,name="my_worker")
	mul_default=multiprocessing.Process(target=worker_name)  # 设置默认的值，如果未指定名字，则使用process号
	# 启动相应进程
	service.start()
	worker_1.start()


# 设置daemon值，来守护某个进程
# 守护进程的意思是会复制一个子进程，然后脱离父进程，称为脱壳
# 守护进程一定要在start开始之前
import sys
def daemon():
	# 这是被守护的进程函数
	p=multiprocessing.current_process()
	print "start : ",p.name,p.pid
	time.sleep(1)
	print "ending:",p.name,p.pid
	sys.stdout.flush()
def non_daemon():
	# 这是不被守护的进程
	p=multiprocessing.current_process()
	print "start : ",p.name,p.pid
	time.sleep(2)
	print "ending:",p.name,p.pid
	sys.stdout.flush()
def main_daemon():
	# 设置守护进程
	d=multiprocessing.Process(target=daemon,name="daemon")
	d.daemon=True
	n=multiprocessing.Process(target=non_daemon,name="non_daemon")
	n.daemon=False
	d.start()
	time.sleep(1)
	n.start()
	# 使用join方法等待进程结束并退出，这时会打印守护进程的信息
	d.join()
	n.join()

# 使用terminate()来杀死子进程
def term_child( ):
	# 子进程
	print "start "
	time.sleep(1)
	print "exit"
def main_term():
	# terminate主进程
	p=multiprocessing.Process(target=term_child)
	print "启动之前活着吗？ ",p.is_alive()
	p.start()
	print "启动了，活着吗？",p.is_alive()
	p.terminate()
	print "杀死子进程，活着吗?",p.is_alive()
	p.join()
	print "等待进程结束，还活着？",p.is_alive()
	# 如果没有杀死子进程，并且join的超时设置大于子进程的执行时间
	# 则返回true
	'''
	p.terminate()
	print "没有杀死子进程，现在活着吗?",p.is_alive()
	p.join(2)
	print "等待进程结束，还活着？",p.is_alive()
	'''
# 启用调试模式
import logging
def log_fuc():
	# 调试函数
	print "doing some work"
	sys.stdout.flush
def main_log():
	# 启用调试模式
	multiprocessing.log_to_stderr(logging.DEBUG)
	p=multiprocessing.Process(target=log_fuc)
	p.start()
	p.join()

# 进程间通信
https://pymotw.com/2/multiprocessing/communication.html

if __name__ == '__main__':
	# copy_process()
	# copy_process_num()
	# main_start()

	# main_f()
	# main_f_queue()
	# main_f_pipe()
	# main_f_lock()
	# pool_fuc()
	# main_daemon()
	# main_term()
	main_log()
