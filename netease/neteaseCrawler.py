#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: neteaseCrawler.py
@time: 2018/06/13
"""

import json
import csv
import os
import requests
import logging
import time

from Tools.swtich import switch
import mongoConn


class neteaseCrawler():
    def __init__(self):
        with open('Conf/netease.conf') as f:
            self._liangyeeConf = json.load(f)

        # init logging:
        self._logConf = self._liangyeeConf['logging']
        self._name = self._logConf['name'] + " crawler"
        self._logger = logging.getLogger(self._name)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        date_str = time.strftime('%Y_%m_%d', time.gmtime())
        filename = self._logConf['logpath'] + "/crawler_" + date_str + ".log"
        self._logfile_handler = logging.FileHandler(filename)
        self._logfile_handler.setFormatter(formatter)
        self._logger.addHandler(self._logfile_handler)

        # default log level
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

        self._logger.warn("netease crawler started.")

        #init other：
        self._conf = self._liangyeeConf['crawler']
        self._debug = self._conf['debug']
        self._repeatTime = self._conf['requestrepeat']
        self._conn = mongoConn.mongoConn()
        self._logger.debug("netease crawler init mongo connection.")

    def __del__(self):
        self._logger.warn("netease crawler stopped.")
        self._logger.removeHandler(self._logfile_handler)

    def requestJson(self, code):
        def loadjson():
            cf = open(filename, 'r')
            results = []
            for x in csv.DictReader(cf):
                d = json.dumps(x, indent=4, separators=(',', ':'), ensure_ascii=False)  # ,sort_keys=True
                results.append(d)
            cf.close()
            return results

        filename = 'Data/' + code + '.csv'
        url = "http://quotes.money.163.com/service/chddata.html?code=0" + code + "&start=20071105&end=20150618&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        response = requests.get(url = url)
        with open(filename, 'w') as f:
            f.write(response.content.decode('gb2312').encode('utf-8'))
        f.close()
        return loadjson()
        os.remove(filename)

    def crawl(self):
        stocks = self._conn.getStocks()
        for item in stocks:
            code = item[0]
            type = item[1]
            print code, type





