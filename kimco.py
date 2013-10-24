# -*- coding: utf-8 -*-
from ghost import Ghost
from lxml import etree
ghost = Ghost()
baseUrl = 'http://www.kymco.com.tw/www2010/location/location_views.asp?r='
urls = ['Taipei_City','New_Taipei_City','Keelung_City','Taoyuan_County','Hsinchu_County',
        'Miaoli_County','Taichung_City','Changhua_County','Yunlin_County','Chiayi_County',
        'Tainan_City','Kaohsiung_City','Pingtung_County','Taitung_County','Hualien_County',
        'Nantou_County','Yilan_County_City','Penghu_County','Kinmen_County_City']

shopList = []
for url in urls:
	url = baseUrl + url
	print url
	extra_resources = ghost.open(url)
	html = ghost.content.encode('utf-8');
	#print type(html.encode('utf8'))
	page = etree.HTML(html)
	locationTable = page.xpath(u"//table[@id='innerLocation_table']")[0]
	shop = locationTable.xpath('./tbody/tr')
	for s in shop:
		name = s.xpath('./td[1]/text()')[0].encode('utf8').strip()
		phone = s.xpath('./td[2]/text()')[0].encode('utf8').strip()
		address = s.xpath('./td[4]/text()')[0].encode('utf8').strip()
		shopString = name + ';' + address + ';' + phone + '\n'
		shopList.append(shopString)

f = open('kimco_location.txt','w')
f.writelines(shopList)