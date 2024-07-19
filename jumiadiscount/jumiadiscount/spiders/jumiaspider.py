import scrapy


class JumiaspiderSpider(scrapy.Spider):
    name = "jumiaspider"
    allowed_domains = ["www.jumia.co.ke"]
    start_urls = ["https://www.jumia.co.ke/"]

    def parse(self, response):
        pass
