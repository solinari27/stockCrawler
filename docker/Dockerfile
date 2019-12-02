# Version: 1.0.1
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python2.7
RUN apt-get install -y python-pip
# RUN apt-get install -y git
RUN apt-get install -y vim
# RUN git clone https://github.com/solinari27/stockCrawler.git /home/solinari/workspace/stockCrawler/
# copy require.txt to here
COPY requirements.txt /opt/requirements.txt
RUN pip install pymongo -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r /opt/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyaml -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN mkdir /home/solinari/workspace/stockCrawler/netease/crawler/data
# RUN mkdir /home/solinari/workspace/stockCrawler/Log
# RUN mkdir /home/solinari/workspace/stockCrawler/netease/crawler/Log
# RUN mkdir /home/solinari/workspace/stockCrawler/sohu/crawler/Log
# RUN mkdir /home/ubuntu/stockCrawler/netease/crawler/data
# RUN mkdir /home/ubuntu/stockCrawler/Log
# RUN mkdir /home/ubuntu/stockCrawler/netease/crawler/Log
# RUN mkdir /home/ubuntu/stockCrawler/sohu/crawler/Log
# RUN echo 'Hi, I am in your container' > /usr/share/nginx/html/index.html
# EXPOSE 80

# ENV MONGODB_AUTH mongodb://127.0.0.1:27017
# ENV MONGODB_AUTH mongodb://login:pw@mongodb:27017/dbname

# RUN git clone https://github.com/solinari27/stockCrawler.git /home/ubuntu/stockCrawler/
# RUN pip install -r /home/ubuntu/stockCrawler/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
