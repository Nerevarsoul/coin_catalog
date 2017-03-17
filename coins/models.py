from django.core.urlresolvers import reverse
from django.db import models

from django_fsm import FSMField, transition

from accounts.models import User
from core.mixins import CreateUpdateMixin
from core.models import Country, Image


class CatalogCoin(CreateUpdateMixin, models.Model):
    
    country = models.ForeignKey(Country)
    currency = models.CharField(max_length=50)
    face_value = models.IntegerField()
    metal = models.CharField(max_length=50, blank=True, null=True)
    ruler = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    circulation = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    catalog_image = models.ManyToManyField(Image)
    slug = models.SlugField(max_length=150)
    
    def __str__(self):
        return "{} {}".format(self.face_value, self.currency)

    def __repr__(self):
        return "CatalogCoin({})".format(self.id)
        
    def get_absolute_url(self):
        return reverse('catalog_detail_coins', args=[self.slug])
    
    
class Coin(CreateUpdateMixin, models.Model):

    condition = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField()
    mint = models.CharField(max_length=50, blank=True, null=True)
    catalog_coin = models.ForeignKey(CatalogCoin)
    image = models.ManyToManyField(Image)
    available = models.ForeignKey(User, blank=True, null=True,
                                  related_name="user_have")
    needful = models.ForeignKey(User, blank=True, null=True,
                                related_name="user_wish")
    changable = models.ForeignKey(User, blank=True, null=True,
                                  related_name="user_change")

    def __str__(self):
        return "{} {}".format(self.catalog_coin, self.year)

    def __repr__(self):
        return "Coin({})".format(self.id)


class Trade(CreateUpdateMixin, models.Model):

    creator = models.ForeignKey(User)
    partner = models.ForeignKey(User)
    creator_offer = models.ManyToManyField(Coin)
    partner_offer = models.ManyToManyField(Coin)
    state = FSMField(default='new')

    def __str__(self):
        return "{} {}".format(self.catalog_coin, self.year)

    def __repr__(self):
        return "Trade({})".format(self.id)
