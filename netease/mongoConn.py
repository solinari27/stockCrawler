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
            self._conn = MongoClient(self._host, self._port)
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



