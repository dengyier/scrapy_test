# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#
# class ScrapyspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
class DoubanMovieItem(scrapy.Item):
    # 排名
    # ranking = scrapy.Field()
    #电影名称
    # movie_name = scrapy.Field()
    #评分
    # score = scrapy.Field()
    #评论人数
    # score_num = scrapy.Field()
    #用户id
    # id =scrapy.Field()
    #name景点名称
    name =scrapy.Field()
    #type 游玩类型
    type = scrapy.Field()
    #address 地址
    address = scrapy.Field()
    #adname 区
    adname = scrapy.Field()
    #location 经纬度
    location = scrapy.Field()


