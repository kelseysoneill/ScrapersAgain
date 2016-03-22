import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz


class MySpider(CrawlSpider):
    name = "guardiancrawl3"  # unique identifier for the spider
    allowed_domains = ['theguardian.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.theguardian.com/us-news/us-elections-2016/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/us-news/'),
         callback='parse_item', follow=True)
    ]

    xpathitem = xpathItem()
    xpathitem.article_title = '//h1[@class="content__headline js-score"]/text()'
    xpathitem.article_imagecaption = '//figure[@class="media-primary media-content()  "]/figcaption/text()'
    xpathitem.article_author = '//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/span/a/span/text()'
    xpathitem.article_highlights = '//div[@class="content__standfirst"]/p/text()'
    xpathitem.article_edsource = '//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()'
    xpathitem.article_content = '//div[@class="content__article-body from-content-api js-article__body"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = '//*[@id="article"]/div[2]/div/div[1]/div[2]/p[2]/time[1]/@datetime'


    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0, tzinfo=pytz.UTC)):
            return item



#    def parse_item(self, response):
#        sel = Selector(response)
#        results = []
#        item = MasterItem()
#        item['article_title'] = sel.xpath('//h1[@class="content__headline js-score"]/text()').extract()
#        item['article_imagecaption'] = sel.xpath('//figure[@class="media-primary media-content()  "]/figcaption/text()').extract()
#        item['article_author'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/span/a/span/text()').extract()
#        item['article_preview'] = sel.xpath('//div[@class="content__standfirst"]/p/text()').extract()
#        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
#        item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
#       
#        temparticlecontent = ''.join(sel.xpath('//div[@class="content__article-body from-content-api js-article__body"]//text()').extract()).strip()
#        temparticlecontent = re.sub(r'(\n)|(\s{2,})', '', temparticlecontent)
#        item['article_content'] = temparticlecontent
#
#
# #item['article_content'] = sel.xpath('//div[@class="content__article-body from-content-api js-article__body"]/p[descendant-or-self::text()]').extract()
#        item['article_timestamp'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[2]/time[1]/@datetime').extract()
#        item['article_url'] = sel.xpath('//*[@id="js-context"]/head/meta[17]/@content').extract()
#        results.append(item)
#        return results
#

