#!usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author: solinari 
@file: sohuConn.py 
@time: 2018/08/29 
"""
import sys
import json
import urllib
from mongoConn import mongoConn
from pymongo import MongoClient


class SohuConn(mongoConn):
    def __init__(self, confile=None):
        assert confile is not None

        self.__name__ = "sohuCrawler Mongo Conn"
        # 注意路径配置
        with open(confile) as f:
            self._mongoConf = json.load(f)

        # init logging:
        self._logConf = self._mongoConf['logging']

        self.init_logger()
        try:
            if sys.version > '3':
                username = urllib.parse.quote_plus(self._username)
                password = urllib.parse.quote_plus(self._password)
            else:
                username = urllib.quote_plus(self._username)
                password = urllib.quote_plus(self._password)
            self._conn = MongoClient('mongodb://%s:%s@%s' % (username, password, self._host))
            if not self._check_connected(self._conn):
                self._logger.error(self.__name__ + " mongo connection failed.")
                sys.exit(1)

            # self.connected = self.db.authenticate (self._username, self._password)
            self._stockdb = self._conn.stockinfo
            self._datadb = self._conn.sohustockdata

        except Exception:
            self._logger.error(self.__name__ + " mongo connection failed.")

    def __del__(self):
        self._logger.info(self.__name__ + " mongo connection stopped.")
        self._conn.close()
        self._logger.removeHandler(self._logfile_handler)

    def set_name(self, name=None):
        assert name is not None
        self.__name__ = name

    def getStocks(self):
        stockslist = []
        try:
            stocks = self._stockdb.stocklist.find()
            for stock in stocks:
                stockslist.append([stock['code'], stock['type']])
            return stockslist
        except Exception:
            self._logger.error(self.__name__ + " mongodb get stocklist error.")

    def insertDailyData(self, data):
        if (self._datadb['CN_A_' + data["CODE"]].find({"DATE": data["DATE"]}).count() == 0):
            self._datadb['CN_A_' + data["CODE"]].insert(data)
            self._logger.info("{} insert data code: {} date: {} .".format(
                self.__name__, data["CODE"], data["DATE"]))
        else:
            return

    def getTime(self, code, today):
        enddate = "19920101"
        # cursor = self._datadb['CN_A_' + code].find(
        #     {"code": code}).sort([("date", -1)]).limit(1)
        cursor = self._datadb['datatime'].find({"code": code})
        for item in cursor:
            if item['date'] > enddate:
                enddate = item['date']
        if enddate == "19920101":
            self._datadb.datatime.insert({"code": code, "date": "19920101"})
        return enddate

    def getDailyData(self, code, date1=None, date2=None):
        # cursor = self._datadb.dailydata.find({"CODE": code}).sort([("DATE", -1)])
        cursor = self._datadb['CN_A_' + code].find(
            {"DATE": {'$gte': date1, '$lte': date2}}).sort([("DATE", 1)])  # 升序

        result = []
        for item in cursor:
            result.append(item)
        return result

    def updateTime(self, code, enddate):
        self._datadb.datatime.update(
            {"code": code}, {"$set": {"date": enddate}})
        self._logger.info("{} update datetime code: {} date: {} .".format(
            self.__name__, code, enddate))

    def cleanDB(self):
        self._datadb.datatime.remove({})
        self._datadb.drop()
