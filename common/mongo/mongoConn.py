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

    def __init__(self, confile=None):
        assert confile is not None
        #注意路径配置
        with open(confile) as f:
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
        self.__name__ = self._dbConf['name']
        self._host = self._dbConf['host']
        self._port = int (self._dbConf['port'])
        self._username = self._dbConf['username']
        self._password = self._dbConf['password']

        self._logger.info(self.__name__ + " mongo connection started.")

    def __del__(self):
        self._logger.info(self.__name__ + " mongo connection stopped.")
        self._conn.close()
        self._logger.removeHandler(self._logfile_handler)

    # 检查是否连接成功
    def _check_connected (self, conn):
        return conn.connected

