# -*- coding: utf-8 -*-
# @Author  : Solinari
# @Email   : 
# @File    : neteaseCrawler.py
# @Software: PyCharm
# @Time    : 2018/12/09

import os
import time
import json
import yaml
import scrapy
from common.mongo.neteaseConn import NeteaseConn


class NeteaseCrawler(scrapy.Spider):
    name = "NeteaseCrawler"
    allowed_domains = ["www.163.com"]

    def __load_conf(self):
        yamlPath = os.path.join(os.getcwd(), 'spider.yaml')

        f = open(yamlPath, 'r')
        self._yamlconf = yaml.load(f.read())  # 用load方法转字典

    def start_requests(self):
        """
        start with url in mongodb!!!
        :return:
        """
        self.__load_conf()
        headers = {}
        cookies = {}
        conn = NeteaseConn(self._yamlconf['netease']['conf'])
        stocklist = conn.getStocks()

        for stock in stocklist:
            code = stock[0]
            type = stock[1]
            pass

        yield "xxx"


    def parse(self, response):
        print 'parse'
