import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz


class MySpider(CrawlSpider):
    name = "nbccrawl2"  # unique identifier for the spider
    allowed_domains = ['nbcnews.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.nbcnews.com/politics/2016-election/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/politics/2016-election/'),
         callback='parse_item', follow=True)
    ]

    xpathitem = xpathItem()
    xpathitem.article_title = './/div[@class="article-hed"]/h1/text()'
  #  xpathitem.article_imagecaption = '//*[@id="article"]/div[1]/figure/figcaption/div[1]/p/text()'
    xpathitem.article_author = './/div[@class="article-hed"]/p/span/span[2]/text()'
    xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
    xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = '//div[@class="article-body"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = './/div[@class="article-flags"]/div[1]/div[2]/time/@datetime'


    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item
#
#    def parse_item(self, response):
#        sel = Selector(response)
#        results = []
#        item = MasterItem()
#        item['article_title'] = sel.xpath('.//div[@class="article-hed"]/h1/text()').extract()
#        #item['article_imagecaption'] = sel.xpath('//*[@id="globalWrapper"]/main/div[4]/div/article/div[1]/section[1]/div/div/figure/figcaption/p/text()').extract()
#        item['article_author'] = sel.xpath('//*[@id="510171"]/div/div[1]/header/div[2]/p/span/span[2]/text()').extract()
#        #item['article_preview'] = sel.xpath('.//div[@class="summary  "]/header/p[2]/text()').extract()
#        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
#        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
#        temparticlecontent = ''.join(sel.xpath('//div[@class="article-body"]//p//text()').extract()).strip()        
#        #temparticlecontent = ''.join(sel.xpath('//div[@class="article-body"]//text()').extract()).strip()
#        temparticlecontent = re.sub(r'(\n)|(\s{2,})', '', temparticlecontent)
#        item['article_content'] = temparticlecontent
#        
#        
#      #  item['article_content'] = sel.xpath('.//div[@class="article-body"]/p/text()').extract()
#        item['article_timestamp'] = sel.xpath('.//div[@class="article-flags"]/div[1]/div[2]/time/@datetime').extract()
#        item['article_url'] = sel.xpath('/html/head/meta[9]/@content').extract()
#        results.append(item)
#        return results