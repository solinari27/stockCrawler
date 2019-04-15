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
# 1、M=（2C+H+L）÷4
# 2、M=（C+H+L+O）÷4
# 3、M=（C+H+L）÷3
# 4、M=（H+L）÷2
# 式中，C为收盘价，H为最高价，L为最低价，O为开盘价。
# 经：
# FIXME: not correct CR index

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
        self.period = 10


    def set_period(self, period):
        self.period = period


    def cal_index(self):
        total = len(self.datas)

        ret = []
        for index in range(0, total):
            P1 = 0
            P2 = 0
            for _i in range(index - self.period + 1, index + 1):
                H = self.datas[_i]['HIGH']
                L = self.datas[_i]['LOW']

                if (_i > 0):
                    C = self.datas[_i-1]['TCLOSE']
                    _H = self.datas[_i-1]['HIGH']
                    _L = self.datas[_i-1]['LOW']
                    _O = self.datas[_i-1]['TOPEN']
                    YM = (2*C+_H+_L)/4
                    # M = (C + _H + _L + _O) / 4
                    # M = (C + _H + _L)/3
                    # M = (_H + _L) / 2
                else:
                    YM = (H + L) / 2

                # C = self.datas[_i]['TCLOSE']
                # O = self.datas[_i]['TOPEN']
                # M = (2 * C + H + L) / 4
                # M = (C + H + L + O) / 4
                # M = (C + H + L)/3
                # M = (H + L) / 2

                P1 += H - YM
                P2 += YM - L

            if P2 > 0:
                CR = P1 / P2 * 100
            else:
                CR = 100
            ret.append({'DATE': self.datas[index]['DATE'], 'CR': CR})

        return ret


c = CR_index(code="600007")
c.set_period(period=26)
print c.cal_index()
