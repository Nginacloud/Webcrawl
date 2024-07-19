import scrapy


class JumiaspiderSpider(scrapy.Spider):
    name = "jumiaspider"
    allowed_domains = ["www.jumia.co.ke"]
    start_urls = ["https://www.jumia.co.ke/"]

    def parse(self, response):
        for products in response.css('div.itm.col'):
            yield{
                'name': products.css('div.name::text').get(),
                'original_price': products.css('div.prc::attr(data-oprc)').get(),
                'discount_percentage': products.css('div.bdg._dsct').get(),
                'discounted_price': products.css('div.prc::text').get(),
                'url': products.css('a.core::attr(href)').get(),
            }