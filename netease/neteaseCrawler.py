#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: neteaseCrawler.py
@time: 2018/06/13
"""

import json
import requests
import csv,json
import pandas as pd


class neteaseCrawler():
    def __init__(self):
        return

    def requestcsv(self, code):
        filename = '../Data/' + code + '.csv'
        url = "http://quotes.money.163.com/service/chddata.html?code=0" + code + "&start=20071105&end=20150618&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        response = requests.get(url=url)
        with open(filename, 'w') as f:
            f.write(response.content.decode('gb2312').encode('utf-8'))
        f.close()

    def loadjson(self, code):
        filename = '../Data/' + code + '.csv'
        cf = open(filename, 'r')
        for x in csv.DictReader(cf):
            d = json.dumps(x, indent=4, separators=(',', ':'), ensure_ascii=False)  # ,sort_keys=True
            print d
        cf.close()

        # t1 = pd.read_csv(filename)
        # print t1.to_json()


# netease
n = neteaseCrawler()
n.requestcsv('601857')
n.loadjson('601857')


