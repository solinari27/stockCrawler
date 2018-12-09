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
        def do_init():
            self._keylist = {}
            self._keylist[u'\u6da8\u8dcc\u989d'] = 'CHG'
            self._keylist[u'\u80a1\u7968\u4ee3\u7801'] = 'CODE'
            self._keylist[u'\u603b\u5e02\u503c'] = 'TCAP'
            self._keylist[u'\u524d\u6536\u76d8'] = 'LCLOSE'
            self._keylist[u'\u6700\u9ad8\u4ef7'] = 'HIGH'
            self._keylist[u'\u6d41\u901a\u5e02\u503c'] = 'MCAP'
            self._keylist[u'\u6700\u4f4e\u4ef7'] = 'LOW'
            self._keylist[u'\u6210\u4ea4\u91cf'] = 'VOTURNOVER'
            self._keylist[u'\u65e5\u671f'] = 'DATE'
            self._keylist[u'\u6362\u624b\u7387'] = 'TURNOVER'
            self._keylist[u'\u540d\u79f0'] = 'NAME'
            self._keylist[u'\u6da8\u8dcc\u5e45'] = 'PCHG'
            self._keylist[u'\u5f00\u76d8\u4ef7'] = 'TOPEN'
            self._keylist[u'\u6536\u76d8\u4ef7'] = 'TCLOSE'
            self._keylist[u'\u6210\u4ea4\u91d1\u989d'] = 'VATURNOVER'

            s = time.localtime(time.time())
            year = s.tm_year
            mon = s.tm_mon
            day = s.tm_mday
            # end date is today
            enddate = str(year) + '%02d' % (mon) + '%02d' % (day)
            return enddate

        self.__load_conf()
        enddate = do_init()
        headers = {}
        cookies = {}
        conn = NeteaseConn(self._yamlconf['netease']['conf'])
        stocklist = conn.getStocks()

        for stock in stocklist:
            code = stock[0]
            type = stock[1]
            startdate = self._conn.getTime(code)
            # results = self._requestJson(type, code, startdate, enddate)
            # yield this


        yield "xxx"


    def parse(self, response):
        print 'parse'
