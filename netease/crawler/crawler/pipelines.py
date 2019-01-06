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
        def loadjson():
            cf = open(file, 'r')
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
            os.remove(file)
            return results

        url = item.get("url")
        code = item.get("code")
        date = item.get("date")
        file = item.get("file")

        self.__load_conf()
        self.__conn = NeteaseConn(self._yamlconf['netease']['conf'])
        self.__conn.set_name("stock_" + str(code) + " pipeline")

        result = loadjson()
        for item in result:
            item['CODE'] = code
            self.__conn.insertDailyData(item)
        self.__conn.updateTime(code, date)
