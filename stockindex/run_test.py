#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: run_test.py
@time: 2018/10/09
"""
import sys
sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')
from stockindex.wr import WR_index


c = WR_index(code="600000")
c.set_period(period=55)
print c.cal_index()
