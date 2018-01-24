# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    # allowed_domains = ['rj.olx.com.br']
    start_urls = ['http://rj.olx.com.br/veiculos-e-pecas/carros/']

    def parse(self, response):
        # itens = response.xpath(
        #     '//ul[@id="main-ad-list"]/li[contains(@class, "item") and not(contains(@class, "list_native"))]'
        # )
        itens = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )      
        for item in itens:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)        

    def parse_detail(self, response):
        self.log(response.url)
