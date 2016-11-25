from scrapy.selector import Selector
from novelcrawl.items import NovelcrawlItem
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re

class NovelSpider(CrawlSpider):
    name = "novelcrawl"
    allowed_domains = ["seecd.net"]
    start_urls = ['http://www.seecd.net/top/allvisit-{}.html'.format(i) for i in range(1,5382)]

    rules = (
        Rule(LinkExtractor(allow=('book-[0-9]{1,9}\.html', )), callback='parse_two',follow=True),
    )
    def parse_item(self,response):
        sel = Selector(response)
        hrefs = sel.xpath('//a/@href').extract()

        for href in hrefs:
            hre = re.findall('http://www.seecd.net/book-[0-9]{0,9}\.html',href)
            if hre:
                yield Request(hre[0],callback=self.parse_two)

    def parse_two(self,response):
        sel = Selector(response)
        url = sel.xpath('//*[@id="content"]/dd[2]/div[1]/a/@href').extract()[0]
        ur = 'http://www.seecd.net{}'.format(url)
        yield Request(ur,callback=self.parse_three)

    def parse_three(self,response):
        sel = Selector(response)
        cons = sel.xpath('//tr/td/a/@href').extract()
        for con in cons:
            yield Request(response.url.split('index')[0] + con, callback=self.parse_four)

    def parse_four(self,response):
        sel = Selector(response)
        sor = sel.xpath('//*[@id="amain"]/dl/dt/a[2]/text()').extract()[0]
        name = sel.xpath('//*[@id="amain"]/dl/dt/a[3]/text()').extract()[0]
        novels = sel.xpath('//*[@id="contents"]/text()').extract()
        novel = '\n'.join(novels)
        
            
        item = NovelcrawlItem()
        item['nvname'] = name
        item['sort'] = sor
        item['nove'] = novel        

        return item

            
        
        
