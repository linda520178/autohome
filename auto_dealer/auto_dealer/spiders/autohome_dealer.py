# -*- coding: utf-8 -*-

import scrapy
import pymysql
from scrapy.http import Request
from auto_dealer.items import AutohomeItem

class Autohome_dealerspiderSpider(scrapy.Spider):
	name= 'autohome_dealer'
	start_urls = ['https://dealer.autohome.com.cn/beijing']

	def parse(self,response):

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
		
		
		
		
		
 		
