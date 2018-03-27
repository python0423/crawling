# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-20 18:54:53
# @Last Modified by:   admin
# @Last Modified time: 2018-03-20 19:00:58
from link_crawal import scrapy_link
import csv
import re
import lxml
class Scrapyback:
	"""docstring for Scrapyback"""
	def __init__(self):
		self.writer=csv.writer(open("data.csv","w"))
		self.field=('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
		self.writer.writerow(self.field)
	def __call__(self,url,html):
		# 保证这个类可调用
		if re.search("/places",url):
			tree=lxml.html.fromstring(html)
			row = []
			for field in self.fields:
			    row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
			self.writer.writerow(row)

		

if __name__ == '__main__':
	scrapy_link('http://example.webscraping.com/', '/(index|view)', scrape_callback=ScrapeCallback())