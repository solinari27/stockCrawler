#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: collection.py
@time: 2018/10/09
"""


from common.mongo.mongoConn import mongoConn
from common.mongo.sohuConn import SohuConn
# netease Conn

sohuconn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
neteaseconn = mongoConn.mongoConn()