import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RTAE.items import *
#from items import MasterItem, xpathItem, ArticleItem  # item class
import datetime
import pytz

class MySpider(CrawlSpider):
    name = "washtimescrawl"  # unique identifier for the spider
    allowed_domains = ['washingtontimes.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.washingtontimes.com/news/politics/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/news/'),
         callback='parse_item', follow=True)
    ]

    xpathitem = xpathItem()
    xpathitem.article_title = '//h1[@class="page-headline"]/text()'
    xpathitem.article_imagecaption = '//*[@id="content"]/div/div/section/article/div[1]/section/div/figure/figcaption/text()'
    xpathitem.article_author = '/html/head/meta[13]/@content'
    xpathitem.article_highlights = './/div[@class="el__storyhighlights"]/ul/li/text()'
    xpathitem.article_edsource = '//*[@id="body-text"]/div[1]/div[2]/p/cite/text()'
    xpathitem.article_content = '//div[@class="storyareawrapper"]/descendant-or-self::*[not(self::script)]/text()'
    xpathitem.article_timestamp = '//div[@class="article-text"]/div[1]/span[2]/text()'


    def parse_item(self, response):
        item =  MasterItem(self.xpathitem, response)
        if (item["article_timestamp"] >= datetime.datetime(2015, 7, 1, 0, 0 , 0)):
            return item

        #sel = Selector(response)
        #results = []
        #item = MasterItem()
        #item['article_title'] = sel.xpath('//h1[@class="page-headline"]/text()').extract()
        #item['article_imagecaption'] = sel.xpath('//*[@id="content"]/div/div/section/article/div[1]/section/div/figure/figcaption/text()').extract()
        #item['article_author'] = sel.xpath('/html/head/meta[13]/@content').extract()
        ##item['article_preview'] = sel.xpath('//div[@class="content__standfirst"]/p/text()').extract()
        ##item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        ##item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
        #temparticlecontent = ''.join(sel.xpath('//div[@class="storyareawrapper"]//text()').extract()).strip()
        #temparticlecontent = re.sub(r'(\n)|(\s{2,})', '', temparticlecontent)
        #item['article_content'] = temparticlecontent
        #
        ##item['article_content'] = sel.xpath('//div[@class="storyareawrapper"]/p[descendant-or-self::text()]').extract()
        #item['article_timestamp'] = sel.xpath('//div[@class="article-text"]/div[1]/span[2]/text()').extract()
        #item['article_url'] = sel.xpath('/html/head/meta[21]/@content').extract()
        #results.append(item)
        #return results
