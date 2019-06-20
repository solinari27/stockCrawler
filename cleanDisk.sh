#!/usr/bin/env bash
cd /home/ubuntu/stockCrawler
python /home/ubuntu/stockCrawler/cleandb.py&

docker ps -a | sed '/^CONTAINER/d' | grep "Exited" | gawk '{cmd="docker rm "$1; system(cmd)}'docker ps -a | sed '/^CONTAINER/d' | grep "Exited" | gawk '{cmd="docker rm "$1; system(cmd)}'