# -*- coding: utf-8 -*-
import scrapy


class IeeeSpider(scrapy.Spider):
    name = 'ieee'
    allowed_domains = ['www.ieee.org']
    start_urls = ['https://www.ieee.org/conferences_events/conferences/search/index.html']

    def parse(self, response):
        pass
