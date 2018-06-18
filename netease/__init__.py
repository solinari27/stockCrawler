#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: __init__.py.py 
@time: 2018/06/13 
"""  

import csv,json
cf = open('../Data/601857.csv','r')
for x in csv.DictReader(cf):
    d = json.dumps(x,indent=6,separators=(',',':'), ensure_ascii=False)   #,sort_keys=True
    print d
cf.close()