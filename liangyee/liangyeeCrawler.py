#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: liangyeeCrawler.py 
@time: 2018/02/25 
"""  

import requests
import json
import logging
import time
import random
import mongoConn
import os

import urlAgent

class liangyeeCrawler():

    def __init__(self):
        with open('Conf/liangyee.conf') as f:
            self._liangyeeConf = json.load(f)

        # init logging:
        self._logConf = self._liangyeeConf['logging']
        self._name = self._logConf['name']
        self._logger = logging.getLogger(self._name)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        date_str = time.strftime('%Y_%m_%d', time.gmtime())
        filename = self._logConf['logpath'] + "/crawler_" + date_str + ".log"
        self._logfile_handler = logging.FileHandler(filename)
        self._logfile_handler.setFormatter(formatter)
        self._logger.addHandler(self._logfile_handler)
        # default log level
        self._logger.setLevel(logging.DEBUG)

        self._logger.warn("liangyee crawler started.")
        self._flushlog()

        #init other：
        self._conf = self._liangyeeConf['crawler']
        self._debug = self._conf['debug']
        self._repeatTime = self._conf['requestrepeat']
        self._agent = urlAgent.urlAgent()
        self._conn = mongoConn.mongoConn()
        self._logger.debug("liangyee crawler init mongo connection.")
        self._flushlog()

        key, timelimit = self._getNextID()
        if (key != None):
            self._setID(key, timelimit)
            self._logger.debug("liangyee crawler set userkey: " + key + ".")
            self._logger.debug("liangyee crawler set time limit: " + str(timelimit) + ".")
            self._flushlog()
        else:
            self._setID(None, 0)

    def __del__(self):
        self._logger.warn("liangyee crawler stopped.")
        self._logger.removeHandler(self._logfile_handler)

    def _flushlog(self):
        if (self._logger != None):
            self._logger.removeHandler(self._logfile_handler)
        self._logger.addHandler(self._logfile_handler)

    def _setID(self, userKey, timelimit):
        self._agent.setUserKey(userKey)
        self._logger.debug("liangyee crawler set userkey: " + str(userKey) + " .")
        self._agent.setTimesLimit(timelimit)
        self._logger.debug("liangyee crawler set time limit: " + str(timelimit) + " .")
        self._flushlog()

    def _getNextID(self):
        return self._conn.getUserID(self._agent.getUserKey(), self._agent.getTimes(), self._debug)

    def _requestJson(self, url):
        for i in range (self._repeatTime):
            try:
                response = requests.get(url=url)
                content = json.loads(response.content)
                return content
            except requests.exceptions.ConnectionError:
                self._logger.error("liangyee crawler request url " + url + " connection error.")
                self._flushlog()
            except requests.exceptions.ChunkedEncodingError:
                self._logger.error("liangyee crawler request url " + url + " chunked encoding error.")
                self._flushlog()
            except:
                self._logger.error("liangyee crawler request url " + url + " other error.")
                self._flushlog()
        return {}

    def _getstockslist(self):
        return self._conn.getStocks()

    def _updateDataTime(self, code, date):
        self._conn.updateTime(code, date)

    def getDailyKData(self, stock, startDay, endDay):
        url = self._agent.getDailyKUrl(stock, startDay, endDay)
        if url != "":
            return self._requestJson(url=url)['result']
        else:
            userKey, timelimit = self._getNextID()
            if (userKey != None):
                self._setID(userKey, timelimit)
                return self.getDailyKData(stock, startDay, endDay)
            else:
                self._logger.warn("liangyee crawler getDailyKData timelimit.")
                self._flushlog()
                return None

    def get5MinKData(self, stock):
        url = self._agent.get5MinKUrl(stock)
        if url != "":
            return self._requestJson(url=url)['result']
        else:
            userKey, timelimit = self._getNextID()
            if (userKey != None):
                self._setID(userKey, timelimit)
                return self.get5MinKData(stock)
            else:
                self._logger.warn("liangyee crawler get5MinKData timelimit.")
                self._flushlog()
                return None

    def getMarketData(self, stocks):
        url = self._agent.getMarketDataUrl(stocks)
        if url != "":
            return self._requestJson(url=url)['result']
        else:
            userKey, timelimit = self._getNextID()
            if (userKey != None):
                self._setID(userKey, timelimit)
                return self.getMarketData(stocks)
            else:
                self._logger.warn("liangyee crawler getMarketData timelimit.")
                self._flushlog()
                return None

    def _recordDailyKData(self, data):
        self._conn.insertDailyKData(data)

    def _record5MinyKData(self, data):
        self._conn.insert5MinKData(data)

    def _recordMarketData(self, data):
        self._conn.insertMarketData(data)

    def crawlliangyee(self):
        def date_cmp(date1, date2):
            if ((date1.tm_year == date2.tm_year) and (date1.tm_mon == date2.tm_mon) and (date1.tm_mday == date2.tm_mday)):
                return True
            else:
                return False

        def parseDailyKData(code, kdata):
            for i in kdata:
                info = i.split(',')
                date = info[0]
                start = info[1]
                high = info[2]
                low = info[3]
                end = info[4]
                count = info[5]
                # print date, start, high, low, end, count
                data = {}
                data['code'] = code
                data['date'] = date
                data['start'] = start
                data['high'] = high
                data['low'] = low
                data['end'] = end
                data['count'] = count
                self._recordDailyKData(data)
            time.sleep(random.randint(3, 5))

        def parse5MinKData(code, kdata):
            for i in kdata:
                info = i.split(',')
                infolv2 = info[0].split(' ')
                date = infolv2[0]
                datatime = infolv2[1]
                start = info[1]
                high = info[2]
                low = info[3]
                end = info[4]
                count = info[5]
                # print date, time, start, high, low, end, count
                data = {}
                data['code'] = code
                data['date'] = date
                data['time'] = datatime
                data['start'] = start
                data['high'] = high
                data['low'] = low
                data['end'] = end
                data['count'] = count
                self._record5MinyKData(data)
            time.sleep(random.randint(3, 6))

        def parseMarketData(code, marketdata):
            for i in marketdata:
                info = i.split(',')
                name = info[0]
                today_start_price = info[1]
                yesterday_end_price = info[2]
                now_price = info[3]
                floating = info[4]
                floating_rate = info[5]
                highest_price = info[6]
                lowest_price = info[7]
                deal_count = info[8]
                deal_count_price = info[9]
                buy1_count = info[10]
                buy1_price = info[11]
                buy2_count = info[12]
                buy2_price = info[13]
                buy3_count = info[14]
                buy3_price = info[15]
                buy4_count = info[16]
                buy4_price = info[17]
                buy5_count = info[18]
                buy5_price = info[19]
                sell1_count = info[20]
                sell1_price = info[21]
                sell2_count = info[22]
                sell2_price = info[23]
                sell3_count = info[24]
                sell3_price = info[25]
                sell4_count = info[26]
                sell4_price = info[27]
                sell5_count = info[28]
                sell5_price = info[29]
                marketdataDateTime = info[30]
                # print name,today_start_price,yesterday_end_price,now_price,floating,floating_rate,highest_price,lowest_price,deal_count,deal_count_price,
                # buy1_count,buy1_price,buy2_count,buy2_price,buy3_count,buy3_price,buy4_count,buy4_price,buy5_count,buy5_price,
                # sell1_count,sell1_price,sell2_count,sell2_price,sell3_count,sell3_price,sell4_count,sell4_price,sell5_count,sell5_price,marketdataDateTime
                data = {}
                data['code'] = code
                data['name'] = name
                data['today_start_price'] = today_start_price
                data['yesterday_end_price'] = yesterday_end_price
                data['now_price'] = now_price
                data['floating'] = floating
                data['floating_rate'] = floating_rate
                data['highest_price'] = highest_price
                data['lowest_price'] = lowest_price
                data['deal_count'] = deal_count
                data['deal_count_price'] = deal_count_price
                data['marketdataDateTime'] = marketdataDateTime

                data['buy1_count'] = buy1_count
                data['buy1_price'] = buy1_price
                data['buy2_count'] = buy2_count
                data['buy2_price'] = buy2_price
                data['buy3_count'] = buy3_count
                data['buy3_price'] = buy3_price
                data['buy4_count'] = buy4_count
                data['buy4_price'] = buy4_price
                data['buy5_count'] = buy5_count
                data['buy5_price'] = buy5_price

                data['sell1_count'] = sell1_count
                data['sell1_price'] = sell1_price
                data['sell2_count'] = sell2_count
                data['sell2_price'] = sell2_price
                data['sell3_count'] = sell3_count
                data['sell3_price'] = sell3_price
                data['sell4_count'] = sell4_count
                data['sell4_price'] = sell4_price
                data['sell5_count'] = sell5_count
                data['sell5_price'] = sell5_price
                self._recordMarketData(data)
            time.sleep(random.randint(5, 8))

        stockcodelist = self._getstockslist()
        for code in stockcodelist:
            # 0 for stockcode 1 for updatetime
            if code[1] == None:
                lastDate = time.strptime("2000:01:01", "%Y:%m:%d")
            else:
                time_local = time.localtime(code[1])
                lastDate = time_local
            now = time.gmtime()
            nowDate = time.strptime(str(now.tm_year) + ":" + str(now.tm_mon) + ":" + str(now.tm_mday), "%Y:%m:%d")
            print "code: ", code[0], "last: ", lastDate, "| now: ", nowDate
            if not date_cmp(nowDate, lastDate):
                try:
                    kData = self.getDailyKData(code[0], lastDate, nowDate)
                    parseDailyKData(code[0], kData)

                    fiveMinData = self.get5MinKData(code[0])
                    parse5MinKData(code[0], fiveMinData)

                    marketData = self.getMarketData([code[0]])
                    parseMarketData(code[0], marketData)

                    self._updateDataTime(code[0], nowDate)
                except Exception:
                    self._logger.error("liangyee crawler crawl error stock code:" + code[0])
                    self._flushlog()
                    break
                time.sleep(random.randint(5, 10))




