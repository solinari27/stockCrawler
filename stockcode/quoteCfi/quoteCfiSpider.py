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
        if (os.path.exists("Data/quoteCfiShanghai.json")):
            os.remove("Data/quoteCfiShanghai.json")
        os.system("scrapy runspider stockcode/spider/scrapyCfiShanghai.py -o Data/quoteCfiShanghai.json --logfile Log/quoteCfiSpider.log --loglevel ERROR")
        if (os.path.exists("Data/quoteCfiShenzhen.json")):
            os.remove("Data/quoteCfiShenzhen.json")
        os.system("scrapy runspider stockcode/spider/scrapyCfiShenzhen.py -o Data/quoteCfiShenzhen.json --logfile Log/quoteCfiSpider.log --loglevel ERROR")

    def inputDB(self):
        #self._conn.cleanStock()
        
        with open("Data/quoteCfiShanghai.json", 'r') as load_f:
            stocks = json.load(load_f)

        for item in stocks:
            self._conn.insertStock(item['code'], item['name'], item['type'])
            
        with open("Data/quoteCfiShenzhen.json", 'r') as load_f:
            stocks = json.load(load_f)

        for item in stocks:
            self._conn.insertStock(item['code'], item['name'], item['type'])
            
            
#0: [http://quote.cfi.cn/stockList.aspx?t=11]
#1：[http://quote.cfi.cn/stockList.aspx?t=12]
#2: [http://quote.cfi.cn/stockList.aspx?t=13]
#3: [http://quote.cfi.cn/stockList.aspx?t=14]