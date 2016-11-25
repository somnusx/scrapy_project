from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
from yaome.items import YaomeItem

class Yaome_spider(Spider):
    name = 'yaome'
    allowed_domains = ['yaohuo.me']

    cookies = {
    'GUID':'9571651818064021',
    'ASP.NET_SessionId':'adkuv1yppgpfhkuuyg2nwn55',
    'GET35188':'', 
    'sidyaohuo':'08F942A33923B98_C88_05187_30480_31001-2-0-0-0-0'
        }

    def start_requests(self):
        return [Request('http://www.yaohuo.me/',cookies=self.cookies,callback=self.parse)]

    
    def parse(self,response):
        sel = Selector(response)
        ne = sel.xpath('/html/body/div[7]/a[2]/@href').extract()[0]
        yield Request('http://www.yaohuo.me{}'.format(ne),cookies=self.cookies,callback=self.tw_parse)

    def tw_parse(self,response):
        sel = Selector(response)
        links = sel.xpath('/html/body/div/a[1]')
        
        for le in links:
            item = YaomeItem()
            item['link'] = le.xpath('.//@href').extract()[0]
            item['name'] = le.xpath('.//text()').extract()[0]
            yield item
            
