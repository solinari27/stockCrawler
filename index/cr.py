#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: cr.py
@time: 2019/04/11
"""
# 所谓CR指标指的就是能量指标，CR指标又叫中间意愿指标、价格动量指标，它和AR、BR指标有很多相似之处，
# 但更有自己独特的研判功能，是分析股市多空双方力量对比、把握买卖股票时机的一种中长期技术分析工具。
# 基本原理CR指标同AR、BR指标有很多相似的地方，如计算公式和研判法则等，
# 但它与AR、BR指标最大不同的地方在于理论的出发点有不同之处。CR指标的理论出发点是：中间价是股市最有代表性的价格。
# CR（N日）=P1÷P2×100
# P1=Σ（H－YM），表示N日以来多方力量的总和；P2=Σ（YM－L），表示N日以来空方力量的总和。H表示今日的最高价，L表示今日的最低价YM表示昨日（上一个交易日）的中间价。
# 经：

import sys
sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')


from base import Base

class CR_index():

    def __init__(self, code, start_date="1900-01-01", end_date="2020-01-01"):
        """
        default cal index from 1900-01-01
        """
        base = Base()
        self.datas = base.getData(
            code=code, start_date=start_date, end_date=end_date)

        self._index = 0
        self.period = 12

    @property
    def H(self):
        return self.datas[self._index]['TCLOSE']

    @property
    def L(self):
        return self.datas[self._index]['TCLOSE']

    @property
    def YM(self):
        return self.datas[self._index]['TCLOSE']

    def set_period(self, period):
        self.period = period


    def cal_index(self):
        total = len(self.datas)

        ret = []
        for index in range(0, total):
            for _i in range(0, index):
                print _i

        return ret


c = CR_index(code="600007")
c.set_period(period=12)
c.cal_index()
