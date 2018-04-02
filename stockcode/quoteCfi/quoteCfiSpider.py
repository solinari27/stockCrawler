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
        with open("Data/out.json", 'r') as load_f:
            stocks = json.load(load_f)

        # self._conn.cleanStock()

        for item in stocks:
            self._conn.insertStock(item['code'], item['name'])