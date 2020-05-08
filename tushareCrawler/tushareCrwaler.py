#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: tushareCrwaler.py 
@time: 2020/05/07 
"""

# tornado + supervisor + celery
from datetime import datetime
import time
# 每n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        time.sleep(n)

timer(5)