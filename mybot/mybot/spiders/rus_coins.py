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
                seria = self.save_seria(series[i].extract().strip())
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
                    if coin_params.get('price') and '/' in coin_params.get('price'):
                        price = coin_params.get('price').split('/')
                        coin_params['price'] = price[0]
                        coin_params['mint'] = 'ММД'
                        coin_params1 = copy(coin_params)
                        coin_params1['price'] = price[1]
                        coin_params1['mint'] = 'CПМД'
                        self.save_coin(**coin_params1)
                    self.save_coin(**coin_params)

    
    @staticmethod
    def save_seria(name):
        seria = SerieItem()
        seria['name'] = name
        seria['country'] = 'Россия'
        return seria.save()

    @staticmethod
    def save_coin(**kwargs):
        coin_item = CoinItem()
        coin_item['country'] = 'Россия'
        coin_item['face_value'] = 10
        coin_item['currency'] = 'рубль'
        coin_item['serie'] = kwargs.get('seria')
        coin_item['year'] = kwargs.get('year')
        coin_item['theme'] = kwargs.get('theme')
        coin_item['count'] = kwargs.get('count')
        if kwargs.get('price').isdigit():
            coin_item['price'] = kwargs.get('price')
        coin_item['mint'] = kwargs.get('mint')
        coin_item.save()
