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
import csv
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
        def loadjson():
            cf = open(filename, 'r')
            results = []
            for x in csv.DictReader(cf):
                d = json.dumps(x, indent=4, separators=(',', ':'), ensure_ascii=False)  # ,sort_keys=True
                d2 = json.loads(d)
                d3 = {}
                for key in d2.keys():
                    try:
                        d3[self._keylist[key]] = float(d2[key])
                    except:
                        d3[self._keylist[key]] = d2[key]
                results.append(d3)
                # self._conn.insertDailyData(d2)
            cf.close()
            os.remove(filename)
            return results

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

        # result = loadjson()
        # for item in result:
        #     item['CODE'] = item['CODE'][1:6]
        #     self.__conn.insertDailyData(item)
        # self.__conn.updateTime(response.meta['code'], response.meta['date'])