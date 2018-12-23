# Version: 1.0.1
FROM ubuntu:latest
MAINTAINER Solinari "solinari27@gmail.com"
RUN apt-get update
RUN apt-get install -y python2.7
RUN apt-get install -y python-pip
RUN apt-get install -y git
RUN git clone https://github.com/solinari27/stockCrawler.git /home/ubuntu/stockCrawler/
RUN pip install -r /home/ubuntu/stockCrawler/requirements.txt
RUN pip install pyaml
RUN mkdir /home/ubuntu/stockCrawler/Log
RUN mkdir/home/ubuntu/stockCrawler/netease/crawler/Log
RUN mkdir/home/ubuntu/stockCrawler/sohu/crawler/Log
# RUN echo 'Hi, I am in your container' > /usr/share/nginx/html/index.html
# EXPOSE 80
