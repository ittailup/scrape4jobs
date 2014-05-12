# Scrapy settings for scrape4jobs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrape4jobs'

SPIDER_MODULES = ['scrape4jobs.spiders']
NEWSPIDER_MODULE = 'scrape4jobs.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Scrape4jobs project'
