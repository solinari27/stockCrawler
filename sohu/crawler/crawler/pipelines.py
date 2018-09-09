# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        url = item.get ("url")
        code = item.get ("code")
        date = item.get ("date")
        raw_data = item.get("raw_data")

        for data in raw_data["hq"]:
            print data
        # return item
