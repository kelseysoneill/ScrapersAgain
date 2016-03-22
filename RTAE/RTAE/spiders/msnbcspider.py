import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz



class MySpider(CrawlSpider):
    name = "msnbccrawl3"  # unique identifier for the spider
    allowed_domains = ['msnbc.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.msnbc.com/elections'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/msnbc/'),
         callback='parse_item', follow=True)
    ]

    xpathitem = xpathItem()
    xpathitem.article_title = '//h1[@class="is-title-pane panel-pane pane-node-title"]/text()'
    xpathitem.article_imagecaption = '//div[@class="media-meta__caption"]/text()'
    xpathitem.article_author = '//*[@id="block-system-main"]/div/div/article/div/div[2]/span[2]/descendant-or-self::*[not(self::script)]/text()'
   # xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
   # xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = '//div[@class="field field-name-body field-type-text-with-summary field-label-hidden"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = '//*[@id="block-system-main"]/div/div/article/header/div[3]/time/@datetime'


    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item

#    def parse_item(self, response):
#        sel = Selector(response)
#        results = []
#        item = MasterItem()
#        item['article_title'] = sel.xpath('//h1[@class="is-title-pane panel-pane pane-node-title"]/text()').extract()
#        item['article_imagecaption'] = sel.xpath('//div[@class="media-meta__caption"]/text()').extract()
#        item['article_author'] = sel.xpath('//*[@id="block-system-main"]/div/div/article/div/div[2]/span[2]/text()').extract()
#        #item['article_preview'] = sel.xpath('//div[@class="content__standfirst"]/p/text()').extract()
#        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
#        #item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
#      
#        temparticlecontent = ''.join(sel.xpath('//div[@class="field field-name-body field-type-text-with-summary field-label-hidden"]//text()').extract()).strip()
#        temparticlecontent = re.sub(r'(\n)|(\s{2,})', '', temparticlecontent)
#        item['article_content'] = temparticlecontent       
#
#       # item['article_content'] = sel.xpath('//div[@class="field field-name-body field-type-text-with-summary field-label-hidden"]/p[descendant-or-self::text()]').extract()
#        item['article_timestamp'] = sel.xpath('//*[@id="block-system-main"]/div/div/article/header/div[3]/time/@datetime').extract()
#        item['article_url'] = sel.xpath('/html/head/meta[4]/@content').extract()
#        results.append(item)
#        return results
