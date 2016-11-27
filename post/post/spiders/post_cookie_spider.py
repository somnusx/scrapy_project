#-*-coding:utf-8-*-
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector
from scrapy.spider import Spider


class Post_spider(Spider):
    name = 'post'
    allowed_domains = ['www.rs05.com']


    def start_requests(self):
        data = {'uid':'somnus@163.com','pwd':'zxcvbnm123'}
        return [FormRequest(url='http://www.rs05.com/user/process/do-login.php',meta = {'cookiejar':1},formdata = data,callback=self.parse)]

    def parse(self,response):
        #print response.body
        sel = Selector(response)
        link = sel.xpath('//*[@id="top"]/div[2]/a[1]/@href').extract()[0]
        print link
        yield Request(link,meta = {'cookiejar':response.meta['cookiejar']},callback=self.t_parse)


    def t_parse(self,response):
        print response.body
        print '------>>>>>>>>>'
        print response.meta['cookiejar']

        
