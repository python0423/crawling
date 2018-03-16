# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-15 16:24:20
# @Last Modified by:   admin
# @Last Modified time: 2018-03-15 22:38:46
a=[1,2,3,4]
print type(a)
for x in a:
	if x<=3:
		a.remove(x)
print a