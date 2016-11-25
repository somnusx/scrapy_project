from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
from huawei.items import HuaweiItem

class Hua_spider(Spider):
    name = 'huawei'
    allowed_domains = ['appimg.hicloud.com','appstore.huawei.com']
    start_urls = ['http://appstore.huawei.com/more/all/1']

    def parse(self,response):
        sel = Selector(response)
        names = sel.xpath('//h4/a/@href').extract()
        for name in names:
            yield Request(name,callback=self.tw_parse)
            
    def tw_parse(self,response):
        sel = Selector(response)
        name = sel.xpath("//p[1]/span[@class='title']/text()").extract()[0]
        big = sel.xpath("//li[@class='ul-li-detail'][1]/span/text()").extract()[0]
        time = sel.xpath("//li[@class='ul-li-detail'][2]/span/text()").extract()[0]
        deve = sel.xpath("//li[@class='ul-li-detail'][3]/span/text()").extract()[0]
        version = sel.xpath("//li[@class='ul-li-detail'][4]/span/text()").extract()[0]
        item = HuaweiItem()
        item['big'] = big
        item['name'] = name
        item['time'] = time
        item['deve'] = deve
        item['version'] = version
        return item
