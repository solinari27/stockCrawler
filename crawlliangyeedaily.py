#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 17:03
# @Author  : Aries
# @Site    : 
# @File    : crawlliangyeedaily.py
# @Software: PyCharm

import liangyee.liangyeeCrawler
from liangyee.liangyeeUser import *

refresh_liangyeeUser()

ll = liangyee.liangyeeCrawler.liangyeeCrawler()
ll.crawlliangyee("daily")


