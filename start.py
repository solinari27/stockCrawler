#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 9:57
# @Author  : Aries
# @Site    : 
# @File    : start.py
# @Software: PyCharm

import stockcode.quoteCfi.quoteCfiSpider as st
spider = st.quoteCfiSpider()
spider.inputDB()
