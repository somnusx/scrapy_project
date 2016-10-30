# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QdcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chap = scrapy.Field()
    nvnames = scrapy.Field()
    chapter = scrapy.Field()
    co = scrapy.Field()
