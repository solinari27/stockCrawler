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
        
        self._keylist = {}
        self._keylist[u'\u6da8\u8dcc\u989d'] = 'CHG'
        self._keylist[u'\u80a1\u7968\u4ee3\u7801'] = 'CODE'
        self._keylist[u'\u603b\u5e02\u503c'] = 'TCAP'
        self._keylist[u'\u524d\u6536\u76d8'] = 'LCLOSE'
        self._keylist[u'\u6700\u9ad8\u4ef7'] = 'HIGH'
        self._keylist[u'\u6d41\u901a\u5e02\u503c'] = 'MCAP'
        self._keylist[u'\u6700\u4f4e\u4ef7'] = 'LOW'
        self._keylist[u'\u6210\u4ea4\u91cf'] = 'VOTURNOVER'
        self._keylist[u'\u65e5\u671f'] = 'DATE'
        self._keylist[u'\u6362\u624b\u7387'] = 'TURNOVER'
        self._keylist[u'\u540d\u79f0'] = 'NAME'
        self._keylist[u'\u6da8\u8dcc\u5e45'] = 'PCHG'
        self._keylist[u'\u5f00\u76d8\u4ef7'] = 'TOPEN'
        self._keylist[u'\u6536\u76d8\u4ef7'] = 'TCLOSE'
        self._keylist[u'\u6210\u4ea4\u91d1\u989d'] = 'VATURNOVER'

    def __del__(self):
        self._logger.warn("netease crawler stopped.")
        self._logger.removeHandler(self._logfile_handler)

    def _requestJson(self, type, code, startdate, enddate):
        def loadjson():
            cf = open(filename, 'r')
            results = []
            for x in csv.DictReader(cf):
                d = json.dumps(x, indent=4, separators=(',', ':'), ensure_ascii=False)  # ,sort_keys=True
                d2 = json.loads(d)
                d3 = {}
                for key in d2.keys():
                    try:
                        d3[self._keylist[key]] = float(d2[key])
                    except:
                        d3[self._keylist[key]] = d2[key]
                results.append(d3)
                # self._conn.insertDailyData(d2)
            cf.close()
            os.remove(filename)
            return results

        filename = 'Data/' + code + '.csv'
        url = "http://quotes.money.163.com/service/chddata.html?code=" + str(type) + str(code) + "&start=" + startdate + "&end=" + enddate + "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        try:
            response = requests.get(url = url)
        except:
            self._logger.error("netease crawler crawl daily data error code: " + code)
            return []

        # self._logger.info("netease crawler crawl daily data get response: ", response.status_code)
        self._logger.info ("netease crawler crawl daily data get response")

        with open(filename, 'w') as f:
            f.write(response.content.decode('gb2312').encode('utf-8'))
        f.close()
        time.sleep(1)
        return loadjson()

    def crawl(self):
        s = time.localtime(time.time())
        year = s.tm_year
        mon = s.tm_mon
        day = s.tm_mday
        #end date is today
        enddate = str(year) + '%02d' % (mon) + '%02d' % (day)

        stocks = self._conn.getStocks()
        for item in stocks:
            code = item[0]
            type = item[1]
            #get start date
            startdate = self._conn.getTime(code)
            results = []
            trytime = 0
            while ((results == []) and (trytime < self._repeatTime)):
                results = self._requestJson (type, code, startdate, enddate)
                trytime += 1
                time.sleep(10)
            if (results != []):
                for item in results:
                    self._conn.insertDailyData(item)
                self._conn.updateTime(code, enddate)
                self._logger.info("netease crawler crawl daily data code:" + str(code))
            time.sleep(20)

    def clean(self):
        self._conn.cleanDB()






