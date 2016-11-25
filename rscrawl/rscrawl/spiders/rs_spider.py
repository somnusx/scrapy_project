from scrapy.spider import Spider
from scrapy.selector import Selector
from rscrawl.items import RscrawlItem 
from scrapy.http import Request

      
class DmozSpider(Spider):
    name = "rscrawl"
    allowed_domains = ["rs05.com"]
    url = 'http://www.rs05.com/'
    start_urls = [ url ]

    def parse(self,response):
        sel = Selector(response)
        cons = sel.xpath('/html/body/div[2]/div[1]/ul/li/h2/a/@href').extract()
        xia = sel.xpath('/html/body/div[2]/div[1]/div/div/a[11]/@href').extract()[0]
        for con in cons:
            url = "http://www.rs05.com/{}".format(con)
            yield Request(url, callback=self.two_parse)

        yield Request(xia, callback=self.parse)
    def two_parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('/html/body/div[4]/div[1]/div[1]/div[5]')
        items = []
        for site in sites:
            links = site.xpath('.//p/a')            
            for link in links:
                torr = link.xpath('.//@href').extract()[0]
                nam = link.xpath('.//text()').extract()[0]
                if nam.split('/')[0] == 'http:':
                    continue
                item = RscrawlItem()
                item['name'] = nam
                item['too'] = torr
                items.append(item)
            return items


        
