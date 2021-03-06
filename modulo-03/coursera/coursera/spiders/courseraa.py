# -*- coding: utf-8 -*-
import scrapy


class CourseraaSpider(scrapy.Spider):
    name = 'courseraa'
    category = None

    def start_requests(self):
        if self.category is None:
            yield scrapy.Request(
                url='https://pt.coursera.org/browse?languages=pt/',
                callback=self.parse
                
            )
        else:
            yield scrapy.Request(
                url='https://pt.coursera.org/browse/%s' % self.category,
                callback=self.parse_category
            )

    
    def parse(self, response):
        self.log(self.category)
        categories = response.xpath("//div[contains(@class, 'rc-DomainNav')]/a")
        for cat in categories:
            cat_url = cat.xpath('./@href').extract_first()
            self.log('Catgory: %s' % cat_url)
            yield scrapy.Request(
                url='https://www.coursera.org%s' % cat_url,
                callback=self.parse_category
            )

    def parse_category(self, response):
        courses = response.xpath("//a[contains(@class, 'rc-OfferingCard')]")
        for course in courses:
            course_url = course.xpath("./@href").extract_first()
            
            yield scrapy.Request(
                url='https://www.coursera.org%s' % course_url,
                callback=self.parse_course
            )

    def parse_course(self, response):
        yield {
            'title': response.xpath("//title/text()").extract_first()
        } 