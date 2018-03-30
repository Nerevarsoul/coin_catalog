import scrapy

from ..items import CoinItem, SerieItem


class StateQuaterCoins(scrapy.Spider):
    name = "statequater"
    allowed_domains = ["http://collection-coin.ru"]
    start_urls = [
        'http://collection-coin.ru/monety-ssha/25-czentov-shtaty-i-territorii-ssha.html',
    ]

    def parse(self, response):
        series = SerieItem(name='25 центов штаты и территории США', is_active=False, country='США')
        table = response.xpath("//table(@class, 'st2')")
        rows = table.xpath("//tr")
        for row in rows:
            items = row.xpath(".//td//a/@title").extract()
            for item in items:
                data = item.split('центов')[1].split()
                coin = CoinItem(
                    year=int(data[1][1:5]), country='США', face_value=25,
                    currency='центов', theme=data[0].strip(), serie=series
                )
                print(coin)
