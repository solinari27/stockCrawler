#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: urltools.py 
@time: 2018/08/29 
"""  

def get_url(code=None, start=None, end=None):
    url = "http://q.stock.sohu.com/hisHq?code=cn_" + code + "&start=20130930&end=20131231&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp"
    return url