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


def create_users():
    username_list = ['Lantash', 'Shiori', 'Kaito', 'Mio', 'Mia', 
                     'Cane', 'Sutter', 'Blazi', 'Kitty', 'Nirtok']

    email_list = ['Lantash@gmail.com', 'Shiori@mail.ru', 'Kaito@yandex.ru', 
                  'Mio@gmail.com', 'Mia@gmail.com', 'Cane@mail.ru', 
                  'Sutter@mail.ru', 'Blazi@gmail.com', 'Kitty@mail.ru', 
                  'Nirtok@yandex.ru']

    password_list = ['1q', '2w', '3e', '4r', '5t', '6y', '7u', '8i', '9o', '0p']

    first_name_list = ['Bob', 'Cristy', 'Maya', 'Alex', 'Rodger', 
                       'Kei', 'Alice', 'Charlie', 'Donna', 'Luis']

    last_name_list = ['Specter', 'Litt', 'Hardman', 'Pirson', 'Depp', 
                      'Beckham', 'Ross', 'Zein', 'Truman', 'Stalin']


    for i in xrange(10):
        user = User.objects.create_user(username_list[i], email_list[i], password_list[i])
        user.last_name = last_name_list[i]
        user.first_name = first_name_list[i]
        user.save()


def create_coins():

    status_list = ('available', 'needful', 'changable')
    year = random.randrange(1875, 2015)

    catalog_coins = CatalogCoins.objects.all()
    users = User.objects.all()
    for i in range(1000):
        coin = Coins(catalog_coin=random.choice(catalog_coins),
                     year=year)
        setattr(coin, random.choice(status_list), random.choice(users))
        coin.save()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()

    from django.contrib.auth.models import User
    from django.core.files import File

    from coins.models import UserProfile, Country, Address, CatalogCoins, Coins

    # from mysite.settings import MEDIA_ROOT

    create_country()

    create_catalog_coins()

    create_users()

    create_coins()
