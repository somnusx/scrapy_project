from scrapy.spider import Spider
from scrapy.selector import Selector
from ymcrawl.items import YmcrawlItem
from scrapy.http import Request


class Ymspider(Spider):
    name = 'ymcrawl'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['https://www.amazon.cn/s/ref=sr_pg_2?rh=n%3A2016116051%2Cn%3A%212016117051%2Cn%3A664978051%2Cn%3A665002051%2Cp_4%3AHUAWEI+%E5%8D%8E%E4%B8%BA&page={}&ie=UTF8'.format(i) for i in range(1,2)]

    def parse(self,response):
        sel = Selector(response)
        links = sel.xpath('//div/div[3]/div[1]/a/@href').extract()
        for link in links:    
            yield Request(link,callback=self.parse_two)

    def parse_two(self,response):
        sel = Selector(response)
        name = sel.xpath('//*[@id="productTitle"]/text()').extract()
        price = sel.xpath('//*[@id="priceblock_ourprice"]/text()').extract()
        links = sel.xpath('//li/@ data-dp-url').extract()

        item = YmcrawlItem()
        if name:            
            item['name'] = name[0].strip()
        if price:
            item['price'] = price[0]

        for link in links:
            url = 'https://www.amazon.cn{}'.format(link)
            yield Request(url, meta={ 'item':item },callback=self.parse_three)
            
    def parse_three(self,response):
        sel = Selector(response)
        name = sel.xpath('//*[@id="productTitle"]/text()').extract()
        price = sel.xpath('//*[@id="priceblock_ourprice"]/text()').extract()
        item = response.meta['item']

        if name:            
            item['name'] = name[0].strip()
        if price:
            item['price'] = price[0]
        return item
