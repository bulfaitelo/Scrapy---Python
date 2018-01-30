# -*- coding: utf-8 -*-
import scrapy

from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class IeeeSpider(CrawlSpider):
    name = 'ieee'
    allowed_domains = ['www.ieee.org']
    start_urls = ['https://www.ieee.org/conferences_events/conferences/search/index.html']

    rules = (
        Rule (
            LinkExtractor(allow='/conferences_events/conferences/search/index.html')
        ),
        Rule (
            LinkExtractor(
                allow='/conferences_events/conferences/conferencedetails/index.html'                
            ),  callback='parse_conferece'
        )
    )

    def parse_conferece(self, response):
        self.log(response.xpath("//title/text()").extract_first())
