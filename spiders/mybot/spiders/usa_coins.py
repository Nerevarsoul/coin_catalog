import scrapy

from ..items import CoinItem, SerieItem


class StateQuaterCoins(scrapy.Spider):
    name = 'state_quater'
    allowed_domains = ['http://collection-coin.ru']
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
        series = series.save()
        table = response.xpath("//table[@class='st']")[0]
        rows = table.xpath(".//tr")
        year = 0
        for row in rows[1:]:
            index = 0
            params = row.xpath(".//td//text()").extract()
            if len(params) == 4:
                index = 2
                year = int(params[0])
            try:
                title = params[index] + ': ' + row.xpath(".//td//a/@title").extract()[0]
            except IndexError:
                title = params[index] + ': ' + params[-1].split('(')[1][:-1]
            coin = CoinItem(
                year=year, country='США', face_value=25,
                currency='центов', theme=title, serie=series,
                is_issued=year < 2018
            )
            coin.save()


class PresidentDollars(scrapy.Spider):
    name = 'president_dollar'
    allowed_domains = ['http://collection-coin.ru']
    start_urls = [
        'http://collection-coin.ru/monety-ssha/spisok-1-dollar-prezidenty-ssha.html',
    ]

    def parse(self, response):
        series = SerieItem(name='1 доллар президенты США', is_active=False, country='США')
        series = series.save()
        table = response.xpath("//table[@class='st']")[0]
        rows = table.xpath(".//tr")
        for row in rows[1:]:
            items = row.xpath(".//td")
            year = items[0].xpath(".//text()").extract()[0].strip()
            if year:
                theme = items[2].xpath(".//a//text()").extract()[0]
                coin_p = CoinItem(
                    year=int(year), country='США', face_value=1, mint='P',
                    currency='доллар', theme=theme, serie=series
                )
                coin_p.save()
                coin_d = CoinItem(
                    year=int(year), country='США', face_value=1, mint='D',
                    currency='доллар', theme=theme, serie=series
                )
                coin_d.save()
