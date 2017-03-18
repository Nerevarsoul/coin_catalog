import json
import scrapy

from ..items import EuroCoinsItem


class EuroCoins(scrapy.Spider):
    name = "eurocoins"
    allowed_domains = ["http://www.euro-coins.info/"]
    start_urls = [
        "http://www.euro-coins.info/euro.html",
    ]

    def parse(self, response):
        num_pages = int(response.xpath('//div[@class="noItems"]/span[@class="bFont"][last()]/text()').re(r'(\d+)')[0])
        sid = response.xpath('//a[contains(@href, "sid")]/@href').re(r'sid=(\w+)(?!&|\z)')[0]

        base_url = 'http://bigbasket.com/product/facet/get-page/?'
        for page in range(1, num_pages/20 + 1):
            yield scrapy.Request(base_url + urllib.urlencode({'sid': sid, 'page': str(page)}), dont_filter=True, callback=self.parse_page)

    def parse_page(self, response):
        data = json.loads(response.body)

        selector = scrapy.Selector(text=data['products'])
        for product in selector.xpath('//li[starts-with(@id, "product")]'):
            title = product.xpath('.//div[@class="muiv2-product-container"]//img/@title').extract()[0]
            print title
