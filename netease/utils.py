# -*- coding: utf-8 -*-
# @Author  : Solinari
# @Email   : 
# @File    : utils.py
# @Software: PyCharm
# @Time    : 2018/12/09

def get_url(type=None, code=None, startdate=None, enddate=None):
    url = "http://quotes.money.163.com/service/chddata.html?code=" + str(type) + str(
        code) + "&start=" + startdate + "&end=" + enddate + "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    return url