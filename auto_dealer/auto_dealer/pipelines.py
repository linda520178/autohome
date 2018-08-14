# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymysql.cursors
from auto_dealer.items import AutohomeItem
from scrapy.exceptions import DropItem
import scrapy

class AutoDealerPipeline(object):
	def __init__(self, dbparams):
		self.dbparams = dbparams

	@classmethod
	def from_crawler(cls, crawler):
		dbparams=dict(
			host=crawler.settings['MYSQL_HOST'],
			db=crawler.settings['MYSQL_DBNAME'],
			user=crawler.settings['MYSQL_USER'],
			passwd=crawler.settings['MYSQL_PASSWD'],
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor,
			use_unicode=False)
		
				
		return cls(
			dbparams=dbparams,
		)

	def open_spider(self,spider):
		self.connection = pymysql.connect(**self.dbparams)

	def process_item(self, item, spider):
		if hasattr(item,"saveto_mysql"):
			if callable(item.saveto_mysql):
				item.saveto_mysql(self.connection)
		return item

	def close_spider(self,spider):
		self.connection.close()