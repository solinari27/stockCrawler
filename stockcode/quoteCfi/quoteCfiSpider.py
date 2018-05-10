#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: quoteCfiSpider.py 
@time: 2018/04/01 
"""  

import os
import json

import stockcode.mongoConn as mc

class quoteCfiSpider():

    def __init__(self):
        self._conn = mc.mongoConn()

    def crawl(self):
        os.system("scrapy runspider stockcode/spider/scrapyCfiSpider.py -o Data/quoteCfiSpider.json --logfile Log/quoteCfiSpider.log --loglevel ERROR")

    def inputDB(self):
        with open("Data/quoteCfiSpider.json", 'r') as load_f:
            stocks = json.load(load_f)

        # self._conn.cleanStock()

        for item in stocks:
            self._conn.insertStock(item['code'], item['name'])
            
            
#0: [http://quote.cfi.cn/stockList.aspx?t=11]
#1：[http://quote.cfi.cn/stockList.aspx?t=12]
#2: [http://quote.cfi.cn/stockList.aspx?t=13]
#3: [http://quote.cfi.cn/stockList.aspx?t=14]