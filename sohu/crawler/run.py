import sys
import os

sys.path.append(os.getcwd())
# os.system("scrapy runspider sohu/crawler/crawler/spiders/sohuCrawler.py --loglevel ERROR")
os.system("export PYTHONPATH=/home/solinari/workspace/stockCrawler:%PYTHONPATH")
os.system("scrapy crawl SohuCrawler ")