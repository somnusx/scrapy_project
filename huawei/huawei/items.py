# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuaweiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    big = scrapy.Field()
    time = scrapy.Field()
    name = scrapy.Field()
    version = scrapy.Field()
    deve = scrapy.Field()
