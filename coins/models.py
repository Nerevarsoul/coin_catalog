from django.contrib.postgres.fields import IntegerRangeField
from django.core.urlresolvers import reverse
from django.db import models

from accounts.models import User
from core.mixins import CreateUpdateMixin
from core.models import Image

__all__ = ('CatalogCoin', 'Coin',)


class CatalogCoin(CreateUpdateMixin, models.Model):
    
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    face_value = models.IntegerField()
    material = models.CharField(max_length=150, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    diameter = models.FloatField(blank=True, null=True)
    thickness = models.FloatField(blank=True, null=True)
    ruler = models.CharField(max_length=50, blank=True, null=True)
    circulation = IntegerRangeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    catalog_image = models.ManyToManyField(Image)
    slug = models.SlugField(max_length=150)
    
    def __str__(self):
        return self.par

    def __repr__(self):
        return "CatalogCoin({})".format(self.id)
        
    def get_absolute_url(self):
        return reverse('catalog_detail_coins', args=[self.slug])

    @property
    def par(self):
        return "{} {}".format(self.face_value, self.currency)
    
    
class Coin(CreateUpdateMixin, models.Model):

    COIN_STATUS = (
        ('in_collection', 'в коллекции'),
        ('for_exchange', 'на обмен'),
        ('in_wishlist', 'в списке желаний'),
    )

    COIN_CONDITION = (
        ('unknown', 'неизвестно'),
    )

    DEFAULT_STATUS = COIN_STATUS[0][0]
    DEFAULT_CONDITION = COIN_CONDITION[0][0]

    condition = models.CharField(choices=COIN_CONDITION, max_length=50)
    year = models.IntegerField(blank=True, null=True)
    mint = models.CharField(max_length=50, blank=True, null=True)
    catalog_coin = models.ForeignKey(CatalogCoin, blank=True, null=True)
    image = models.ManyToManyField(Image)
    owner = models.ForeignKey(User, related_name="coins")
    status = models.CharField(choices=COIN_STATUS, default=DEFAULT_STATUS, max_length=20)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.catalog_coin, self.year)

    def __repr__(self):
        return "Coin({})".format(self.id)
