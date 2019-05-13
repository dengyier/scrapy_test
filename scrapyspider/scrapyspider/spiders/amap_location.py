# -*- coding: utf-8 -*-
import re
import json
import demjson
from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem

class AmapLocation(Spider):
    name = "location"
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Referer':'https://www.amap.com/'
    }
    keywords = "文物古迹"
    city = "chengdu"
    page = 1
    key = "b35f0cede5d6c4d26497f02a93ce3e51"


    def start_requests(self):
        url = 'https://restapi.amap.com/v3/place/text?keywords=%E6%96%87%E7%89%A9%E5%8F%A4%E8%BF%B9&city=%E6%88%90%E9%83%BD&output=json&offset=20&page=1&key=b35f0cede5d6c4d26497f02a93ce3e51&extensions=all'
        yield Request(url,headers=self.headers)


    def parse(self, response):
        datas = json.loads(response.body)
        item = DoubanMovieItem()

        datas = eval(json.dumps(datas))
        datanew = datas['pois']

        for data in range(len(datanew)):
            # item['id'] = datanew[data+1]['id']
            item['name'] = datanew[data+1]['name'].decode("unicode-escape")
            item['type'] = datanew[data+1]['type'].decode("unicode-escape")
            item['address'] = datanew[data+1]['address'].decode("gbk")
            item['location'] = datanew[data+1]['location']
            item['adname'] = datanew[data+1]['adname'].decode("unicode-escape")
            yield item


            page_num = re.search(r'page=(\d+)',response.url).group(1)
            page_num = 'page='+ str(int(page_num)+1)
            next_url = re.sub(r'page=\d+',page_num,response.url)
            yield Request(next_url,headers=self.headers)




