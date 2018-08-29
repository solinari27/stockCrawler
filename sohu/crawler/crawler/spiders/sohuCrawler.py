#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: sohuCrawler.py 
@time: 2018/08/28 
"""  
import scrapy
from sohu.urltools import get_url

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
        url = get_url(str(300288))
        yield scrapy.Request (url=url, headers=headers, callback=self.parse, cookies=cookies)

    def parse(self, response):
        print response.body


