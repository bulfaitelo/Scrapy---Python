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
        next_page = response.xpath(
            '//li[contains(@class, "item next")]//a[@rel = "next"]/@href'
        )

        if next_page:
            self.log('PROXIMMA PAGINA {}'.format(next_page.extract_first()))
            # self.log("PROXIMMA PAGINA %s" % next_page.extract_first())
            yield scrapy.Request(
                url=next_page.extract_first(), callback=self.parse
            )
    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        year = response.xpath(
            "//span[contains(text(), 'Ano')]/following-sibling::strong/a/@title"
        ).extract_first()
        ports = response.xpath(
            "//span[contains(text(), 'Portas')]/following-sibling::strong/@text"
        ).extract_first()
        yield {
            'title': title,
            'port' : ports, 
            'year' : year,
        }