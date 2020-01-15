# -*- coding: utf-8 -*-
import scrapy


class RecipesSpider(scrapy.Spider):
    name = 'recipes'
    allowed_domains = ['https://www.myrecipes.com/']
    start_urls = [
        'https://www.myrecipes.com/recipe/mediterranean-tuna-salad-2'
        ]

    def parse(self, response):
        title = response.\
            xpath('//*[@class="headline heading-content"]/text()')\
            .extract_first()

        totalTime = response.\
            xpath('//*[@class="recipe-meta-item-body"]/text()')\
            .extract_first().strip()

        ingredients = response.\
            xpath('//*[@class="ingredients"]/ul/li/text()').extract()

        instructions = response.\
            xpath('//*[@class="step"]/p/text()').extract()

        nutrients = response.\
            xpath('//*[@class="partial recipe-nutrition"]/ul/li/text()').\
            extract()

        yield {
            'Title': title,
            'TotalTime': totalTime,
            'Ingredients': ingredients,
            'Instructions': instructions,
            'Nutrients': nutrients
        }
