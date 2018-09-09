# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from common.mongo.sohuConn import SohuConn

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        url = item.get ("url")
        code = item.get ("code")
        date = item.get ("date")
        raw_data = item.get("raw_data")
        sohuconn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
        sohuconn.set_name("stock_" + str(code) + " pipeline")

        for data in raw_data["hq"]:
            print data
            # add to mongo
        # return item
