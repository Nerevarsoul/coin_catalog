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
                    coin_params = []
                    coin_params.append(seria)
                    coin_params.append(fields[0].extract().strip())
                    coin_params.append(fields[1].extract().strip())
                    if len(fields) == 4:
                        coin_params.append(fields[2].extract().strip())
                        coin_params.append(fields[3].extract().strip())
                    else:
                        
                        coin_params.append(fields[2].extract().strip())
                    if coin_item.get('price') and '/' in coin_item.get('price'):
                        price = coin_item.get('price').split('/')
                        coin_item['price'] = price[0]
                        coin_item['mint'] = 'ММД'
                        coin_item.save()
                        coin_item['price'] = price[1]
                        coin_item['mint'] = 'CПМД'
                        coin_item.save()
                    coin_item.save()
    
    @staticmethod
    def save_seria(name):
        seria = SeriaItem()
        seria['name'] = name
        seria['country'] = 'Россия'
        seria.save()

    def save_coin(seria, year, theme, count=None, price=None, mint=None):
        coin_item = CoinItem()
        coin_item['country'] = 'Россия'
        coin_item['seria'] = seria
        coin_item['year'] = year
        coin_item['theme'] = theme
        coin_item['count'] = count
        coin_item['price'] = price
        coin_item['mint'] = mint
        coin_item.save()
