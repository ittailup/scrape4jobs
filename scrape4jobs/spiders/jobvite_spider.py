from scrapy.spider import Spider
from scrapy import signals
from scrapy.selector import Selector
import logging
import csv
from careerpagescraper.items import Startup, StartupJob
from scrapy.log import ScrapyFileLogObserver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import log

logfile = open('testlog.log', 'w')
log_observer = ScrapyFileLogObserver(logfile, level=logging.DEBUG)
log_observer.start()

class JobviteSpider(Spider):
    name = 'jobvite'
    allowed_domains = ['jobvite.com']
    start_urls = ['']
    
    def __init__(self, stats):
        self.stats = stats
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)
    
    
    def parse(self, response):
        sel = Selector(response)
        categories = sel.xpath("//h3/text()").extract()
        
        items = []
        catindex = 1
        for category in categories:
            jobindex = 0
            joblist = sel.xpath("(//ul[@class='joblist'])[" + str(catindex) + "]/li")
            for jobs in joblist:
                listing = StartupJob()
                listing['startup'] = sel.xpath('//div[@class="jvheader"]/img/@alt').extract()
                listing['title'] = sel.xpath("(//ul[@class='joblist'])[" + str(catindex) + "]/li/text()").extract()[jobindex].strip()
                listing['url'] = sel.xpath("(//ul[@class='joblist'])[" + str(catindex) + "]/li/a/@onclick").extract()[jobindex].split("'")[5]
                listing['location'] = sel.xpath("(//ul[@class='joblist'])[" + str(catindex) + "]/li/span[@class='joblocation']/text()").extract()[jobindex]
                items.append(listing)
                jobindex += 1
            catindex += 1
        return items