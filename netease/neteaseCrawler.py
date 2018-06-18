#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: neteaseCrawler.py
@time: 2018/06/13
"""

import json
import csv
import os
import requests


class neteaseCrawler():
    def __init__(self):
        return

    def requestJson(self, code):
        def loadjson():
            cf = open(filename, 'r')
            results = []
            for x in csv.DictReader(cf):
                d = json.dumps(x, indent=4, separators=(',', ':'), ensure_ascii=False)  # ,sort_keys=True
                results.append(d)
            cf.close()
            return results

        filename = '../Data/' + code + '.csv'
        url = "http://quotes.money.163.com/service/chddata.html?code=0" + code + "&start=20071105&end=20150618&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        response = requests.get(url = url)
        with open(filename, 'w') as f:
            f.write(response.content.decode('gb2312').encode('utf-8'))
        f.close()
        return loadjson()
        os.remove(filename)

# netease
n = neteaseCrawler()
n.requestJson('601857')


