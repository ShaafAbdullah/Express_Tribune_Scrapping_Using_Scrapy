# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataScrapingNewspageItem(scrapy.Item):
    #define the fields for your item here like:
    tagline = scrapy.Field()
    news =scrapy.Field()
    link= scrapy.Field()
    date=scrapy.Field()

