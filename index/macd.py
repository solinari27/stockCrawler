#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: macd.py
@time: 2019/04/28
"""
# 加权平均指数（DI）=（当日最高指数 当日收盘指数2倍的当日最低指数）
# 十二日平滑系数（L12）=2/（12+1）=0.1538
# 二十六日平滑系数（L26）=2/（26+1）=0.0741
# 十二日指数平均值（12日EMA）=L12×当日收盘指数+11/（12+1）×昨日的12日EMA
# 二十六日指数平均值（26日EMA）=L26×当日收盘指数+25/（26+1）×昨日的26日EMA
# 差离率（DIFF）=12日EMA-26日EMA
# DIFF平均值9日（DEA）=前一日DEA× 8/10+今日DIF× 2/10
# 柱状值（BAR）=DIFF-DEA
# MACD=（当日的DIF-昨日的DIF）× 0.2 + 昨日的MACD × 0.8

import sys
sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')


from base import Base

class MACD_index():

    def __init__(self, code, start_date="1900-01-01", end_date="2020-01-01"):
        """
        default cal index from 1900-01-01
        """
        base = Base()
        start_date="1900-01-01" #must from beginning
        self.datas = base.getData(
            code=code, start_date=start_date, end_date=end_date)

        self.exa12 = None
        self.ema26 = None
