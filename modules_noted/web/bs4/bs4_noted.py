# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-13 06:58:38
# @Last Modified by:   admin
# @Last Modified time: 2018-03-23 16:23:00
from bs4 import BeautifulSoup
import urllib2
from alice_html import alice_docu

def prettify_print(html):
	# beautfulsoup类传入对象可以是字符串，也可以是一个file handle
	# file handle 实例：soup=BeautfulSoup(open("index.html"),"lxml")
	# 第二个参数指定解析器，默认是用python标准库，推荐使用lxml，不过要安装C库
	# soup是一个文档对象，所有的html实例都会被转化为unicode编码，然后用指定的解析器来解析
	soup=BeautifulSoup(html,"lxml")
	# 返回网页的结构性文档
	return soup.prettify()

# 说明
# bs会将一个复杂的文档转换为一个树形结构，包含四部分：标签，导航字符串，beautfulsoup(表示一个文档的全部内容),注释
	''' 标签：tag----所有标签都有name属性，如果name属性被改变，则会影响当前所有通过bs生成的文档
		attr是标签的属性，每个标签可能有很多属性，操作方式类似于字典
		tag["class"]表示打印clas属性的值；或者直接取属性：tag.attrs会打印所有属性
		属性可以被添加，删除，修改，操作方式与字典一致
	'''
def title_attr(html):
	soup=BeautifulSoup(html,"lxml")
	# title的属性
	print "标题：",soup.title.name 
	print "标题名：",soup.title.string
	print "标题的父标签",soup.title.parent.name
	print "打印标题属性",soup.title.attrs 
	# "添加标题属性"
	soup.title["class"]="title title1"
	print soup.title.attrs
	print soup.title["class"]
	# "删除标题属性"
	del soup.title["class"]
	print soup.title.attrs

def p_attr(html):
	soup=BeautifulSoup(html,"lxml")
	# p标签的属性
	print "段落:",soup.p
	# 每个标签可能定义了多种属性，多值属性的返回值是列表
	print "段落css：",soup.p["class"]
	# 打印文档中所有文字内容
	print soup.get_text()

# 字符串属性：bs使用NavigableString类来封装字符串，他和unicode字符串相同
def tag_string(html):
	soup=BeautifulSoup(html,"lxml")
	print "标签字符串: ",soup.p.string
	print "检查字符串类型：",type(soup.p.string)
	# 字符串支持被替换，使用replace_with方法
	soup.p.string.replace_with("世界大同")
	print soup.p
	# 字符串不支持.string,.content,.find方法
	# 如果想在bs之外的地方使用NavigableString，需要使用unicode方法转换，否则会造成内存浪费
	unicode_str=unicode(soup.p.string)
	print unicode_str,type(unicode_str)

def beautfulsoup_object(html):
	soup=BeautifulSoup(html,"lxml")
	# 这里研究beautfulsoup部分，它表示一个文档的全部内容
	# 它没有name和attribute，但有一个特殊的name,返回document
	print soup.name


def a_attr(html):
	soup=BeautifulSoup(html,"lxml")
	# a标签的属性
	print "链接：",soup.a
	print "查找所有链接：",soup.find_all("a")
	print "查找指定链接：",soup.find(id="link3")
	# 打印所有a标签的链接
	for link in soup.find_all("a"):
		print link.get("href")

def comment_fuc(makeup):
	soup=BeautifulSoup(makeup,"lxml")
	# 这里显示的是文档的注释部分的处理
	print soup.b.string
	print "类型是comment：",type(soup.b.string)
	comment_str=soup.b.string
	print comment_str
	# 当文档中有注释时，注释会以特殊的格式输出
	print soup.b.prettify()

def docu_tree(html):
	soup=BeautifulSoup(html,"lxml")
	# 一个tag中可能包含多个tag或者字符串，这里讨论如何在一个tag中找到其他tag或者字符串，这称为遍历文档树
	# 字符串节点不支持此属性，因为字符串没有子节点
	# 第一种方式：tag.name,使用标签名直接寻找对应的标签,这种方式的缺点在于只能获取文档的第一个匹配项
	print soup.head 
	print soup.title
	# 如果想要获取所有的匹配的标签内容，使用find_all方法
	print soup.find_all("a")  # 他会匹配所有的a标签


	# 使用content可以将子节点以列表方式输出,只输出第一个匹配项标签中的所有子节点
	print soup.p.contents
	print soup.p.contents[1]
	# 如果tag只有一个子节点，可以直接用string输出字符串；如果包含多个，string会返回none
	print "只有一个子节点：",soup.head.string
	# 如果tag包含多个子节点，可以用strings来循环获取字符串
	for str in soup.p.strings:
		print "循环：",str
	# 输出的内容包含了多个空行，使用 .stripped_strings来去除
	# 全部是空格的行会被忽略掉,段首和段末的空白会被删除
	for str in soup.p.stripped_strings:
		print "去除空行：",str
	# 通过使用children生成器，可以对子节点进行循环迭代
	for child in soup.p.children:
		print child
	# 使用descendants可以对所有的子孙节点进行递归循环；子孙节点：<head><title>hello</title></head>
	# title是head的子节点，hello字符串是head的孙节点
	for child_son in soup.p.descendants:
		print child_son
	# soup对象只有一个直接子节点，就是html，却有很多孙节点
	# for child_son in soup.descendants:
	# 	print child_son


	# 父节点,使用parent来获取父节点
	title_tag=soup.title
	print "打印父节点：", title_tag.parent
	print "打印字符串的父节点：(就是标签)",title_tag.string.parent
	# 文档顶层的父节点就是beautfulsoup对象
	html_tag=soup.html 
	print "顶层父节点:",type(html_tag.parent)
	# beautfulsoup的父节点是空
	# .parents 来递归所有父节点，直到返回none
	print "递归父节点"
	for parent in soup.a.parents:

		if parent==None:
			print parent
		else:
			print parent.name

	# 兄弟节点 在同一层下的相邻节点是兄弟节点
	bro="<a href='#'><b>hello</b><c>world</c></a>"
	soup_bro=BeautifulSoup(bro,"lxml")
	# 查询兄弟节点
	print soup_bro.b.next_sibling
	print soup_bro.c.previous_sibling
	# hello和world不是兄弟节点，因为他们的父节点不同
	# 使用next_siblings和previous_siblings可以迭代兄弟节点，实际情况中兄弟节点常常是换行，顿号等

def search_tree_find_all(html):
	# 搜索文档树,这里着重介绍find和find_all方法，通过在find和find_all中传入不同类型的参数
	# 过滤器：要查找的内容，可以是以下几种类型
	# 第一种：字符串；直接使用字符串进行匹配
	soup=BeautifulSoup(html,"lxml")
	print soup.find_all("title")
	# 第二种：正则；下面的例子表示以b开头的标签，body和b都会被找到,bs会以re.match来匹配
	# find_all可以传入正则表达式
	import re
	for tag in soup.find_all(re.compile("^b")):
		print tag.name
	# 第三种：列表；下面的例子传入一个包含a,b的列表，任何匹配列表中任意一项的标签都会被找到
	for tag in soup.find_all(["a","b"]):
		print tag
	# 第四种：true；它会匹配所有标签，除了字符串
	for tag in soup.find_all(True):
		print tag.name
	# 第五种：方法；定义一个方法，方法只能接受一个元素参数，如果这个方法返回真，则表示元素被找到，否则返回false
	def has_class_no_id(tag):
		return tag.has_attr("class") and not tag.has_attr("id")
	print "输出方法匹配项"
	print soup.find_all(has_class_no_id)
	# find_all方法的具体参数是find_all(name,attr,recurive,text,**kwargs)
	# name 是标签名，字符串会被自动忽略
	# kwargs，如果传入的不是标签，则会把该参数作为标签的属性来搜索
	print soup.find_all(id="link2")
		# 如果传入的是href，则会搜索每个标签的href属性
	print soup.find_all(href=re.compile("elsie"))
		# 传入的属性类型可以是列表，字符串，正则，true
		# 下面演示了传入true时，所有有id属性的标签都会被检索出来
	print soup.find_all(id=True)
		# 使用多个属性一起搜索，可以过滤多个属性
	print soup.find_all(id="link1",href=re.compile("elsie"))
	# attr 可以定义个字典参数，用以添加无法过滤到的属性，attr={"data":"value"}

	# 按照css来搜索
	# 因为class在python中是关键字，所以从4.1.1开始，使用class_来获取css
	print soup.find_all("a",class_="sister")
	# class_同样可以接受不同类型的过滤器，包括字符串，正则，列表

	# text文档参数
	# text显示标签中的字符串，同样可以接受过滤器(字符串，正则，列表，ture，方法)
	print soup.find_all(text="Elsie")
	print soup.find_all(text=["Tillie","Elsie"])
	# 可以和其他过滤器一同使用
	print soup.find_all("a",text="Elsie")

	#limit 限制搜索的数量
	# 当文档结构很大时，使用limit来限制搜索到的数量
	print soup.find_all("a",limit=2)

	# recursive，默认find_all会检索所有子孙节点，如果想要只检索直接子节点，设置为false
	markup='''
	<html>
	<head>
	<title></title>
	</head>
	
	<body>
	<p>
	<span>hello</span>
	<span>world</span>
	</p>
	</body>
	</html>
	'''
	soup_test=BeautifulSoup(markup,"lxml")
	print soup_test.html.find_all("title",recursive=False)

	# 简写的方式，bs对象=bs.find_all(),因为find_all()几乎是最常用的方法
	#下面的两行代码等价
	print soup("html")
	soup.find_all("html")

	print soup(text="Elsie")
	soup.find_all(text="Elsie")


def search_tree_find(html):
	# 搜索文档树
	# 这里介绍find方法以及其他方法
	# find方法相当于find_all(limit=1),不过find返回的是字符串，如果没有找到，则返回none
	# 可以简写标签，原理就是多次调用find，下面两行代码等价
	soup=BeautifulSoup(html,"lxml")
	print soup.head.title
	print soup.find("head").find("title")

	#find和find_all方法用来搜索当前节点的所有子节点和子孙节点
	#find_parent和find_parents用来搜索当前节点的父辈节点
	a_string=soup.find(text="Lacie")
	print a_string
	print a_string.find_parent("a")
	print a_string.find_parent("p")


	# 后面还有方法，但估计用不到，用到的时候再说


def css_select(html):
	soup=BeautifulSoup(html,"lxml")
	# bs支持大部分的css选择器，使用select方法传入字符串参数
	# css选择器返回的是列表，如果有多个元素匹配，则返回包含这些元素的列表
	print soup.select("title")
	# 表示打印p下面的story标签内容
	print soup.select("p story")
	# 逐层查找
	# 打印出所有body下的连接
	print soup.select("body a")
	# 直接子节点
	print soup.select("head > title")
	print soup.select("p > a")
	print soup.select("p > #link1")
	# 找到兄弟节点
	print "兄弟节点"
	# 它表示和link1相邻的，并且class=sister的标签，不会匹配所有
	print soup.select("#link1 + .sister")
	# 通过css类名查找
	print soup.select("#link2")
	# 通过cssid查找
	print soup.select(".sister")
	# 通过某个属性来查找
	print soup.select("a[href]='baidu.com'")
	# 搜索表格  不要找表格内行里面的连接，直接从表格中找连接
	print "表格"
	table=soup.select("div table a[href='#']")
	print table


def adapt_tree():
	soup=BeautifulSoup("<html><b class='index'>hello,world</b></html>","lxml")
	# bs最强大的地方是文档树的搜索，同时可以修改文档树的内容
	# 这里讨论对文档树的修改

	# 重命名一个标签，添加或修改属性的值
	tag=soup.b 
	tag.name="blockquote"
	tag["class"]="nav1"
	tag["id"]=1
	print tag
	del tag["class"] 
	del tag["id"]
	# 用string来替换掉所有文本内容；如果当前元素由子元素，使用string会替换掉标签内的所有元素，包括子元素
	# 所以这个方法慎用
	tag.string="你好，世界"
	print tag

	# 使用append方法向tag中添加内容，就像列表中的append一样
	tag.append(",中国，你好")
	print tag

	# 使用new_string方法，可以添加一段注释,利用这个特性，可以对整个页面进行注释
	# 这是4.2.1中新增 的方法
	from bs4 import Comment
	new_comment=soup.new_string("这是一段注释",Comment)
	tag.append(new_comment)
	print tag

	# 使用new_tag方法，创建一个新标签;只有第一个参数是必须的，表示标签名；
	# 相当于是一个工厂函数
	soup_b=BeautifulSoup("<b></b>","lxml")
	origin_tag=soup_b.b
	new_tag=soup_b.new_tag("a",href="baidu.com")
	origin_tag.append(new_tag)
	print origin_tag
	# 添加字符串
	new_tag.string="link_text"
	print origin_tag

	# 压缩输出：如果不考虑输出的格式，只在乎结果，可以使用str()或者unicode压缩输出
	# str返回的是utf8字符串
	print str(soup)

	# 获取文本内容
	# 使用Get_text方法，可以获得当前节点的所有文本内容，包含子孙节点
	print soup.get_text()
	# 可以指定分隔符,strip=True去除两边的空白
	print soup.get_text("/",strip=True)


	# 不同的解析器很可能会产生不同的运行结果，在代码中一定要注明使用了哪种解析器
	# html和xml都有自己的编码方式，但是使用了beautfulsoup的编码，文档会统一被转换为unicode
	print "打印出bs识别为哪一种编码: ",soup.original_encoding
	# 在创建bs对象时，可以通过设置from_encoding参数来预先设置编码方式，从而加快解析速度
	soup=BeautifulSoup(html,"lxml",from_encoding="utf-8")
	# 经过bs处理后，所有文档都会被设置为utf-8,如果想采用其他编码，请在prettify中设置
	print soup.prettify("utf-8")


def extra_fuc(html):
	# 一些额外的功能
	# 编码自动检测，可以在bs之外的地方使用
	# 如果不知道某段字符的编码，可以使用这个方式
	from bs4 import UnicodeDammit
	dammit=UnicodeDammit("Sacr\xc3\xa9 bleu!")
	print dammit.unicode_markup
	print dammit.original_encoding

	# 解析部分文档，如果仅仅需要解析链接，就不需要解析所有文档，从而节省内存，但并不会节省多少时间
	# 使用soupstrainer类可以只解析部分文档
	from bs4 import SoupStrainer
	only_tag_a=SoupStrainer("a")
	only_id=SoupStrainer(id="link2")
	soup=BeautifulSoup(html,"lxml",parse_only=only_tag_a)
	print soup.prettify()
	soup_id=BeautifulSoup(html,"lxml",parse_only=only_id)
	print soup_id.prettify()

	# 默认bs会解析为html，如果需要，可以设置为xml
	soup=BeautifulSoup(html,"xml")
	# 通常解析器会将文档中所有大小写全部转换为小写，因为html对大小写敏感
	# 如果需要大小写，请转换为xml
	# 安装cchardet会让文档的编码的解析速度会更快
	






if __name__ == '__main__':
	# print prettify_print(alice_docu())
	# title_attr(alice_docu())
	# p_attr(alice_docu())
	# a_attr(alice_docu())
	# tag_string(alice_docu())
	# beautfulsoup_object(alice_docu())
	# comment_fuc("<b><!--Hey, buddy. Want to buy a used parser?--></b>")
	# docu_tree(alice_docu())
	# search_tree_find_all(alice_docu())
	# search_tree_find(alice_docu())
	# css_select(alice_docu())
	# adapt_tree()
	# extra_fuc(alice_docu())