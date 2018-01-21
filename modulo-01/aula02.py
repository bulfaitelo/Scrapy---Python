import scrapy

class BullSpider(scrapy.Spider):
    name = 'bulfaitelo'
    start_urls = ['https://bulfaitelo.com.br']

    def parse(self, response):
        self.log('helo word')
        self.log(response.body)