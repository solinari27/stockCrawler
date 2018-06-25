#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 9:57
# @Author  : Solinari
# @Site    :
# @File    : crawlnetease.py
# @Software: PyCharm

import netease.neteaseCrawler

n = netease.neteaseCrawler.neteaseCrawler()
# n.clean()
n.crawl()

