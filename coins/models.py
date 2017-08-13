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

    COIN_STATUS = (
        ('in_collection', 'в коллекции'),
        ('for_exchange', 'на обмен'),
        ('in_wishlist', 'в списке желаний'),
    )

    COIN_MINT = (
        ('unknown', 'неизвестно'),
    )

    DEFAULT_STATUS = COIN_STATUS[0][0]
    DEFAULT_MINT = COIN_MINT[0][0]

    condition = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    mint = models.CharField(choices=COIN_MINT, default=DEFAULT_MINT, max_length=20)
    catalog_coin = models.ForeignKey(CatalogCoin, blank=True, null=True)
    image = models.ManyToManyField(Image)
    owner = models.ForeignKey(User, related_name="coins")
    status = models.CharField(choices=COIN_STATUS, default=DEFAULT_STATUS, max_length=20)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.catalog_coin, self.year)

    def __repr__(self):
        return "Coin({})".format(self.id)


class Trade(CreateUpdateMixin, models.Model):

    # creator = models.ForeignKey(User)
    # partner = models.ForeignKey(User)
    # creator_offer = models.ManyToManyField(Coin)
    # partner_offer = models.ManyToManyField(Coin)
    state = FSMField(default='new')

    def __str__(self):
        return "{} {}".format(self.catalog_coin, self.year)

    def __repr__(self):
        return "Trade({})".format(self.id)
