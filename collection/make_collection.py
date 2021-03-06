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

import copy
import numpy as np
import torch
import collection
from tools import data_show
from sk_utils.sklearn_lineregression import do_regression
import yaml

def del_useless_info(info_dict):
    del(info_dict['CODE'])
    del(info_dict['NAME'])
    del(info_dict['DATE'])
    return info_dict

def dict2list(_dict, suspension):
    key_list = ['LCLOSE', 'TOPEN', 'TCLOSE',
        'HIGH', 'LOW', 'MCAP', 'TCAP', 'CHG',
        'PCHG', 'TURNOVER', 'VATURNOVER', 'VOTURNOVER']
    _list = []
    # _list.append(_dict['LCLOSE'])
    # _list.append(_dict['TOPEN'])
    # _list.append(_dict['TCLOSE'])
    # _list.append(_dict['HIGH'])
    # _list.append(_dict['LOW'])
    # _list.append(_dict['MCAP'])
    # _list.append(_dict['TCAP'])
    # _list.append(_dict['CHG'])
    # _list.append(_dict['PCHG'])
    # _list.append(_dict['TURNOVER'])
    # _list.append(_dict['VATURNOVER'])
    # _list.append(_dict['VOTURNOVER'])

    for key in key_list:
        if type(_dict[key]) == float:
            _list.append(_dict[key])
        elif suspension:
            _list.append(0.0)
        else:
            return []
    return _list

def data2ndarray(dataset, suspension):
    _data = []
    for _item in dataset:
        try:
            _item = del_useless_info(_item)
        except KeyError:
            pass    # FIXME: ERROR in dict key
        _list = dict2list(_item, suspension)
        if not len(_list) == 0:
            _data.append(_list)
    _data = np.array(_data).T
    return _data

def make_training_tensor(code, start_date, end_date):
    with open("/home/solinari/workspace/stockCrawler/collection/conf/conf.yaml") as f:
        conf = yaml.load(f)
        c = collection.Collection()

        for result in c.getData(code=code, start_date=start_date, end_date=end_date):
            ret = do_regression(result, epochs=conf['epochs'], thres=conf['thres'],
                                algo=conf['algo']['name'], params=conf['algo'])
            for item in ret:
                w = item[0]
                b = item[1]
                dataset = result[item[2]: item[3]]
                dateperiod = len(dataset)
                # print item[2], item[3], dateperiod
                stand = conf['collection']
                # date > stand and weights > stand
                if dateperiod >= stand['dateperiod_up'] and w > stand['w_up']:
                    _data = data2ndarray(dataset=dataset)
                    # show = data_show.Plt()
                    # show.load_data(data=dataset)
                    # show.plot(w=w, b=b)
                    # time.sleep(1)
                    yield _data
                # date > stand and weights stand
                if dateperiod >= stand['dateperiod_down'] and w < stand['w_down']:
                    _data = data2ndarray(dataset=dataset)
                    # show = data_show.Plt()
                    # show.load_data(data=dataset)
                    # show.plot(w=w, b=b)
                    # time.sleep(1)
                    yield _data

def ascend_training_tensor(code, start_date, end_date):
    with open("/home/solinari/workspace/stockCrawler/collection/conf/conf.yaml") as f:
        conf = yaml.load(f)
        c = collection.Collection()

        # get indexs
        wr = c.get_index(code=code, index='WR', start_date=None, end_date=None, period=55)
        alldata = c.getAllData(code=code, start_date=start_date, end_date=end_date)

        for result in c.getData(code=code, start_date=start_date, end_date=end_date):
            ret = do_regression(result, epochs=conf['epochs'], thres=conf['thres'],
                                algo=conf['algo']['name'], params=conf['algo'])

            # print result
            for item in ret:
                w = item[0]
                b = item[1]
                dateperiod = item[3] - item[2]
                stand = conf['collection']

                if not (dateperiod >= stand['dateperiod_up'] and w > stand['w_up']):
                    break

                # ==============================================================================

                ascend_upper = stand['ascend_upper']
                ascend_point = item[2] - 1
                top_point = item[3] - 1
                ascend_date = result[ascend_point]['DATE']

                # cal befire days and after days
                # using BOLLING MACD EXPMA WR ...
                start_day = item[2]
                end_day = item[2]
                start_index = 0
                end_index = 0
                for start_index in range(0, len(alldata)):
                    if alldata[start_index]['DATE'] == ascend_date:
                        break
                for end_index in range(start_index, len(alldata)):
                    if alldata[end_index]['DATE'] == ascend_date:
                        break

                # ===============================================================================
                #rule: under start point 20% upper
                _topprice = ascend_upper * (result[top_point]['TCLOSE'] - result[ascend_point]['TOPEN']) + result[ascend_point]['TOPEN']
                #rule: below start point 10% lower

                # rule: W%R
                #locate
                _index = 0
                for _i in wr:
                    if _i['DATE'] == ascend_date:
                        break
                    _index += 1
                # lists ascend points

                WR_rules = conf['WR']
                for _i in range(_index, 0, -1):
                    if wr[_i]['W%R'] > WR_rules['ascend'] and alldata[start_index]['TCLOSE'] < _topprice:
                        break
                    start_day = wr[_i]['DATE']
                    start_index -= 1

                for _i in range(_index, len(wr)):
                    if wr[_i]['W%R'] > WR_rules['ascend'] and alldata[end_index]['TCLOSE'] < _topprice:
                        break
                    end_day = wr[_i]['DATE']
                    end_index += 1

                # =================================================================================
                #deep copy
                dataset = copy.deepcopy(alldata[start_index: end_index])
                _data = data2ndarray(dataset=dataset, suspension=stand['suspension'])
                yield _data

# for ret in make_training_tensor(code="600007", start_date="2015-01-01", end_date="2019-12-31"):
#     print torch.tensor(ret)

for ret in ascend_training_tensor(code="600000", start_date="2010-01-01", end_date="2019-12-31"):
    print torch.tensor(ret)
    # yield torch.tensor(ret)
