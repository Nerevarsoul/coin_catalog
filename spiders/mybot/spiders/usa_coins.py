import scrapy

from ..items import CoinItem, SerieItem


class StateQuaterCoins(scrapy.Spider):
    name = "state_quater"
    allowed_domains = ["http://collection-coin.ru"]
    start_urls = [
        'http://collection-coin.ru/monety-ssha/25-czentov-shtaty-i-territorii-ssha.html',
    ]

    def parse(self, response):
        series = SerieItem(name='25 центов штаты и территории США', is_active=False, country='США')
        series = series.save()
        table = response.xpath("//table[@class='st2']")[0]
        rows = table.xpath(".//tr")
        for row in rows:
            items = row.xpath(".//td//a/@title").extract()
            for item in items:
                data = item.split('центов')[1].split()
                coin = CoinItem(
                    year=int(data[-1][1:5]), country='США', face_value=25,
                    currency='центов', theme=' '.join(data[:-1]), serie=series
                )
                coin.save()


class ParkQuaterCoins(scrapy.Spider):
    name = "park_quater"
    allowed_domains = ["http://collection-coin.ru"]
    start_urls = [
        'http://collection-coin.ru/monety-ssha/spisok-25-czentov-prekrasnaya-amerika.html',
    ]

    def parse(self, response):
        series = SerieItem(name='25 центов Прекрасная Америка', is_active=True, country='США')
        table = response.xpath("//table[@class='st']")[0]
        rows = table.xpath(".//tr")
        year = 0
        for row in rows[1:]:
            index = 0
            params = row.xpath(".//td//text()").extract()
            if len(params) == 4:
                index = 2
                year = int(params[0])    
            title = params[index] + ': ' + row.xpath(".//td//a/@title").extract()[0]
            coin = CoinItem(
                year=year, country='США', face_value=25,
                currency='центов', theme=title, serie=series
            )
            print(coin)
