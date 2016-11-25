from scrapy.spider import Spider
from scrapy.selector import Selector
from mkcrawl.items import MkcrawlItem 
from scrapy.http import Request

      
class DmozSpider(Spider):
    name = "mkcrawl"
    allowed_domains = ["imooc.com"]
    url = 'http://www.imooc.com/course/list?page={}'
    start_urls = [ url.format(i) for i in range(1,26) ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="main"]/div[2]/div[2]/div[1]/ul/div/a/@href').extract()
        for site in sites:
            url = "http://www.imooc.com{}".format(site)           
            yield Request(url, callback=self.two_parse)

    def two_parse(self, response):
        sel = Selector(response)
        name_2 = sel.xpath('//*[@id="main"]/div[1]/div[1]/div[1]/a[2]/text()').extract()[0]
        name_1 = sel.xpath('//*[@id="main"]/div[1]/div[1]/div[1]/a[3]/text()').extract()[0]
        name0 = sel.xpath('//*[@id="main"]/div[1]/div[1]/div[2]/h2/text()').extract()[0]
        sites = sel.xpath('//div[@class="chapter "]')      
        for site in sites:
            name1 = site.xpath('.//strong/text()').extract()[-2]
            content = site.xpath('.//ul[@class="video"]/li')
            for cont in content:
                nam = cont.xpath('.//a/text()').extract()
                link = cont.xpath('.//a/@href').extract()[0]
                item = MkcrawlItem()
                item['types'] = name_2
                item['language'] = name_1
                item['subject'] = name0
                item['course'] = name1.strip()
                item['summary'] = nam[1].replace(' ','').split()[0]
                item['video'] = link
        yield item
        
