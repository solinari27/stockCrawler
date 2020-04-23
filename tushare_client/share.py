#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: share.py 
@time: 2020/04/12 
"""  

import ConfigParser
import tushare as ts

cf = ConfigParser.ConfigParser()
cf.read('stockCrawler/tushare_client/tushare.ini')
TOKEN = cf.get("tushare", "token")

ts.set_token(token=TOKEN)
pro = ts.pro_api(TOKEN)

# # df = pro.daily(trade_date='20200325')
# # df = pro.trade_cal(exchange='', start_date='20200101', end_date='20200107', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
# # df = pro.daily(ts_code='000001.SZ', start_date='20190201', end_date='20200210')
# df = ts.get_tick_data('600848',date='2018-12-12',src='tt')
# # df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
# # df = pro.query('trade_cal', exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

# print(df.head(10000))

# print (ts.get_industry_classified())
# print (ts.get_concept_classified())
# print (ts.get_area_classified())
# print (ts.get_sme_classified())
# print (ts.get_gem_classified())
# print (ts.get_st_classified())
# print (ts.get_hs300s())
# print (ts.get_sz50s())
# print (ts.get_zz500s())
# print (ts.get_terminated())
# print (ts.get_suspended())