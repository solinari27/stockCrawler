import sys
import os

from common.mongo.sohuConn import SohuConn

sys.path.append(os.getcwd())
# os.system("scrapy runspider crawler/crawler/spiders/sohuCrawler.py --loglevel ERROR")

conn = SohuConn("/home/solinari/workspace/stockCrawler/Conf/sohu.conf")