# -*- coding: utf-8 -*-

import scrapy
from auto_dealer.items import AutohomeItem
from scrapy.selector import Selector
from scrapy.http import Request
import re
from redis import Redis
from scrapy_redis.spiders import RedisSpider

class Autohome_dealerspiderSpider(RedisSpider):
	name= 'autohome_dealer'
	#start_urls = ['https://dealer.autohome.com.cn/beijing']
	redis_key = 'Autohome:start_urls'

	# def start_requests(self):
	# 	res = []
	# 	for i in range(1, 45):
	# 		url = 'https://dealer.autohome.com.cn/beijing/0/0/0/0/%s/1/0/0.html' % i
	# 		res.append(url)
	# 	return res

	def parse(self,response):
		for i in range(1,45):
			url = 'https://dealer.autohome.com.cn/beijing/0/0/0/0/%s/1/0/0.html'%i
			yield scrapy.Request(url=url,callback=self.parse_item)

	def parse_item(self, response):
		item = AutohomeItem()
		name = response.xpath("//li[@class='tit-row']/a[@class='link']/span/text()")[1].extract()
		item['name'] = name
		brand = response.xpath("//ul[@class='info-wrap']/li[2]/span/em/text()")[1].extract()
		item['brand'] = brand
		phone = response.xpath("//ul[@class='info-wrap']/li[3]/span[2]/text()")[1].extract()
		item['phone'] = phone
		address = response.xpath("//ul[@class='info-wrap']/li[4]/span[2]/text()")[1].extract()
		item['address'] = address
		Promotion = response.xpath("//ul[@class='info-wrap']/li[5]/a/text()")[1].extract()
		item['Promotion'] = Promotion

		yield item
		
		
		
		
		
 		
