#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: sohuCrawler.py 
@time: 2018/08/28 
"""  
import scrapy

class Sohu_crawler(scrapy.Spider):
    def get_url(code=None, start=None, end=None):
        url = "http://q.stock.sohu.com/hisHq?code=cn_" + str (code) + \
              "&start=20130930&end=20131231&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp"
        return url

    name = "SohuCrawler"
    allowed_domains = ["www.sohu.com"]
    start_urls = []
    start_urls = start_urls.append(get_url(code=300228))
    # start_urls = ["http://q.stock.sohu.com/hisHq?code=cn_300228&start=20130930&end=20131231&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp"]

    def parse(self, response):
        print response.body


