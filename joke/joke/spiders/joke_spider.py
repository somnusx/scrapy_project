from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
from joke.items import JokeItem


class Joke_spider(Spider):
    name = 'joke'
    allowed_domains = ['www.jokeji.cn']
    start_urls = ['http://www.jokeji.cn/search.asp?MaxPerPage=33&me_page=1']


    def parse(self,response):
        sel = Selector(response)
        links = sel.xpath('//tr/td[2]/a/@href').extract()
        next_page = sel.xpath("//*[@align='center']/td[3]/a/@href").extract()[0]
        items = []
        for link in links:
            item = JokeItem()
            item['joke'] = link
            items.append(item)
        return items
            #yield Request('http://www.jokeji.cn{}'.format(link),callback=self.de_parse)


            
##        if next_page:
##            yield Request('http://www.jokeji.cn/search.asp{}'.format(next_page),callback=self.parse)

##    def de_parse(self,response):
##        sel = Selector(response)
##        jos = sel.xpath('//*[@face="Verdana"]/text()').extract()
##        items = []
##        for jo in jos:
##            if jo:
##                item = JokeItem()
##                item['joke'] = jo
##        yield items
            
