#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: collection.py
@time: 2018/10/09
"""
import time

from common.mongo.sohuConn import SohuConn
from common.mongo.neteaseConn import NeteaseConn
from utils.common.switch import switch


class Collection(object):
    def __init__(self):
        self.sohuconn = SohuConn(
            "/home/solinari/workspace/stockCrawler/Conf/sohu.conf")
        self.neteaseconn = NeteaseConn(
            "/home/solinari/workspace/stockCrawler/Conf/netease.conf")

    def __del__(self):
        # self.sohuconn = None
        # self.neteaseconn = None
        pass

    def getToday(self):
        s = time.localtime(time.time())
        year = s.tm_year
        mon = s.tm_mon
        day = s.tm_mday
        return year, mon, day

    def getData(self, code, start_date, end_date):
        assert code is not None
        assert start_date is not None
        assert end_date is not None

        netease_result = self.neteaseconn.getDailyData(
            code=str(code), date1=start_date, date2=end_date)
        sohu_result = self.sohuconn.getDailyData(
            code=str(code), date1=start_date, date2=end_date)
        # assert (len(netease_result) == len(sohu_result))

        result = []
        name = None
        for index, sohu_item in enumerate(sohu_result):
            netease_item = netease_result[index]
            if name is None:
                name = netease_item['NAME']

            if netease_item['NAME'] != name and name is not None:
                yield result
                result = []

            item = {}

            for key in netease_item.keys():
                for case in switch(key):
                    # base info
                    if case('HIGH'):
                        item[key] = netease_item[key]
                        break
                    if case('LOW'):
                        item[key] = netease_item[key]
                        break
                    if case('CODE'):
                        item[key] = netease_item[key]
                        break
                    if case('DATE'):
                        item[key] = netease_item[key]
                        break
                    if case('NAME'):
                        item[key] = netease_item[key]
                        break

                # drop this
                    if case('_id'):
                        break

                # advantage info
                    if case('TCAP'):
                        item[key] = netease_item[key]
                        break
                    if case('MCAP'):
                        item[key] = netease_item[key]
                        break

                    if case('CHG'):
                        item[key] = netease_item[key]
                        break
                    if case('PCHG'):
                        item[key] = netease_item[key]
                        break

                    if case('LCLOSE'):
                        item[key] = netease_item[key]
                        break
                    if case('TOPEN'):
                        item[key] = netease_item[key]
                        break
                    if case('TCLOSE'):
                        item[key] = netease_item[key]
                        break
                    if case('VATURNOVER'):
                        item[key] = netease_item[key]
                        break

                    if case('VOTURNOVER'):
                        item[key] = netease_item[key]
                        break
                    if case('TURNOVER'):
                        item[key] = netease_item[key]
                        break
                    if case():  # default, could also just omit condition or 'if True'
                        pass
                        # No need to break here, it'll stop anyway
            result.append(item)
        yield result
