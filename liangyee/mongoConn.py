#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: mongoConn.py 
@time: 2018/02/25 
"""  

from pymongo import MongoClient
import sys
import json
import time
import logging

from Tools.swtich import switch

class mongoConn():

    def __init__(self):
        #注意路径配置
        with open('Conf/liangyee.conf') as f:
            self._mongoConf = json.load(f)

        #init logging:
        self._logConf = self._mongoConf['logging']
        self._name = self._logConf['name'] + " mongodb"
        self._logger = logging.getLogger(self._name)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        date_str = time.strftime('%Y_%m_%d', time.gmtime ())
        filename = self._logConf['logpath'] + "/crawler_" + date_str + ".log"
        self._logfile_handler = logging.FileHandler (filename)
        self._logfile_handler.setFormatter(formatter)
        self._logger.addHandler(self._logfile_handler)

        # set logging level
        for case in switch(self._logConf['level']):
            if case('NOTSET'):
                self._logger.setLevel(logging.NOTSET)
                break
            if case('DEBUG'):
                self._logger.setLevel(logging.DEBUG)
                break
            if case('INFO'):
                self._logger.setLevel(logging.INFO)
                break
            if case('WARN'):
                self._logger.setLevel(logging.WARN)
                break
            if case('ERROR'):
                self._logger.setLevel(logging.ERROR)
                break
            if case('FATAL'):
                self._logger.setLevel(logging.FATAL)
                break
            if case():  # default, could also just omit condition or 'if True'
                self._logger.setLevel(logging.WARN)
                # No need to break here, it'll stop anyway

        #init mongo connection
        self._dbConf = self._mongoConf['mongo']
        self._host = self._dbConf['host']
        self._port = int (self._dbConf['port'])
        self._username = self._dbConf['username']
        self._password = self._dbConf['password']

        self._logger.warn("stockcode crawler started.")

        try:
            self._conn = MongoClient(self._host, self._port)
            if not self._check_connected(self._conn):
                self._logger.error("mongodb connection failed.")
                sys.exit(1)

            # self.connected = self.db.authenticate (self._username, self._password)
            self._stockdb = self._conn.stockinfo
            self._datadb = self._conn.stockdata

        except Exception:
            self._logger.error("mongodb connection failed.")
            # sys.exit (1)

    def __del__(self):
        self._logger.warn("stockcode crawler stopped.")
        self._logger.removeHandler(self._logfile_handler)
        self._conn.close()

    # 检查是否连接成功
    def _check_connected (self, conn):
        return conn.connected

    def getStocks(self):
        stockslist = []
        try:
            stocks = self._stockdb.stocklist.find()
            for stock in stocks:
                stockslist.append([stock['code'] , stock['updatetime']])
            return stockslist
        except Exception:
            self._logger.error("mongodb get stocklist error.")

    def updateTime(self, code, date):
        data = {}
        un_time = time.mktime(date)
        data['updatetime'] = un_time
        self._stockdb.stocklist.update({"code": code}, {"$set": data})
        return

    def insertDailyKData(self, data):
        self._datadb.dailyKData.insert(data)

    def insert5MinKData(self, data):
        self._datadb.fiveMinKData.insert(data)

    def insertMarketData(self, data):
        self._datadb.marketData.insert(data)

    def getUserID(self, id, times, debug):
        #TODO update time
        key = None
        timelimit = 0

        try:
            if (id != None):
                data = {}
                data ['times'] = times;
                self._stockdb.liangyeeuser.update({"key": id}, {"$set": data})
            nextid = list(self._stockdb.liangyeeuser.find({"debug": debug, "times": 0}))[0]
            key = nextid['key']
            timelimit = nextid['timelimit']
        except Exception:
            return None, 0

        return key, timelimit









