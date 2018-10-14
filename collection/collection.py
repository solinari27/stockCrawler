#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: collection.py
@time: 2018/10/09
"""
from common.mongo.sohuConn import SohuConn
from common.mongo.neteaseConn import NeteaseConn

sohuconn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
neteaseconn = NeteaseConn("/home/solinari/workspace/stockCrawler/Conf/netease.conf")

print neteaseconn.getDailyData()