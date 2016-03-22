import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz

class MySpider(CrawlSpider):
    name = "cbscrawl3"  # unique identifier for the spider
    allowed_domains = ['cbsnews.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.cbsnews.com/election-2016/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/news/'),
         callback='parse_item', follow=True)
    ]

    xpathitem = xpathItem()
    xpathitem.article_title = '//h1[@class="title"]/text()'
    xpathitem.article_imagecaption = '//*[@id="article"]/div[1]/figure/figcaption/div[1]/p/text()'
    xpathitem.article_author = '/html/head/meta[7]/@content'
    xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
    xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = '//div[@class="entry"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = '//*[@id="article"]/header/div/span[4]/text()'


    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item
