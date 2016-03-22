import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz



class MySpider(CrawlSpider):
    name = "newsmaxcrawl"  # unique identifier for the spider
    allowed_domains = ['newsmax.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.newsmax.com/hottopics/topic/2016-Elections/246/'
    ]

    rules = [
        Rule(LinkExtractor(allow=r''),
         callback='parse_item', follow=True)
    ]
    
    xpathitem = xpathItem()
    xpathitem.article_title = './/h1[@class="article"]/text()'
    #xpathitem.article_imagecaption = './/div[@class="entry-content"]/div[3]/figure[1]/figcaption[1]/span[1]/text()'
    xpathitem.article_author = './/span[@class="artPgByline"]/text()'
  #  xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
  #  xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = './/div[@class="mainArticleDiv"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = './/span[@class="date"]/text()'
    #xpathitem.article_url = '/html/head/meta[14]/@content'     

    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item

#        sel = Selector(response)
#        #results = []
#        item = MasterItem()
#        item['article_title'] = sel.xpath('//*[@id="page-title"]/text()').extract()
#        #item['article_imagecaption'] = sel.xpath('.//div[@class="entry-content"]/div[3]/figure[1]/figcaption[1]/span[1]/text()').extract()
#        item['article_author'] = sel.xpath('/html/head/meta[2]/@content').extract()
#        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
#        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
#        item['article_content'] = "".join(sel.xpath('//div[@class="field-item even"]/descendant-or-self::*[not(self::script)]/text()').extract()).strip()
#        ##temparticlecontent = ''.join(sel.xpath('//div[@class="field-item even"]//text()').extract()).strip()
#        #temparticlecontent = "".join(re.sub(r'(\n)|(\s{2,})', '', temparticlecontent))
#
#                        
#        try:
#            item['article_timestamp'] = parse("".join(sel.xpath('//*[@id="content"]/article/p/span[2]/text()').extract()).strip())
#        except:
#            item['article_timestamp'] = datetime.datetime.now()
#                                  
#        item['article_url'] = sel.xpath('/html/head/meta[14]/@content').extract()
#        #results.append(item)
#        return (item)


