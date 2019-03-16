#!usr/bin/env python
# -*- coding:utf-8 _*-

"""
@author: solinari
@file: make_collection.py
@time: 2019/03/14
"""
import sys
import time

sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')

from collection import collection
from collection.tools import data_show
from sk_utils.sklearn_lineregression import do_regression


c = collection.Collection()

for result in c.getData(code="600000", start_date="2017-01-01", end_date="2018-12-31"):
    ret = do_regression(result, epochs=10000, thres=10,
                        DBSCAN_eps=3, DBSCAN_minsamples=4)
    for item in ret:
        w = item[0]
        b = item[1]
        dataset = result[item[2]: item[3]]
        show = data_show.Plt()
        show.load_data(data=dataset)
        show.plot(w=w, b=b)
        time.sleep(1)
