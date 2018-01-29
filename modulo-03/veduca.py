# -*- coding: utf-8 -*-
import scrapy


class VeducaSpider(scrapy.Spider):
    name = 'veduca'
    allowed_domains = ['veduca.org/p/matematica-financeira']
    start_urls = ['http://veduca.org/p/matematica-financeira/']

    def parse(self, response):
        pass
