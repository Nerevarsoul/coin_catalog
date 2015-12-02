from django.views.generic.base import TemplateView

from django_tables2 import SingleTableView

from .models import *
from .tables import *


# Create your views here.
class IndexView(TemplateView):

	template_name = "index.html"


class CoinsTableView(SingleTableView):
    model = Coins
    table_class = CoinsTable
    template_name = "coins.html"
