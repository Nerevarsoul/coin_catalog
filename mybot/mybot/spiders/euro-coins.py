import scrapy

#  from ..items import EuroCoinsItem


class EuroCoins(scrapy.Spider):
    name = "eurocoins"
    allowed_domains = ["http://www.euro-coins.info/"]
    start_urls = [
        "http://www.euro-coins.info/euro.html",
    ]

    @staticmethod
    def parse_parameters(parameters):
        pass

    def parse(self, response):
        dds = response.xpath("//dd[contains(@class, 'level1')]")
        for dd in dds:
            url = dd.xpath(".//a[contains(@href, 'spain')]").extract()
            yield scrapy.Request(url, dont_filter=True, callback=self.parse_page)

    def parse_page(self, response):
        entries = response.xpath("//div[@class='entry']")

        for entry in entries:
            parameters = entry.select(".//td//text()").extract()
            self.parse_parameters(parameters)
