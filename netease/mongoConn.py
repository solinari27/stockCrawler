#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: mongoConn.py 
@time: 2018/06/13 
"""  

from pymongo import MongoClient
import sys
import json
import time
import logging
import urllib

from Tools.swtich import switch

class mongoConn():

    def __init__(self):
        #注意路径配置
        with open('Conf/netease.conf') as f:
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

        self._logger.warn("netease crawler mongo connection started.")

        try:
            username = urllib.quote_plus(self._username)
            password = urllib.quote_plus(self._password)
            self._conn = MongoClient('mongodb://%s:%s@' + self._host % (username, password))
            # self._conn = MongoClient(self._host, self._port)
            if not self._check_connected(self._conn):
                self._logger.error("netease crawler mongo connection failed.")
                sys.exit(1)

            # self.connected = self.db.authenticate (self._username, self._password)
            self._stockdb = self._conn.stockinfo
            self._datadb = self._conn.neteasestockdata

        except Exception:
            self._logger.error("netease crawler mongo connection failed.")
            # sys.exit (1)

    def __del__(self):
        self._logger.warn("netease crawler mongo connection stopped.")
        self._conn.close()
        self._logger.removeHandler(self._logfile_handler)

    # 检查是否连接成功
    def _check_connected (self, conn):
        return conn.connected

    def getStocks(self):
        stockslist = []
        try:
            stocks = self._stockdb.stocklist.find()
            for stock in stocks:
                stockslist.append([stock['code'], stock['type']])
            return stockslist
        except Exception:
            self._logger.error("netease crawler mongodb get stocklist error.")

    def insertDailyData(self, data):
        if (self._datadb.dailydata.find({"CODE": data["CODE"], "DATE": data["DATE"]}).count() == 0):
            self._datadb.dailydata.insert(data)
            self._logger.info("netease crawler insert data code: " + data["CODE"] + " date: " + data["DATE"] + ".")
        else:
            return
    
    def getTime(self, code):
        # startdate = "19920101"
        # enddate = startdate
        # date = self._datadb.datatime.find({"code": code})
        # if date.count() == 0:
        #     self._datadb.datatime.insert({"code": code, "date": startdate})
        #     return startdate
        # else:
        #     for i in date:
        #         if (i["date"]>enddate):
        #             enddate = i["date"]
        #     return enddate
        enddate = "19920101"
        cursor = self._datadb.datatime.find({"code": code}).sort([("date", -1)]).limit(1)
        for item in cursor:
            enddate = item['date']
        if enddate == "19920101":
            self._datadb.datatime.insert({"code": code, "date": "19920101"})
        return enddate
        
    def updateTime(self, code, enddate):
        self._datadb.datatime.update({"code": code}, {"$set":{"date":enddate}})
        self._logger.info("netease crawler update datetime code: " + code + " date: " + enddate + ".")

    def cleanDB(self):
        self._datadb.datatime.remove({})
        self._datadb.dailydata.remove({})

