import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz


class MySpider(CrawlSpider):
    name = "politicocrawl3"  # unique identifier for the spider
    allowed_domains = ['politico.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.politico.com/news/2016-elections'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'.com/story/'),
         callback='parse_item', follow=True)
    ]

    xpathitem = xpathItem()
    xpathitem.article_title = './/h1[@class=" "]/text()'
    xpathitem.article_imagecaption = './/*[@id="globalWrapper"]/main/div[4]/div/article/div[1]/section[1]/div/div/figure/figcaption/p/text()'
    xpathitem.article_author = './/div[@class="credits-list"]/dl/dt/a/text()'
    xpathitem.article_highlights = './/div[@class="summary  "]/header/p[2]/text()'
    xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = './/div[@class="content-group story-core"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = '//time/@datetime'


    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item





    #def parse_item(self, response):
    #    sel = Selector(response)
    #    results = []
    #    item = MasterItem()
    #    item['article_title'] = sel.xpath('.//h1[@class=" "]/text()').extract()
    #    item['article_imagecaption'] = sel.xpath('.//*[@id="globalWrapper"]/main/div[4]/div/article/div[1]/section[1]/div/div/figure/figcaption/p/text()').extract()
    #   #item['article_author'] = sel.xpath('.//div[@class="content-group story-preface"]/div/div/footer/p[1]/span/text()').extract()
    #    #item['article_author'] = sel.xpath('.//footer[@class="meta"]/p[1]/a/text()').extract()
    #    item['article_author'] = sel.xpath('.//div[@class="credits-list"]/dl/dt/a/text()').extract()
    #    item['article_preview'] = sel.xpath('.//div[@class="summary  "]/header/p[2]/text()').extract()
    #    #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
    #    #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
    #    temparticlecontent = ''.join(sel.xpath('.//div[@class="content-group story-core"]//p//text()').extract()).strip()
    #    temparticlecontent = re.sub(r'(\n)|(\s{2,})', '', temparticlecontent)
    #    item['article_content'] = temparticlecontent
    #            
    #    #item['article_content'] = sel.xpath('//div[@class="content-group story-core"]//p//text()').extract()
    #    item['article_timestamp'] = sel.xpath('//div[@class="story-text "]/div[2]/div/footer/p[2]/time/@datetime').extract()
    #    item['article_url'] = sel.xpath('/html/head/meta[8]/@content').extract()
    #    results.append(item)
    #    return results