#-*-coding:utf-8-*-
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector
from scrapy.spider import Spider


class Post_spider(Spider):
    name = 'post'
    allowed_domains = ['yaohuo.me']
    #start_urls = ['http://yaohuo.me/']#不会打开这个网页

    def start_requests(self):
        data = {'logname':'13255290027','logpass':'zxcvbnm123','savesid':'0','action':'login','classid':'0','siteid':'1000','sid':'-3-0-0-0-0','backurl':'waplogout.aspx%3Fsiteid%3D1000&g=%E7%99%BB+%E5%BD%95'}
        return [FormRequest(url='http://yaohuo.me/waplogin.aspx',formdata = data,callback=self.parse)]

    def parse(self,response):
        print response.body

        
