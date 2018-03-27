# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-27 10:48:46
# @Last Modified by:   admin
# @Last Modified time: 2018-03-27 11:20:56
# 这里记录string模块
import string

def string_attr():
	# 打印string中的常量
	for x in dir(string):
		if x.startswith("_"):
			continue
		v=getattr(string,x)
		if isinstance(v,basestring):
			print "%s --> %s" %(x,repr(v))

def string_fuc():
	# string中的函数
	# 转换为首字母大写
	exp="go spurs go, my team , you will play the playoff and win chapionship again"
	print string.capwords(exp)

	# 指定转换，使用translte可以将指定字符转换为想要的字符
	leet=string.maketrans("abcdefg","1234567")
	ch_leet=string.maketrans("休斯顿火箭队","圣安东尼马刺")
	team='我喜欢休斯顿火箭队'
	print exp
	print exp.translate(leet)
	print team
	print team.translate(ch_leet)  # 不支持中文替换

	# 模板转换,模板只能是字典
	values={"first":"休斯顿火箭","second":"圣安东尼奥马刺","third":"金州勇士"}
	t=string.Template("$first --> $second")
	print "teaplate",t.substitute(values)	


if __name__ == '__main__':
	# string_attr()
	string_fuc()