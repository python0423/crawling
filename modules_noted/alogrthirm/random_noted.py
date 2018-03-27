# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-27 10:02:48
# @Last Modified by:   admin
# @Last Modified time: 2018-03-27 10:48:23
# 这里介绍伪随机数模块
import random
import string
def random_fuc():
	# random 产生一个0-1之间的伪随机数
	# 它会在每次被调用的时候产生一个不同的值
	for x in range(5):
		print "%.5f" %random.random()

	# 可以指定random的种子，以使用固定的公式，否则使用系统随机源或者当前时间
	random.seed(1)
	for b in xrange(1,10):
		print "%.5f" %random.random()

	# uniform通过给定的范围，生成一个特殊的数值
	for a in range(5):
		print "%0.5f" %random.uniform(1,100)

	# randint 随机生成整型数据
	for x in xrange(1,5):
		print "%d" %random.randint(-10,19)

	# randrange产生一个随机数，但是提供了步长
	for x in xrange(1,5):
		print "%d" %random.randrange(1,100,3)

	# choice提供了一种方式，可以随机产生序列中的某个元素，序列不一定是数字，也可以是任意对象
	# 下面的例子演示了硬币抛一万次，产生正反面的概率
	outcomes={"head":0,"tail":0}
	sides=outcomes.keys()
	for x in range(10000):
		outcomes[random.choice(sides)]+=1
	print outcomes["head"]
	print outcomes["tail"]

	# sample可以从一个总体中随机筛选样本，下面通过读取一个单词列表，产生3个随机样本
	words=["one","two","three","four","five","six","seven","eight"]
	for x in xrange(1,5):
		print "%s" %random.sample(words,3)

	# random提供了一个random类，以上的方法都可以在random类中使用，不同的对象之间不会有影响
	r1=random.Random()
	r2=random.Random()
	for x in xrange(1,10):
		print "%f,%f" %(r1.random(),r2.random())

	# 设置二者初始状态为相同,产生的数值就是一致的
	r2.setstate(r1.getstate())
	for x in range(1,5):
		print r1.random(),r2.random()
	# 使用jumphead来跳出相同状态
	r2.jumpahead(102)
	for x in range(5):
		print r1.random(),r2.random()

def random_string():
	# python 如何生成8位随机字符串
	seed="1234567890abcdefghigklmnopkrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ"
	sq=[]
	for x in range(10):
		sq.append(random.choice(seed))
	rst="".join(sq)
	print rst

	# 另一种方法
	sat="".join(random.sample(string.ascii_letters+string.digits,8))
	print sat

if __name__ == '__main__':
	# random_fuc()
	random_string()