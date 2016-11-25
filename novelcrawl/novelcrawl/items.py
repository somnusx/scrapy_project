# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nvname = scrapy.Field()
    sort = scrapy.Field()
    nove = scrapy.Field()
