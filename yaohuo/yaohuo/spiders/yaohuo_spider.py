from scrapy.http import request
from scrapy.selector import Selector
from scrapy.spider import Spider
from yaohuo.items import YaohuoItem


class Yao_spider(Spider):
    name = 'yaohuo'
    allowed_domains = ['www.yaohuo.net/t/']
    start_urls = ['http://www.yaohuo.net/t/']


    def parse(self,response):
        sel = Selector(response)
        names = sel.xpath("//p[@class='post1']/text()").extract()
        items = []
        for i in names:
            item = YaohuoItem()
            item['name'] = i
            items.append(item)
        return items
