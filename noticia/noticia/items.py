# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoticiaItem(scrapy.Item):
    #define the fields for your item here like:
    link = scrapy.Field()
    titulo = scrapy.Field()
    autor = scrapy.Field()
    pubdate = scrapy.Field()
    descrip = scrapy.Field()
    imagen = scrapy.Field()
    video = scrapy.Field()



