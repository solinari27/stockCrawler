# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from common.mongo.sohuConn import SohuConn


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        url = item.get("url")
        code = item.get("code")
        date = item.get("date")
        raw_data = item.get("raw_data")
        sohuconn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
        # sohuconn = SohuConn("/home/ubuntu/stockCrawler/Conf/sohu.conf")
        sohuconn.set_name("stock_" + str(code) + " pipeline")

        for codedata in raw_data["hq"]:
            info = {"CODE": code,
                    "DATE": codedata[0],
                    "TOPEN": codedata[1],
                    "TCLOSE": codedata[2],
                    "CHG": codedata[3],
                    "PCHG": codedata[4],
                    "LOW": codedata[5],
                    "HIGH": codedata[6],
                    "VOTURNOVER": codedata[7],
                    "VATURNOVER": codedata[8],
                    "TURNOVER": codedata[9]}
            # add to mongo
            sohuconn.insertDailyData(info)

        # update date
        sohuconn.updateTime(code, date)
