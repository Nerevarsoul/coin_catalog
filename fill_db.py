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


def create_coins():

    nominal_list = [1, 2, 5, 10, 15, 20, 25, 50, 100, 200, 500, 1000]

    series = ['Christmas Series', 'Starbucks', 'Special Edition', 
              'Regional Series', 'Small card']

    issued_on = [2001, 2003, 2005, 2009, 2010, 2012]

    for card in name_list:
        new_country = random.choice(country)
        new_series = random.choice(series)
        year = random.choice(issued_on)
        catalog_codes = str(name_list.index(card))
        face_picture = open(os.path.join(MEDIA_ROOT, 'cards', card + '.jpg'))
        reverse_picture = open(os.path.join(MEDIA_ROOT, 'cards', card + '-back.jpg'))
        new_card = Card(name=card, country=new_country, series=new_series, 
                        issued_on=year, catalog_codes=catalog_codes, 
                        face_picture=File(face_picture),
                        reverse_picture=File(reverse_picture))
        new_card.save()




if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()

    from django.contrib.auth.models import User
    from django.core.files import File

    from coins.models import UserProfile, Country, Address, CatalogCoins, Coins

    # from mysite.settings import MEDIA_ROOT

    create_country()