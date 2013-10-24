# -*- coding: utf-8 -*-
import urllib2
import urllib
from lxml import etree

url = 'http://tw.sym-global.com/servicemap/'
response = urllib2.urlopen(url)
html = response.read()

page = etree.HTML(html)
areas = page.xpath(u"//area")
hrefList = []
shopList = []
i =0
for area in areas:
	
	hrefList.append(area.attrib['href'])

for link in hrefList:
	for p in range(20):
		areaUrl = url + link[2:] + '&p=' + str(p+1)
		print areaUrl
		response = urllib2.urlopen(areaUrl)
		html = response.read()
		page = etree.HTML(html) 
		name = page.xpath(u"//td[@style='text-align:left;padding:5px 0px;width:270px;border-left:1pt solid #CCCCCC;border-bottom:1pt solid #CCCCCC;']")
		
		if len(name) == 0:
			break
		for n in name:
			title = n.xpath('./a/span/text()')[0].encode('utf8').strip()
			address = n.xpath('./div/nobr/a/text()')[0].encode('utf8').strip()
			phone = n.xpath('./div/br/following-sibling::text()')[0][5:].encode('utf8').strip()

			shopString = title + ';' + address + ';' + phone + '\n'
			shopList.append(shopString)
	# areaUrl = url + link[2:] + '&p='
	# print areaUrl
	# response = urllib2.urlopen(areaUrl)
	# html = response.read()
	# page = etree.HTML(html) 

	# pager = page.xpath(u"//td[@style='width:40%;text-align:left;height:17px;']/div[@style='position:relative;z-index:20;']")
	# if len(pager) != 0:
	# 	print pager[0].xpath("./div/a[@title=" + u'最後一頁' + "]/text()")
			
	# name = page.xpath(u"//td[@style='text-align:left;padding:5px 0px;width:270px;border-left:1pt solid #CCCCCC;border-bottom:1pt solid #CCCCCC;']")
	
	# for n in name:
	# 	title = n.xpath('./a/span/text()')[0].encode('utf8').strip()
	# 	address = n.xpath('./div/nobr/a/text()')[0].encode('utf8').strip()
	# 	phone = n.xpath('./div/br/following-sibling::text()')[0][5:].encode('utf8').strip()

	# 	shopString = title + ';' + address + ';' + phone + '\n'
	# 	shopList.append(shopString)

f = open('sym_location.txt','w')
f.writelines(shopList)
