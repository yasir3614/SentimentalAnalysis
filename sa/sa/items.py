# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SaItem(scrapy.Item):
    item_name = scrapy.Field()
    img=scrapy.Field()
    comments=scrapy.Field()
    price=scrapy.Field()
    pass
