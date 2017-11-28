from copy import copy

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
            for i, box in enumerate(coin_box):
                self.save_seria(series[i].extract().strip())
                coins = box.xpath(".//tr[not(@class)]")
                for coin in coins: 
                    fields = coin.xpath(".//td//text()")
                    coin_params = {}
                    coin_params.update({'seria': seria})
                    coin_params.update({'year': fields[0].extract().strip()})
                    coin_params.update({'theve': fields[1].extract().strip()})
                    if len(fields) == 4:
                        coin_params.update({'price': fields[2].extract().strip()})
                        coin_params.update({'count': fields[3].extract().strip()})
                    else:
                        coin_params.update({'price': fields[2].extract().strip()})
                    if coin_item.get('price') and '/' in coin_item.get('price'):
                        price = coin_item.get('price').split('/')
                        coin_item['price'] = price[0]
                        coin_item['mint'] = 'ММД'
                        coin_item1 = copy(coin_item)
                        coin_item1['price'] = price[1]
                        coin_item1['mint'] = 'CПМД'
                        self.save_coin(coin_item1)
                    self.save_coin(coin_item)

    
    @staticmethod
    def save_seria(name):
        seria = SerieItem()
        seria['name'] = name
        seria['country'] = 'Россия'
        seria.save()

    @staticmethod
    def save_coin(**kwargs):
        coin_item = CoinItem()
        coin_item['country'] = 'Россия'
        coin_item['seria'] = kwargs.get('seria')
        coin_item['year'] = kwargs.get('year')
        coin_item['theme'] = kwargs.get('theme')
        coin_item['count'] = kwargs.get('count')
        if kwargs.get('price').isnumber():
            coin_item['price'] = kwargs.get('price')
        coin_item['mint'] = kwargs.get('mint')
        coin_item.save()
