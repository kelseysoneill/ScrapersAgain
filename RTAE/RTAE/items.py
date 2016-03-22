# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.selector import Selector

from dateutil.parser import parse
import datetime
import re


class MasterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass

    article_title = scrapy.Field()
    article_author = scrapy.Field()
    article_content = scrapy.Field()
    article_timestamp = scrapy.Field()
    article_highlights = scrapy.Field()
    article_preview = scrapy.Field()
    article_edsource = scrapy.Field()
    article_url = scrapy.Field()
    article_imagecaption = scrapy.Field()



    def __init__(self, xpathitem, response):
        super(scrapy.Item, self).__init__()

        u = campaignutilities()

        self["article_title"] = u.itemextract(xpathitem.article_title, response)
        self["article_author"] = u.itemextract(xpathitem.article_author, response)
        self["article_content"] = u.itemextract(xpathitem.article_content, response)
        self["article_timestamp"] = u.dateparse(u.itemextract(xpathitem.article_timestamp, response))
        self["article_highlights"] = u.itemextract(xpathitem.article_highlights, response)
        self["article_preview"] = u.itemextract(xpathitem.article_preview, response)
        self["article_edsource"] = u.itemextract(xpathitem.article_edsource, response)
        self["article_url"] = response.url #u.itemextract(xpathitem.article_url, response)
        self["article_imagecaption"] = u.itemextract(xpathitem.article_imagecaption, response)
        if self["article_content"] == None:
            return []
        if self["article_content"] == "":
            return []


class ArticleItem(scrapy.Item):

    article_title = scrapy.Field()
    article_author = scrapy.Field()
    article_content = scrapy.Field()
    article_timestamp = scrapy.Field()
    article_highlights = scrapy.Field()
    article_preview = scrapy.Field()
    article_edsource = scrapy.Field()
    article_url = scrapy.Field()
    article_imagecaption = scrapy.Field()



    def fill(self, xpathitem, response, article):

        u = campaignutilities()

        self["article_title"] = u.selectorextract(xpathitem.article_title, article)
        self["article_author"] = u.selectorextract(xpathitem.article_author, article)
        self["article_content"] = u.selectorextract(xpathitem.article_content, article)
        self["article_timestamp"] = u.dateparse(u.selectorextract(xpathitem.article_timestamp, article))
        self["article_highlights"] = u.selectorextract(xpathitem.article_highlights, article)
        self["article_preview"] = u.selectorextract(xpathitem.article_preview, article)
        self["article_edsource"] = u.selectorextract(xpathitem.article_edsource, article)
        self["article_url"] = response.url #u.itemextract(xpathitem.article_url, response)
        self["article_imagecaption"] = u.selectorextract(xpathitem.article_imagecaption, article)
        if self["article_content"] == None:
            return None
        if self["article_content"] == "":
            return None


class xpathItem():

    def __init__(self):
        self.article_title = None
        self.article_author = None
        self.article_content = None
        self.article_timestamp = None
        self.article_highlights = None
        self.article_preview = None
        self.article_edsource = None
        self.article_url = None
        self.article_imagecaption = None


class campaignutilities():
    def dateparse(self,datestring):
        try:
           return parse(datestring)
        except:
            return datetime.datetime.now()

    def itemextract(self, _xpath, response):
        try:
            sel = Selector(response)
            txt = "".join(sel.xpath(_xpath).extract()).strip()
            txt = re.sub(r'(\n)|(\s{2,})', '', txt)
            return txt
        except:
            return None

    def selectorextract(self, _xpath, selector):
        """

        :rtype: object
        """
        try:
            txt = "".join(selector.xpath(_xpath).extract()).strip()
            txt = re.sub(r'(\n)|(\s{2,})', '', txt)
            return txt
        except:
            return ""
