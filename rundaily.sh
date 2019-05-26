#!/usr/bin/env bash
cd /home/ubuntu/stockCrawler
python /home/ubuntu/stockCrawler/crawlliangyeedaily.py
# python /home/ubuntu/stockCrawler/crawlnetease.py&
# sh crawlnetease.sh
# sh crawlsohu.sh
# sudo docker run -d stockcrawler:test /home/ubuntu/stockCrawler/crawlnetease.sh
#docker run -d --net=host stockcrawler /home/solinari/workspace/stockCrawler/crawlnetease.sh
#docker run -d --net=host stockcrawler /home/solinari/workspace/stockCrawler/crawlsohu.sh
