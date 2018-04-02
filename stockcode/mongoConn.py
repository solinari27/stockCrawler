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
        self._logfile_handler = logging.FileHandler (filename)
        self._logfile_handler.setFormatter(formatter)
        self._logger.addHandler(self._logfile_handler)

        #init mongo connection
        self._dbConf = self._mongoConf['mongo']
        self._host = self._dbConf['host']
        self._port = int (self._dbConf['port'])
        self._username = self._dbConf['username']
        self._password = self._dbConf['password']

        try:
            self._conn = MongoClient(self._host, self._port)
            if not self._check_connected(self._conn):
                self._logger.error("mongodb connection failed.")
                sys.exit(1)

            # self.connected = self.db.authenticate (self._username, self._password)
            self._db = self._conn.stockinfo

        except Exceptions:
            self._logger.error("mongodb connection failed.")
            # sys.exit (1)

    def __del__(self):
        self._logger.removeHandler(self._logfile_handler)

    # 检查是否连接成功
    def _check_connected (self, conn):
        return conn.connected

    def createDB(self):
        return

    def maintain(self):
        return

    def cleanStock(self):
        self._db.stocklist.remove({})

    def insertStock(self, code, name):
        # self._db.stocklist.insert({"code": code, "name": name})    #完全清空后重新添加
        dbresult = self._db.stocklist.find({"code": code})
        result = {}
        have = False

        for i in dbresult:
            result['code'] = i['code']
            result['name'] = i['name']
            have = True

        if (not have):
            self._db.stocklist.insert({"code": code, "name": name})
        elif (result['name'] != name):
            self._db.stocklist.update({"code": code}, {"$set": {"name": name}})






