# -*- coding: utf-8 -*-
# @Author  : Solinari
# @Email   : 
# @File    : neteaseCrawler.py
# @Software: PyCharm
# @Time    : 2018/12/09

import os
import time
import yaml
import scrapy
from common.mongo.neteaseConn import NeteaseConn
from netease.utils import get_url
from netease.crawler.crawler.items import CrawlerItem


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
            s = time.localtime(time.time())
            year = s.tm_year
            mon = s.tm_mon
            day = s.tm_mday
            # end date is today
            enddate = str(year) + '%02d' % (mon) + '%02d' % (day)
            return enddate

        def get_today():
            s = time.localtime(time.time())
            year = s.tm_year
            mon = s.tm_mon
            day = s.tm_mday
            # end date is today
            return str(year) + '%02d' % (mon) + '%02d' % (day)

        self.__load_conf()
        enddate = do_init()
        headers = {}
        cookies = {}
        self.__conn = NeteaseConn(self._yamlconf['netease']['conf'])
        stocklist = self.__conn.getStocks()

        for stock in stocklist:
            code = stock[0]
            type = stock[1]
            startdate = self.__conn.getTime(code, today=get_today())
            url = get_url(type=str(type), code=str(code), startdate=startdate, enddate=enddate)
            meta = {
                "url": url,
                "code": code,
                "date": enddate
            }
            yield scrapy.Request(url=url, headers=headers, callback=self.parse, cookies=cookies, meta=meta)
            time.sleep(5)

    def parse(self, response):
        """
        get csv file
        :param response:
        :return:
        """
        filename = 'data/' + response.meta['code'] + '.csv'
        filename = os.path.join(os.getcwd(), filename)
        with open(filename, 'w') as f:
            f.write(response.body.decode('gb2312').encode('utf-8'))
        f.close()

        item = CrawlerItem()
        item["file"] = filename
        item["url"] = response.meta["url"]
        item["code"] = response.meta["code"]
        item["date"] = response.meta["date"]

        # 将item提交给pipelines
        yield item
