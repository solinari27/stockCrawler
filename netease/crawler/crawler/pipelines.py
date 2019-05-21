# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import yaml
import csv
from common.mongo.neteaseConn import NeteaseConn


class CrawlerPipeline(object):
    def __load_conf(self):
        yamlPath = os.path.join(os.getcwd(), 'spider.yaml')

        f = open(yamlPath, 'r')
        self._yamlconf = yaml.load(f.read())  # 用load方法转字典

    def process_item(self, item, spider):
        def loadjson(file):
            cf = open(file, 'r')
            results = []
            for x in csv.DictReader(cf):
                d = json.dumps(x, indent=4, separators=(',', ':'),
                               ensure_ascii=False)  # ,sort_keys=True
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
            os.remove(file)
            return results

        url = item.get("url")
        code = item.get("code")
        date = item.get("date")
        file = item.get("file")

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

        self.__load_conf()
        self.__conn = NeteaseConn(self._yamlconf['netease']['conf'])
        self.__conn.set_name("stock_" + str(code) + " pipeline")

        result = loadjson(file=file)
        for item in result:
            item['CODE'] = code
            self.__conn.insertDailyData(item)
        self.__conn.updateTime(code, date)
