#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: scrapyCfiSpider.py
@time: 2018/04/01
"""

import scrapy
import re

class scrapyCfiSpider(scrapy.Spider):
    name = "scrapyCfiSpider"
    start_urls = ['http://quote.cfi.cn/stockList.aspx?t=11']
    allowed_domains = ["quote.cfi.cn"]

    def parse(self, response):
        body = response.body
        unicode_body = response.body_as_unicode ()
        stock = {}
        for sel in response.xpath ('//div[@id="divcontent"]'):
            stocks = sel.re (r'<td><a href=*>*(.+?)</a>(.+?)</td>')
            if not stocks:
                pass
            else:
                for it in stocks:
                    codestr = re.search(r'\d\d\d\d\d\d', it)
                    code = codestr.group()
                    left = re.search(r'(?<=\"\>).+?$', it)
                    leftname = left.group()
                    stocknamesplit = leftname.split("(")
                    stockname = stocknamesplit[0]
                    stock['code'] = code
                    stock['name'] = stockname
                    yield stock

