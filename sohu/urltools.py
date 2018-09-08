#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: urltools.py 
@time: 2018/08/29 
"""  

def get_url(code=None, start=None, end=None):
    url = "http://q.stock.sohu.com/hisHq?code=cn_" + code + "&start=" + start + "&end=" + end + "&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp"
    return url