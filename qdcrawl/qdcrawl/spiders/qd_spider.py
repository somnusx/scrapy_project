from scrapy.selector import Selector
from qdcrawl.items import QdcrawlItem
from scrapy.http import Request
from scrapy.spider import Spider

class QdSpider(Spider):
    name = 'qdcrawl'
    allowed_domains = ['qidian.com']
    start_urls = ['http://f.qidian.com/all?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page={}&month=-1&style=1&action=-1'.format(i) for i in range(1,21487)]
    
    def parse(self,response):
        sel = Selector(response)
        infos = sel.xpath('//h4/a/@href').extract()
        for info in infos:
            url = 'http:{}'.format(info) + '#Catalog'
            yield Request(url,callback=self.parse_sort)

    def parse_sort(self,response):
        sel = Selector(response)
        item = QdcrawlItem()
        sors = sel.xpath('//*[@id="j-catalogWrap"]/div[2]/div')
        for sor in sors:
            chapter = sel.xpath('.//h3/text()[2]').extract()[0]
            links = sel.xpath('.//ul/li/a/@href').extract()
            item['chap'] = chapter
            for link in links:
                lin = 'http:{}'.format(link)
                yield Request(lin, meta={'item':item}, callback=self.parse_chap)

    def parse_chap(self,response):
        item = response.meta['item']
        sel = Selector(response)
        nvname = sel.xpath('//*[@id="wrapbig"]/div[5]/div[1]/a[4]/text()').extract()[0]
        chapters = sel.xpath('//h1/text()').extract()[0]
        cons = sel.xpath('//p/text()').extract()
        con = '\n'.join(cons)
        item['nvnames'] = nvname
        item['chapter'] = chapters
        item['co'] = con
        return item
            
