# -*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Content-Type':'application/json;charset=utf-8',
        'Accept':'application/json'
    }
keywords = "文物古迹"
city = "chengdu"
page = 1
key = "b35f0cede5d6c4d26497f02a93ce3e51"
url = 'https://restapi.amap.com/v3/place/text?keywords={keywords}&city={city}&output=json&offset=20&page={page}&key={key}&extensions=all'
def gethtml(url,keywords,city,page,key,headers):
    url = url.format(keywords = keywords,city=city,page=page,key=key)
    try:
        r = requests.get(url,headers=headers)
        r.raise_for_status()
    except requests.RequestException as e:
        print e
    else:
        result = r.json()
        return result

def parse(jsons,details):
    try:
        for item in jsons['pois']:
            id = item['id']
            name = item['name']
            type = item['type']
            add = item['add']
            adnames=item['adnames']
            locations=item['locations']

            play = {"id":id,'name':name,'type':type,'add':add,'adname':adnames,'locations':locations}
            details.append(play)
    except:
        pass

def loop(num):
    global page
    while page < num:
        jsons = gethtml(url,keywords,city,page,key,headers)
        parse(jsons,details)
        page = page+1

details = [ ]
loop(2)
for i in details:
    print i
