#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: make_ascend.py
@time: 2019/05/04
"""
import sys
import time

sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')

import torch
from make_collection import make_training_tensor

for ret in make_training_tensor(code="600007", start_date="2015-01-01", end_date="2019-12-31"):
    print torch.tensor(ret)
