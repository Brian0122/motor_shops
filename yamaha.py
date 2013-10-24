# -*- coding: utf-8 -*-
from ghost import Ghost
from lxml import etree
import urllib2
import json
import time
ghost = Ghost()

url = 'http://www.yamaha-motor.com.tw/dealer/dealer.aspx'
mapUrl = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=zh-tw&address='
ghost.open(url)

html = ghost.content.encode('utf-8');
#print type(html.encode('utf8'))
page = etree.HTML(html)
cityOption = page.xpath(u"//select[@id='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_selCity']")[0]
cities = cityOption.xpath("./option/@value")
shopList = []
f2 = open('yamaha_location2.txt','a')
for city in cities:
	if city != '':
		print city
		result, resources = ghost.fill("#aspnetForm", {
		    "ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$selCity": city,
		    "sss": "1"
		})
		ghost.fire_on("#aspnetForm", "submit", expect_loading=True)
		html = ghost.content.encode('utf-8');
		page = etree.HTML(html)
		dealer = page.xpath(u"//table[@id='dealerTD1']")[0]
		for shop in dealer.xpath('./tbody/tr'):
			name = shop.xpath('./td[1]/a/text()')[0].encode('utf8').strip()
			address = shop.xpath('./td[2]/text()')[0].encode('utf8').strip()
			response = urllib2.urlopen(mapUrl + address)
			responseJSON = response.read()
			jsonObj = json.loads(responseJSON)
			loc = jsonObj['results'][0]['geometry']['location']
			location = str(loc['lat']) + ';' + str(loc['lng'])
			print location
			phone = shop.xpath('./td[3]/text()')[0].encode('utf8').strip()
			shopString = name + ';' + address + ';' + location + ';' + phone + '\n'
			shopList.append(shopString)
			f2.writelines(shopString)
			time.sleep(1)

f = open('yamaha_location.txt','w')
f.writelines(shopList)