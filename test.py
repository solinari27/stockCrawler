import netease.neteaseCrawler
import time

#lastDate = time.strptime("2000:01:01", "%Y:%m:%d")
#print lastDate
#s = time.localtime(time.time())
#print s.tm_year
#print '%02d' % s.tm_mon
#print '%02d' % s.tm_mday
# netease
n = netease.neteaseCrawler.neteaseCrawler()
#n.crawl()
print n.requestJson(0, '600027', '20071105', '20150618')