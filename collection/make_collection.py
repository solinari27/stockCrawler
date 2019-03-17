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

import collection
from tools import data_show
from sk_utils.sklearn_lineregression import do_regression
import yaml

def del_useless_info(info_dict):
    del(info_dict['CODE'])
    del(info_dict['NAME'])
    del(info_dict['DATE'])
    return info_dict

def dict2array():
    pass

with open("/home/solinari/workspace/stockCrawler/collection/conf/conf.yaml") as f:
    conf = yaml.load(f)
    c = collection.Collection()

    for result in c.getData(code="600007", start_date="2017-01-01", end_date="2019-12-31"):
        ret = do_regression(result, epochs=conf['epochs'], thres=conf['thres'],
                            algo=conf['algo']['name'], params=conf['algo'])
        for item in ret:
            w = item[0]
            b = item[1]
            dataset = result[item[2]: item[3]]
            dateperiod = len(dataset)
            stand = conf['collection']
            if dateperiod >= stand['dateperiod_up'] and w >= stand['w_up']:
                for _item in dataset:
                    _item = del_useless_info(_item)
                    print _item
                # show = data_show.Plt()
                # show.load_data(data=dataset)
                # show.plot(w=w, b=b)
                # time.sleep(1)
            if dateperiod >= stand['dateperiod_down'] and w <= stand['w_down']:
                print dataset
                # show = data_show.Plt()
                # show.load_data(data=dataset)
                # show.plot(w=w, b=b)
                # time.sleep(1)
                pass
