#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: sohuCrawler.py 
@time: 2018/08/28 
"""  
import scrapy

class Sohu_crawler(scrapy.Spider):
    name = "SohuCrawler"
    start_urls = ['http://q.stock.sohu.com/hisHq?code=cn_300228&start=20130930&end=20131231&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp']

