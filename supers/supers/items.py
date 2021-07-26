# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SupersItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    headline = scrapy.Field()
    body = scrapy.Field()
