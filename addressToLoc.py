# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import time

#地址轉經緯度, parse 回傳的 json data 
mapUrl = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=zh-tw&address='
#f = open('yamaha_location_copy.txt','r')
#f2 = open('yamaha_location2.txt','a')
#f = open('kimco_location_copy.txt','r')
#f2 = open('kimco_location2.txt','a')
f = open('sym_location_copy.txt','r')
f2 = open('sym_location2.txt','a')
for lines in f.readlines():
	name = lines.split(';')[0]
	address = lines.split(';')[1]
	phone = lines.split(';')[2]
	print address
	response = urllib2.urlopen(mapUrl + urllib2.quote(address))
	responseJSON = response.read()
	jsonObj = json.loads(responseJSON)
	loc = jsonObj['results'][0]['geometry']['location']
	location = str(loc['lat']) + ';' + str(loc['lng'])
	shopString = name + ';' + address + ';' + location + ';' + phone
	f2.writelines(shopString)
	time.sleep(1)