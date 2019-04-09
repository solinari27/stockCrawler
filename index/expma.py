#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: expma.py
@time: 2019/04/08
"""
# EXPMA指标简称EMA，中文名字指数平均数指标，一种趋向类指标，从统计学的观点来看，
# 只有把移动平均线（MA)绘制在价格时间跨度的中点，才能够正确地反映价格的运动趋势，
# 但这会使信号在时间上滞后，而EXPMA指标是对移动平均线的弥补，
# EXPMA指标由于其计算公式中着重考虑了价格当天（当期）行情的权重，
# 因此在使用中可克服MACD其他指标信号对于价格走势的滞后性。
# 同时也在一定程度中消除了DMA指标在某些时候对于价格走势所产生的信号提前性，是一个非常有效的分析指标。
# EXPMA=（当日或当期收盘价－上一日或上期EXPMA）/N+上一日或上期EXPMA，其中，首次上期EXPMA值为上一期收盘价，N为天数。
# 经：

import sys
sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')


from base import Base

class EXPMA_index():

    def __init__(self, code, start_date="1900-01-01", end_date="2020-01-01"):
        """
        default cal index from 1900-01-01
        """
        base = Base()
        self.datas = base.getData(
            code=code, start_date=start_date, end_date=end_date)

        self._index = 0
        self._last_expma = 0
        self.period = 14

        for item in self.datas:
            print item


    def set_period(self, period):
        self.period = period


    def cal_index(self):
        pass


c = EXPMA_index(code="600007")
