#!/usr/bin/env bash
/home/ubuntu/stockCrawler
python /home/ubuntu/stockCrawler/crawlstockcode.py&
sleep 1h
python /home/ubuntu/stockCrawler/crawlliangyeeweekend.py&
