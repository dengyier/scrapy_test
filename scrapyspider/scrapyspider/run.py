# -*- coding: utf-8 -*-
from scrapy import cmdline

# name = 'douban_movie_top250'
# name = 'douban_ajax'
name = 'location'
cmd =  'scrapy crawl {0} -o culture.csv'.format(name)
cmdline.execute(cmd.split())