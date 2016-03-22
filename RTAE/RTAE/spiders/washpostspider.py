import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz


class MySpider(CrawlSpider):
    name = "washpostcrawl2"  # unique identifier for the spider
    allowed_domains = ['washingtonpost.com']  # limits the crawl to this domain list
    start_urls = [
    'https://www.washingtonpost.com/politics/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/news/the-fix/'), follow=True),
        Rule(LinkExtractor(), callback='parse_item')
        ]

    xpathitem = xpathItem()
    xpathitem.article_title = '//*[@id="article-topper"]/h1/text()'
   # xpathitem.article_imagecaption = '//*[@id="article"]/div[1]/figure/figcaption/div[1]/p/text()'
    xpathitem.article_author = '//span[@class="pb-byline"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
    xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = '//*[@id="article-body"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = '//*[@id="article-body"]/div[1]/span[2]/@content'


    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0, 0)):
            return item

#    def parse_item(self, response):
#        sel = Selector(response)
#        results = []
#        item = WashpostItem()
#        item['article_title'] = sel.xpath('//*[@id="article-topper"]/h1/text()').extract()
#        item['article_author1'] = sel.xpath('//*[@id="article-body"]/div[1]/span[1]/a/span/text()').extract()
#        item['article_timestamp'] =sel.xpath('//*[@id="article-body"]/div[1]/span[2]/@content').extract()
#        item['article_content'] = sel.xpath('//*[@id="article-body"]//text()').extract()
#        item['article_url'] = sel.xpath('/html/head/meta[23]/@content').extract()
#        results.append(item)
#        return results
#
