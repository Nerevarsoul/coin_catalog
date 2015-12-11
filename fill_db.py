#!/.virtualenvs/coins/bin python
# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

import os
import sys
import random
import django

def create_country():

    country_name = ("США", "Великобритания", "Китай", "Индия", "Швеция", "Испания",
                    "Италия", "Франция", "Бразилия", "Канада", "Австралия")

    for name in country_name:
        country = Country(name=name, status=2)
        country.save()


def create_catalog_coins():

    nominal_list = [1, 2, 5, 10, 15, 20, 25, 50, 100, 200, 500, 1000]

    countrys = Country.objects.all()

    currency_list = ("евро", "франк", "Песо", "Доллар", "Лира", "Крона", "Рупия", "Юань")

    metal_list = ("серебро", "никель", "аллюминий", "медь")

    for i in xrange(100):
        country = random.choice(countrys)
        nominal = random.choice(nominal_list)
        currency = random.choice(currency_list)
        metal = random.choice(metal_list)
        new_coin = CatalogCoins(country=country,
                                face_value=nominal, 
                                currency=currency,
                                metal=metal
                                )
        new_coin.save()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()

    from django.contrib.auth.models import User
    from django.core.files import File

    from coins.models import UserProfile, Country, Address, CatalogCoins, Coins

    # from mysite.settings import MEDIA_ROOT

    # create_country()

    # create_catalog_coins()
