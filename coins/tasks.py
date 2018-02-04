from django_rq import job

from models import *


@job
def check_serie_amount():
    series = Serie.object.all()
    for serie in series:
        catalog_coin_amount = CatalogCoin.objects.filter(serie=serie).count()
        if catalog_coin_amount != serie.coin_amount:
            serie.coin_amount = catalog_coin_amount
            serie.save()
check_serie_amount.delay()

