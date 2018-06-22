import netease.neteaseCrawler

# netease
n = netease.neteaseCrawler.neteaseCrawler()
n.crawl()
print n.requestJson('601857', '20071105', '20150618')