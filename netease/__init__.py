#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: __init__.py.py 
@time: 2018/06/13 
"""  

import json
import requests

def requestJson(url):
    response = requests.get(url=url)
    print response.content
    # content = json.loads(response.content)
    # print content

# sohu
# url = "http://q.stock.sohu.com/hisHq?code=cn_300228&start=20130930&end=20131231&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp"
# requestJson(url)

# netease
url = "http://quotes.money.163.com/service/chddata.html?code=0601857&start=20071105&end=20150618&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
url = "http://quotes.money.163.com/service/chddata.html?code=0601857&start=20071105&end=20150618"
requestJson(url)