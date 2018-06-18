#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: neteaseCrawler.py
@time: 2018/06/13
"""

import json
import requests
import pandas as pd


class neteaseCrawler():
    def __init__(self):
        return

    def requestcsv(self, code):
        url = "http://quotes.money.163.com/service/chddata.html?code=0" + code + "&start=20071105&end=20150618&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        response = requests.get(url=url)
        filename = '../Data/' + code + '.csv'
        with open(filename, 'w') as f:
            f.write(response.content)
        f.close()

    def loadjson(self, code):
        df1 = pd.read_csv('../Data/' + code + '.csv')
        print df1


# netease
n = neteaseCrawler()
n.requestcsv('601857')
n.loadjson('601857')


