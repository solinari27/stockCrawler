#!/usr/bin/env bash
cd /home/ubuntu/stockCrawler
#python /home/ubuntu/stockCrawler/crawlliangyeedaily.py&
python /home/ubuntu/stockCrawler/crawlnetease.py&
sh crawlsohu.sh
