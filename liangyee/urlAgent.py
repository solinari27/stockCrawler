#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: urlAgent.py 
@time: 2018/02/25 
"""  

import time

class urlAgent():
    """
    give liangyee url
    """

    def __init__(self, *args, **kwargs):
        self._userkey = None
        self._timesLimit = 0
        self._userKeyTimes = {}

    def setUserKey(self, key):
        self._userkey = key
        if key != None:
            self._userKeyTimes[key] = 0  # url 使用次数 liangyee数据限制200次访问

    def getUserKey(self):
        return self._userkey

    def getTimes(self):
        return self._timesLimit

    def setTimesLimit(self, timeslimit):
        self._timesLimit = timeslimit

    def _addKeyTime(self):
        self._userKeyTimes[self._userkey] += 1
        return self._userKeyTimes[self._userkey]

    def _getSymbolString(self, stocks):
        symbols = ''
        for stock in stocks:
            if (symbols == ''):
                symbols = str(stock)
            else:
                symbols += ',' + str(stock)
        return symbols

    #params:
    #stock: stock id
    #Day: timestamp of the YY-MM-DD
    def getDailyKUrl(self, stock, startDay, endDay):
        #check params ...
        if self._addKeyTime() < self._timesLimit:
            startDayStr = time.strftime('%Y-%m-%d', startDay)
            endDayStr = time.strftime('%Y-%m-%d', endDay)
            url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/getDailyKBar?userKey=' + self._userkey + r'&startDate=' + startDayStr + r'&symbol=' + str(stock) + '&endDate=' + endDayStr + r'&type=0'
            return url
        else:
            return ""

    def get5MinKUrl(self, stock):
        if self._addKeyTime() < self._timesLimit:
            url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/get5MinK?userKey=' + self._userkey + r'&symbol=' + str(stock) + r'&type=0'
            return url
        else:
            return ""

    def getMarketDataUrl(self, stocks):
        if self._addKeyTime() < self._timesLimit:
            # this stock must be tuples
            symbolist = self._getSymbolString(stocks)
            url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/GetMarketData?userKey=' + self._userkey + r'&symbol='+ symbolist + r'&type=0'
            return url
        else:
            return ""