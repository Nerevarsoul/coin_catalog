import re
import unicodedata

import scrapy

from ..items import CoinItem, Serie


class EuroCoinsParser(object):
    PARAMETER_MAP = {
        'Страна:': 'set_country',
        'Годы выпуска:': 'set_year',
        'Номинал': 'set_par',
        'Материал': 'set_material',
        'Масса': 'set_weight',
        'Диаметр': 'set_diameter',
        'Толщина': 'set_thickness',
    }

    def __init__(self, coin, parameters):
        self.coin = coin
        self.parameters = self.normilize_parameters(parameters)

    @staticmethod
    def normilize_parameters(parameters):
        return [unicodedata.normalize("NFKD", p.strip()) for p in parameters]
    
    def parse_parameters(self):
        for i, parameter in enumerate(self.parameters):
            method = self.PARAMETER_MAP.get(parameter)
            if method:
                getattr(self, self.PARAMETER_MAP[parameter])(i)

    def set_country(self, i):
        self.coin['country'] = self.parameters[i+1]

    def set_year(self, i):
        print(self.parameters[i + 1])
        digits = [d for d in re.split(' |-', self.parameters[i + 1]) if d.isdigit()]
        print(digits)
        self.coin['year'] = (digits[0], digits[1] if len(digits) != 1 else digits[0])

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


class BaseEuro(scrapy.Spider):
    allowed_domains = ["http://www.euro-coins.info/"]

    def parse(self, response):
        dd = response.xpath("//dd[contains(@class, 'active')]")[0]
        urls = dd.xpath(".//a/@href").extract()
        for url in urls:
            yield scrapy.Request(url, dont_filter=True, callback=self.parse_page)

    def parse_page(self, response):
        pass


class EuroCoins(BaseEuro):
    name = "eurocoins"
    allowed_domains = ["http://www.euro-coins.info/"]
    start_urls = [
        "http://www.euro-coins.info/euro.html",
    ]
    NEEDLESS = (
        'finland', 'san-marino', 'euro-total', 'belgium', 'vatican', 'spain', 'monaco', 'netherlands', 'total',
    )

    def parse_page(self, response):
        entries = response.xpath("//div[@class='entry']")

        for entry in entries:
            coin = CoinItem()
            parameters = entry.xpath(".//td//text()").extract()
            parser = EuroCoinsParser(coin, parameters)
            parser.parse_parameters()
            coin['serie'] = '0261600c-5202-425b-b516-6171464a6960'
            coin.save()


class EuroCoinsMintage(BaseEuro):
    name = 'eurocoinsmintage'
    start_urls = [
        'https://www.euro-coins.info/info/mintage.html',
    ]

    VALUE = (1, 2, 5, 10, 20, 50, 1, 2, 2, 2, 2,)
    CENTS = 'евроцентов'
    EURO = 'евро'
    CURRENCY = ('евроцент', 'евроцента', CENTS, CENTS, CENTS, CENTS, EURO, EURO, EURO, EURO, EURO)

    def parse_page(self, response):
        SERIE = Serie.objects.get(id='ad7279ee-57ba-4fe9-a9af-3caca31acdfc')
        COMMEMORATIVE_SERIE = Serie.objects.get(id='a30d8bc8-e242-4764-9386-635aa3c7d750')
        EURO_SERIE = Serie.objects.get(id='d65bec1c-65d5-4be4-81bf-fd6c490d6620')
        ROME_SERIE = Serie.objects.get(id='b4b3e1fa-4846-4b2d-8ff6-6453525a2830')
        FLAG_SERIE = Serie.objects.get(id='745b1f74-1710-460e-9cfb-14cd38c0acfe')
        ALLIANCE_SERIE = Serie.objects.get(id='e914f8e9-ca18-4224-9228-8dd494a1f16e')
        SERIE_MAP = {2007: ROME_SERIE, 2009: ALLIANCE_SERIE, 2012: EURO_SERIE, 2015: FLAG_SERIE}

        country = response.xpath("//dt[contains(@class, 'active')]//div//text()").extract()[0]
        entries = response.xpath("//table[@class='mintage']//tr[@class='total']")

        for entry in entries:
            offset = 1
            themes = entry.xpath(".//td//abbr/@title").extract()
            row = entry.xpath(".//td//text()").extract()
            if '*' in row[0]:
                continue
            for sign in ('\n', '1', '2', '\xa0',):
                try:
                    row.remove(sign)
                except ValueError:
                    pass
            year = int(row[0])
            mint = row[1]
            for i, mintage in enumerate(row[2:]):
                mintage = ''.join(mintage.split('.'))
                if mintage.isdigit():
                    coin = CoinItem(
                        year=year, country=country, mint=mint, face_value=self.VALUE[i],
                        currency=self.CURRENCY[i], mintage=int(mintage)
                    )
                    if i > 7:
                        try:
                            coin['theme'] = themes[offset]
                            offset += 1
                        except IndexError:
                            coin['theme'] = themes[offset-1]
                        if i != 10:
                            coin['serie'] = COMMEMORATIVE_SERIE
                        else:
                            try:
                                coin['serie'] = SERIE_MAP[coin['year']]
                            except KeyError:
                                coin['serie'] = COMMEMORATIVE_SERIE
                    else:
                        coin['serie'] = SERIE
                    if coin['currency'] == self.EURO:
                        coin['material'] = 'биметалл'
                    coin.save()
