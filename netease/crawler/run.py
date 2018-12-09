# -*- coding: utf-8 -*-
# @Author  : Solinari
# @Email   : 
# @File    : run.py
# @Software: PyCharm
# @Time    : 2018/12/09

import sys
import os

sys.path.append(os.getcwd())
os.system("export PYTHONPATH=/home/ubuntu/stockCrawler:/home/solinari/workspace/stockCrawler:%PYTHONPATH")
os.system("scrapy crawl NeteaseCrawler")