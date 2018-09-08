#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: sohuCrawler.py 
@time: 2018/08/28 
"""  
import scrapy
from sohu.urltools import get_url
from common.mongo.sohuConn import SohuConn

class Sohu_crawler(scrapy.Spider):
    name = "SohuCrawler"
    allowed_domains = ["www.sohu.com"]

    def start_requests(self):
        """
        start with url in mongodb!!!
        :return:
        """
        headers = {}
        cookies = {}
        conn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
        stocklist = conn.getStocks()

        for stock in stocklist:
            code = stock[0]
            type = stock[1]
            date = conn.getTime(code=code)
            url = get_url(str(code))
            # FIXME: use date to make url
            yield scrapy.Request(url=url, headers=headers, callback=self.parse, cookies=cookies)
            # FIXME: add time intervals

    def parse(self, response):
        print response.body


