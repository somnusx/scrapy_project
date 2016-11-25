from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
from ffdy.items import FfdyItem


class Ffdy_spider(Spider):
    name = 'ffdy'
    allowed_domains = ['www.ffdy.cc']
    start_urls = ['http://www.ffdy.cc/list/1.html']


    def parse(self,response):
        sel = Selector(response)
        links = sel.xpath('//*[@id="main"]/div[2]/div[2]/ul/li/h3/a/@href').extract()
        next_page = sel.xpath('//*[@id="main"]/div[2]/div[3]/a[8]/@href').extract()
        if next_page[0]:
            url = 'http://www.ffdy.cc' + next_page[0]
            print url
            yield Request(url,callback=self.parse)

        for link in links:
            item = FfdyItem()
            item['link'] = link
            yield item

