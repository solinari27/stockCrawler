#!/usr/bin/env bash
cd /home/ubuntu/stockCrawler/sohu/crawler
export PYTHONPATH=/home/ubuntu/stockCrawler:%PYTHONPATH
#cd /home/solinari/workspace/stockCrawler/sohu/crawler
#export PYTHONPATH=/home/solinari/workspace/stockCrawler:%PYTHONPATH
python run.py
