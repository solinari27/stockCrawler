#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: crawler.py 
@time: 2018/08/29 
"""  

import sys
import os

sys.path.append(os.getcwd())
os.system("scrapy runspider crawler/crawler/spiders/sohuCrawler.py --loglevel ERROR")

