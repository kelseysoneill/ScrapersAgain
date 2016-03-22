import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz


class MySpider(CrawlSpider):
    name = "cnncrawl"  # unique identifier for the spider
    allowed_domains = ['cnn.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.cnn.com/specials/politics/2016-election'
    ]  
    rules = [
        Rule(LinkExtractor(allow=r'/politics/'),
         callback='parse_item', follow=True)
    ]

    xpathitem = xpathItem()
    xpathitem.article_title = './/h1[@class="pg-headline"]/text()'
   # xpathitem.article_imagecaption = '//*[@id="article"]/div[1]/figure/figcaption/div[1]/p/text()'
    xpathitem.article_author = '/html/head/meta[10]/@content'
    xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
    xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = '//div[@class="zn-body__read-all"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = './/p[@class="update-time"]/text()'



    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item

#
#    def parse_item(self, response):
#        item = MasterItem(self.xpathitem, response)
#        #return item
#        
#        if item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0, 0):
#            return item
#

#    def parse_item(self, response):
#        sel = Selector(response)
#        results = []
#        item = MasterItem()
#        item['article_title'] = sel.xpath('.//h1[@class="pg-headline"]/text()').extract()
#        item['article_author'] = sel.xpath('.//p[@class="metadata__byline"]/span/a/text()').extract()
#        item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
#        item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
#       
#        temparticlecontent = ''.join(sel.xpath('//div[@class="zn-body__read-all"]//p//text()').extract()).strip()
#        temparticlecontent = re.sub(r'(\n)|(\s{2,})', '', temparticlecontent)
#        item['article_content'] = temparticlecontent
#        #item['article_content'] = sel.xpath('//div[@class="zn-body__read-all"]/p[descendant-or-self::text()]').extract()
#       
#        
#        
#        item['article_timestamp'] = sel.xpath('.//p[@class="update-time"]/text()').extract()
#        item['article_url'] = sel.xpath('/html/head/meta[9]/@content').extract()
#        results.append(item)
#        return results

