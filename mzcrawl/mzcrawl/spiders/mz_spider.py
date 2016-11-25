from scrapy.spider import Spider
from scrapy.selector import Selector
from mzcrawl.items import MzcrawlItem
from scrapy.http import Request
import redis


class MzSpider(Spider):
    name = "mzcrawl"
    allowed_domains =["www.mzitu.com"]
    start_urls = ['http://www.mzitu.com/']

    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)


    def parse(self, response):
        sel = Selector(response)
        urls = sel.xpath('//@href').extract()
        item = MzcrawlItem()
        for url in urls:
            if not self.r.get(url):
                self.r.set(url,url)
                if url.split('.')[-1] == "jpg":
                    item['jpg'] = url
                    yield item

                else:
                    yield Request(url,callback =self.parse)
                    
                
                
            
        
