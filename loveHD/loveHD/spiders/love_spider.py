from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from loveHD.items import LovehdItem
import re

class Love_spider(Spider):
    name = 'loveHD'
    allowed_domains = ['api.ipip.net','api.lovebizhi.com','clientapi.lovebizhi.com','s.qdcdn.com']
    start_urls = ['http://api.lovebizhi.com/windows_v3.php?a=index&model_id=106&width=1366&height=768&client_id=1004&channel=30001&uuid=2f1187596eb64b40b772fa9eb517cc25&screen_width=1366&screen_height=768&bizhi_width=1366&bizhi_height=768&language=zh-CN&version_code=33&runtime_version=4.0.30319.42000&os_version=6.2.9200.0&device_id=69332240=1004&platform=windows&brand=&model=&manufacturer=ASUSTeK%20COMPUTER%20INC.&os_apilevel=0&imei=&device_id=69332240']

    def parse(response):
        print '________________________________________'
        print response + '-------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        links = re.findall('http.+?(?=")',response)
        items = []
        for link in links:
            item = LovehdItem()
            item['name'] = link
            items.append(item)
        return items
