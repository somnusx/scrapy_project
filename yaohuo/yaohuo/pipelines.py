# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class YaohuoPipeline(object):
    def __init__(self):
        self.file = codecs.open('name.json',mode='wb',encoding='utf-8')
    def process_item(self, item, spider):
        lin = json.dumps(dict(item)) +'\n'
        self.file.write(lin.decode('unicode_escape'))
        return item
