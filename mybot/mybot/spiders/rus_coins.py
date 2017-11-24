import scrapy

from ..items import CoinItem, SerieItem


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
                seria = SeriaItem()
                seria['name'] = series[i].extract().split()
                seria['country'] = 'Россия'
                coins = box.xpath(".//tr[not(@class)]")
                for coin in coins:
                    coin_item = CoinItem() 
                    fields = coin.xpath(".//td//text()")
                    coin_item['year'] = fields[0].extract().split()
                    coin_item['name'] = fields[1].extract().split()
                if len(fields) == 4:
                    coin_item['count'] = fields[2].extract().split()
                    coin_item['price'] = fields[3].extract().split()
                else:
                    coin_item['price'] = fields[3].extract().split()

