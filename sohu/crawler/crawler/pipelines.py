# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        raw_data = item.get("raw_data")
        url = item.get("url")
        code = item.get("code")
        date = item.get("date")

        # return item
