from scrapy.spider import Spider
from scrapy import signals
from scrapy.selector import Selector
import logging
import csv
from careerpagescrapers.items import Startup, StartupJob
from scrapy.log import ScrapyFileLogObserver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import log

logfile = open('testlog.log', 'w')
log_observer = ScrapyFileLogObserver(logfile, level=logging.DEBUG)
log_observer.start()

class KarmahireSpider(Spider):
    name = 'karmahire'
    allowed_domains = ['karmahire.com']
    start_urls = ['']
    
    def __init__(self, stats):
        self.stats = stats
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)
    
    
    def parse(self, response):
        sel = Selector(response)
        
        items = []
        jobindex = 0
        joblist = sel.xpath('//div[@class="job-list-item"]')
        for jobs in joblist:
            listing = StartupJob()
            listing['startup'] = response.url
            listing['title'] = sel.xpath('//div[@class="job-list-item"]/div/h2/text()').extract()[jobindex]
            listing['url'] =  sel.xpath('//div[@class="job-list-item"]/a/@href').extract()[jobindex]
            listing['location'] = sel.xpath('//div[@class="job-list-item"]/div/h3/text()').extract()[jobindex]
            items.append(listing)
            jobindex += 1
        return items