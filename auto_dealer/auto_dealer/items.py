# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoDealerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AutohomeItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    Promotion = scrapy.Field()

    def saveto_mysql(self,db):
        name = self.get('name', '')
        brand = self.get('brand', '')
        phone = self.get('phone', '') 
        address = self.get('address', '')
        Promotion = self.get('Promotion', '')
        try:
            with db.cursor() as cursor:
                sql = "INSERT INTO`autohome_dealer`(name,brand,phone,address,Promotion) VALUES (%s,%s,%s,%s,%s)"
                data = (name,brand,phone,address,Promotion)
                cursor.execute(sql,data)
                db.commit()
        except Exception as e:
            print("save autohome_dealer fail %s"% e)