import re

import scrapy

from ..items import EuroCoinsItem


NEEDLESS = ('finland', 'san-marino', 'euro-total', 'belgium', 'vatican', 'spain', 'monaco', 'netherlands')


class EuroCoinsParser(object):
    PARAMETER_MAP = {
        'Страна: ': 'set_country',
        'Годы выпуска: ': 'set_circulation',
        'Номинал': 'set_par',
        'Материал': 'set_material',
        'Масса': 'set_weight',
        'Диаметр': 'set_diameter',
        'Толщина': 'set_thickness',
    }

    def __init__(self, coin, parameters):
        self.coin = coin
        self.parameters = parameters

    def parse_parameters(self):
        for i, parameter in enumerate(self.parameters):
            method = self.PARAMETER_MAP.get(parameter)
            if method:
                getattr(self, self.PARAMETER_MAP[parameter])(i)

    def set_country(self, i):
        self.coin['country'] = self.parameters[i+1]

    def set_circulation(self, i):
        digits = [d for d in re.split(' |-', self.parameters[i + 1]) if d.isdigit()]
        self.coin['circulation'] = (digits[0], digits[1] if len(digits) != 1 else None)

    def set_par(self, i):
        par = self.parameters[i + 5].split()
        self.coin['currency'] = par[0]
        self.coin['face_value'] = par[1]

    def set_material(self, i):
        self.coin['material'] = self.parameters[i + 5]

    def set_weight(self, i):
        self.coin['weight'] = self.parameters[i + 5].split()[0]

    def set_diameter(self, i):
        self.coin['diameter'] = self.parameters[i + 5].split()[0]

    def set_thickness(self, i):
        self.coin['thickness'] = self.parameters[i + 5].split()[0]


class EuroCoins(scrapy.Spider):
    name = "eurocoins"
    allowed_domains = ["http://www.euro-coins.info/"]
    start_urls = [
        "http://www.euro-coins.info/euro.html",
    ]

    def parse(self, response):
        dds = response.xpath("//dd[contains(@class, 'level1')]")
        for dd in dds[:1]:
            urls = dd.xpath(".//a/@href").extract()
            for url in urls:
                if url.split('/')[-1].split('.')[0] not in NEEDLESS:
                    yield scrapy.Request(url, dont_filter=True, callback=self.parse_page)

    def parse_page(self, response):
        entries = response.xpath("//div[@class='entry']")

        for entry in entries:
            coin = EuroCoinsItem()
            parameters = entry.xpath(".//td//text()").extract()
            parser = EuroCoinsParser(parameters, coin)
            parser.parse_parameters()
            coin.save()
