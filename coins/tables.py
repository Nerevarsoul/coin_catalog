import django_tables2 as tables
from .models import CatalogCoins


class CoinsTable(tables.Table):
    class Meta:
        model = CatalogCoins
        # attrs = {"class": "paleblue"}
