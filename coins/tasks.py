from django_rq import job, get_scheduler

from .models import *

__all__ = ('check_serie_amount',)


@job
def check_serie_amount():
    series = Serie.objects.all()
    for serie in series:
        catalog_coin_amount = CatalogCoin.objects.filter(serie=serie).count()
        if catalog_coin_amount != serie.coin_amount:
            serie.coin_amount = catalog_coin_amount
            serie.save()

