import django_tables2 as tables
from .models import Coins


class CoinsTable(tables.Table):
    class Meta:
        model = Coins
        # attrs = {"class": "paleblue"}
