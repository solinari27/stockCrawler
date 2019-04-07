#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: base.py
@time: 2018/10/09
"""

# W%R指标即威廉指标，主要是通过分析一段时间内股价最高价、最低价和收盘价之间的关系，
# 来判断股市的超买超卖现象，预测股价中短期的走势。它主要是利用振荡点来反映市场的超买超卖行为，
# 分析多空双方力量的对比，从而提出有效的信号来研判市场中短期行为的走势。
# W%R=(Hn—C)÷(Hn—Ln)×100
# 其中：C为计算日的收盘价，Ln为N周期内的最低价，Hn为N周期内的最高价，公式中的N为选定的计算时间参数，一般为4或14。
# 以计算周期为14日为例，其计算过程如下：
# W%R(14日)=(H14—C)÷(H14—L14)×100
# 其中，C为第14天的收盘价，H14为14日内的最高价，L14为14日内的最低价。


import sys
sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')

from base import Base

class WR_index():

    def __init__(self, code, start_date="1900-01-01", end_date="2019-01-01"):
        """
        default cal index from 1900-01-01
        """
        base = Base()
        self.datas = base.getData(
            code=code, start_date=start_date, end_date=end_date)
        self._index = 0

    @property
    def C(self):
        return self.datas[self._index]['TCLOSE']

    @property
    def Hn(self):
        Hn = self.datas[self._index]['HIGH']

    @property
    def Ln(self):
        Hn = self.datas[self._index]['LOW']

    def cal_index(self):
        pass


c = WR_index(code="600004")
c.cal_index()
print c.C, c.Hn, c.Ln
