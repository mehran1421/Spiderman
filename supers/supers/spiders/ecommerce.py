import scrapy
import json
from ..items import SupersItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from readability import Document
import pandas as pd
from pprint import pprint


class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'

    # allowed_domains = ['localhost:8000']

    def start_requests(self):
        yield scrapy.Request(url='http://localhost:8000/product/?format=json', callback=self.parse_id)

    def parse_id(self, response):
        data = json.loads(response.body)['data']['data']
        for product in data:
            yield scrapy.Request(url='http://localhost:8000/product/{0}/?format=json'.format(product.get('slug')),
                                 callback=self.parse)

    def parse(self, response, **kwargs):
        data = json.loads(response.body)['data']['data']
        yield {
            'title': data.get('title'),
            'slug': data.get('slug'),
            'description': data.get('description'),
            'category': [
                {
                    'title': cat.get('title'),
                    'slug': cat.get('slug')
                }
                for cat in data.get('category')
            ],
            'seller': {
                'username': data.get('seller').get('username'),
                'email': data.get('seller').get('email'),

            },
            'thumbnail': data.get('thumbnail'),
            'persian_publish': data.get('persian_publish'),
            'price': data.get('price'),
            'status': data.get('status'),
            'choice': data.get('choice')
        }

