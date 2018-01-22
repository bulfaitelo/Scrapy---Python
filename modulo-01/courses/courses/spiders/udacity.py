# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/ir-root/ir-content/ir-course-catalog/section/div/div[2]/div[2]/div/div")
        for div in divs:
            link = div.xpath('.//h3/a')
            # test() pega apensa o texto 
            # title = link.xpath('./text()').extract_first()
            # @ pega o atributo da tag
            href = link.xpath('./@href').extract_first()
            # img = div.xpath('.//img[contains(@class, "img-responsive")]/@src').extract_first()
            # description = div.xpath('.//div[2]/div[2]/span/text()').extract_first()
            yield scrapy.Request(
                url= 'https://br.udacity.com%s' %href, 
                callback=self.parse_detail
            )

    def parse_detail(self, response):
        title = response.xpath(
            '//h1[contains(@class, "hero__course--title")]/text()'
        ).extract_first()
        readline = response.xpath(
            '//div[contains(@class, "summary-text")]/p/text()'
        ).extract_first()
        instructors = []
        for div in response.xpath('//ir-instructor'):
            instructors.append(
                {
                    'name': div.xpath('./h3/text()').extract_first(),
                    'image': div.xpath('.//img/@src').extract_first()
                }
            )
        yield {
            'title' : title,
            'readline': readline,
            'instructor': instructors,
        }