from datetime import datetime, timedelta

from django_rq import job

from .models import *

__all__ = ('check_serie_amount', 'delete_coins',)


@job
def check_serie_amount():
    series = Serie.objects.all()
    for serie in series:
        catalog_coin_amount = CatalogCoin.objects.filter(serie=serie).count()
        if catalog_coin_amount != serie.coin_amount:
            serie.coin_amount = catalog_coin_amount
            serie.save()


@job
def delete_coins():
    Coin.objects.filter(status='deleted', modified__gt=datetime.now() + timedelta(days=30)).delete()
