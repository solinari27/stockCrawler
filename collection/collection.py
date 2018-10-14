#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: collection.py
@time: 2018/10/09
"""
from common.mongo.sohuConn import SohuConn
from common.mongo.neteaseConn import NeteaseConn
import time

sohuconn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
neteaseconn = NeteaseConn("/home/solinari/workspace/stockCrawler/Conf/netease.conf")

s = time.localtime(time.time())
year = s.tm_year
mon = s.tm_mon
day = s.tm_mday
#end date is today
enddate = str(year) + '%02d' % (mon) + '%02d' % (day)
print s
# print neteaseconn.getDailyData(code=str("'600000")) #new bug to fix for '