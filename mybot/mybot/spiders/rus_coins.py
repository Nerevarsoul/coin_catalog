import scrapy

from ..items import EuroCoinsItem


class RusCoins(scrapy.Spider):
    name = "ruscoins"
    allowed_domains = ["http://moneta-russia.ru/"]
    start_urls = [
        "http://moneta-russia.ru/library/yubileynye-monety-10-rubley.php",
    ]

    def parse(self, response):
        tables = response.xpath("//div[contains(@class, 'tabs_block')]")
        for table in tables:
            series = table.xpath(".//ul[contains(@class, 'tabs')]//li//text()")
            coin_box = table.xpath(".//div[contains(@class, 'box')]")
            for box, i in enumerate(coin_box):
                seria = series[i].extract().split()
                coins = box.xpath(".//tr[not(@class)]")
                for coin in coins:
                    fields = coin.xpath(".//td//text()")
                    year = fields[0].extract().split()
                    name = fields[1].extract().split()
                if len(fields) == 4:
                    count = fields[2].extract().split()
                    price = fields[3].extract().split()
                else:
                    count = fields[3].extract().split()

