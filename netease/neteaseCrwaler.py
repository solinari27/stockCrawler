#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: neteaseCrwaler.py 
@time: 2018/06/13 
"""  

import json
import requests
import pandas as pd
import csv

def requestJson(url):
    response = requests.get(url=url)
    # print response.content
    print json.dumps (list(csv.reader(response.content.decode('utf8'))))
    # content = pd.read_csv(response.content)
    # content = json.loads (response.content)
    # print content

# netease
url = "http://quotes.money.163.com/service/chddata.html?code=0601857&start=20071105&end=20150618&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
url = "http://quotes.money.163.com/service/chddata.html?code=0601857&start=20071105&end=20150618"
requestJson(url)