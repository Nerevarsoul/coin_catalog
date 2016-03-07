import django_tables2 as tables
from .models import CatalogCoin


class CoinsTable(tables.Table):
    class Meta:
        model = CatalogCoin
        # attrs = {"class": "paleblue"}
