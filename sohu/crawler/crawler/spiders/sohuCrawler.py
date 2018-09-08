#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: sohuCrawler.py 
@time: 2018/08/28 
"""
import time
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
        def get_today():
            s = time.localtime(time.time())
            year = s.tm_year
            mon = s.tm_mon
            day = s.tm_mday
            # end date is today
            return str(year) + '%02d' % (mon) + '%02d' % (day)

        headers = {}
        cookies = {}
        conn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
        stocklist = conn.getStocks()

        for stock in stocklist:
            code = stock[0]
            type = stock[1]
            start_date = conn.getTime(code=code)
            end_date = get_today()
            url = get_url(code=str(code), start=start_date, end=end_date)
            yield scrapy.Request(url=url, headers=headers, callback=self.parse, cookies=cookies)
            # FIXME: add time intervals in scrapy
            time.sleep(10)

    def parse(self, response):
        print response.body


