import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz


class MySpider(CrawlSpider):
    name = "foxcrawl"  # unique identifier for the spider
    allowed_domains = ['foxnews.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.foxnews.com/politics/elections/2016/presidential-election-headquarters'
    ]  
    rules = [
        Rule(LinkExtractor(allow=r'/politics/'), follow=True),
        Rule(LinkExtractor(), callback='parse_item')
        ]

    xpathitem = xpathItem()
    xpathitem.article_title = '//div[@class="main"]/article/div/h1/text()'
  #  xpathitem.article_imagecaption = '//*[@id="article"]/div[1]/figure/figcaption/div[1]/p/text()'
    xpathitem.article_author = '/html/head/meta[9]/@content'
    xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
    xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = './/div[@class="article-text"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = './/div[@class="inlineModule byline"]/time/@datetime'

    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item


#    def parse_item(self, response):
#        sel = Selector(response)
#        results = []
#
#        item = FoxItem()
#        item['article_title'] = sel.xpath('//div[@class="main"]/article/div/h1/text()').extract()
#        #item['article_imagecaption'] = sel.xpath('.//div[@class="entry-content"]/div[3]/figure[1]/figcaption[1]/span[1]/text()').extract()
#        #item['article_author'] = sel.xpath('.//div[@class="name"]/address/span/text()').extract()
#        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
#        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
#        #item['article_content'] = articles.xpath('.//p[@class="story-body-text"]//text()').extract()
#        #item['article_timestamp'] = articles.xpath('.//div[@class="inlineModule byline"]/time/@datetime').extract()
#        #item['article_url'] = articles.xpath('.//h3[@class="entry-title"]/a/@href').extract()
#        results.append(item)
#        return results
