#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: neteaseCrwaler.py
@time: 2018/06/13
"""

import json
import requests
import pandas as pd
import csv


def neteaseCrwaler():
    def requestCsv(code):
        url = "http://quotes.money.163.com/service/chddata.html?code=0" + code + "&start=20071105&end=20150618&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        response = requests.get(url=url)
        # print response.content
        # print json.dumps (list(csv.reader(response.content.decode('utf8'))))
        # content = pd.read_csv(response.content)
        # content = json.loads (response.content)
        # print content
        filename = '../Data/' + code + '.csv'
        with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(response.content)
        f.close()

    def loadJson(code):

# # netease
# requestCsv('601857')