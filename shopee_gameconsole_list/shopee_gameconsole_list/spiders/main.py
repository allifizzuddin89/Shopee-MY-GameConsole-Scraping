import scrapy


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
