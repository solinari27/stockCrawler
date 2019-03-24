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

import numpy as np
import collection
from tools import data_show
from sk_utils.sklearn_lineregression import do_regression
import yaml

def del_useless_info(info_dict):
    del(info_dict['CODE'])
    del(info_dict['NAME'])
    del(info_dict['DATE'])
    return info_dict

def dict2list(_dict):
    _list = []
    _list.append(_dict['LCLOSE'])
    _list.append(_dict['TOPEN'])
    _list.append(_dict['TCLOSE'])
    _list.append(_dict['HIGH'])
    _list.append(_dict['LOW'])
    _list.append(_dict['MCAP'])
    _list.append(_dict['TCAP'])
    _list.append(_dict['CHG'])
    _list.append(_dict['PCHG'])
    _list.append(_dict['TURNOVER'])
    _list.append(_dict['VATURNOVER'])
    _list.append(_dict['VOTURNOVER'])
    return _list

def data2ndarray(dataset):
    _data = []
    for _item in dataset:
        _item = del_useless_info(_item)
        _data.append(dict2list(_item))
    _data = np.array(_data).T
    return _data

def make():
    with open("/home/solinari/workspace/stockCrawler/collection/conf/conf.yaml") as f:
        conf = yaml.load(f)
        c = collection.Collection()

        for result in c.getData(code="600007", start_date="2015-01-01", end_date="2019-12-31"):
            ret = do_regression(result, epochs=conf['epochs'], thres=conf['thres'],
                                algo=conf['algo']['name'], params=conf['algo'])
            for item in ret:
                w = item[0]
                b = item[1]
                dataset = result[item[2]: item[3]]
                dateperiod = len(dataset)
                stand = conf['collection']
                if dateperiod >= stand['dateperiod_up'] and w > stand['w_up']:
                    _data = data2ndarray(dataset=dataset)
                    print _data
                    # show = data_show.Plt()
                    # show.load_data(data=dataset)
                    # show.plot(w=w, b=b)
                    # time.sleep(1)
                if dateperiod >= stand['dateperiod_down'] and w < stand['w_down']:
                    _data = data2ndarray(dataset=dataset)
                    print _data
                    # show = data_show.Plt()
                    # show.load_data(data=dataset)
                    # show.plot(w=w, b=b)
                    # time.sleep(1)

make()
