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
from cr import CR_index


# c = WR_index(code="600000")
# c.set_period(period=55)
# print c.cal_index()


c = CR_index(code="600007", end_date='1999-05-31')
print c.cal_index()
#consider python stockstats
#19990419   132.56
#19990420   133.8
#19990421   102.56
#19990422   93.86