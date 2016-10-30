# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MkcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    types = scrapy.Field()
    language = scrapy.Field()
    subject = scrapy.Field()
    course = scrapy.Field()
    summary = scrapy.Field()
    video = scrapy.Field()
