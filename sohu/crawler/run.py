import sys
import os

sys.path.append(os.getcwd())
# os.system("scrapy runspider sohu/crawler/crawler/spiders/sohuCrawler.py --loglevel ERROR")
os.system("export PYTHONPATH=/home/ubuntu/stockCrawler:/home/solinari/workspace/stockCrawler:%PYTHONPATH")
os.system("scrapy crawl SohuCrawler ")