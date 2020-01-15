# -*- coding: utf-8 -*-
import scrapy


class RecipesSpider(scrapy.Spider):
    name = 'recipes'
    allowed_domains = ['https://www.myrecipes.com/']
    start_urls = ['http://https://www.myrecipes.com//']

    def parse(self, response):
        pass
