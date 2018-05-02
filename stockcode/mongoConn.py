#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: mongoConn.py 
@time: 2018/03/10 
"""  

from pymongo import MongoClient
import json
import time
import logging
import sys

class mongoConn():

    def __init__(self):
        #注意路径配置
        with open('Conf/crawler.conf') as f:
            self._mongoConf = json.load(f)

        #init logging:
        self._logConf = self._mongoConf['logging']
        self._name = self._logConf['name']
        self._logger = logging.getLogger(self._name)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        date_str = time.strftime('%Y_%m_%d', time.gmtime ())
        filename = self._logConf['logpath'] + "/crawler_" + date_str + ".log"
        self._logfile_handler = logging.FileHandler(filename)
        self._logfile_handler.setFormatter(formatter)
        self._logger.addHandler(self._logfile_handler)

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
            self._db = self._conn.stockinfo

        except Exception:
            self._logger.error("mongodb connection failed.")
            # sys.exit (1)

    def __del__(self):
        self._conn.close()
        self._logger.warn("stockcode crawler stopped.")
        self._logger.removeHandler(self._logfile_handler)

    # 检查是否连接成功
    def _check_connected (self, conn):
        return conn.connected

    def cleanStock(self):
        self._logger.warn("stockcode crawler clean mongodb.")
        self._db.stocklist.remove({})

    def insertStock(self, code, name):
        # self._logger.debug("stockcode crawler insert mongodb stock code: " + code)
        # self._db.stocklist.insert({"code": code, "name": name, "updatetime": None})    #完全清空后重新添加

        dbresult = self._db.stocklist.find({"code": code})
        result = {}
        have = False
        updatetime = None

        for i in dbresult:
            result['code'] = i['code']
            result['name'] = i['name']
            updatetime = i['updatetime']
            have = True

        if (not have):
            self._logger.info("stockcode crawler insert mongodb stock code: " + code)
            self._db.stocklist.insert({"code": code, "name": name, "updatetime": None})
        elif (result['name'] != name):
            self._logger.info("stockcode crawler insert mongodb stock code: " + code)
            self._db.stocklist.update({"code": code}, {"$set": {"name": name, "updatetime": updatetime}})






