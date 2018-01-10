import uuid

from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

from core.mixins import CreateUpdateMixin
from .managers import CatalogCoinManager

__all__ = ('CatalogCoin', 'Coin', 'Serie',)


class Serie(CreateUpdateMixin, models.Model):

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    country = models.CharField(
        max_length=50
    )
    name = models.CharField(
        max_length=250,
        unique=True,
    )
    coin_amount = models.IntegerField(
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Serie({self.id})'


class CatalogCoin(CreateUpdateMixin, models.Model):
    
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    country = models.CharField(
        max_length=50
    )
    currency = models.CharField(
        max_length=50
    )
    face_value = models.IntegerField()
    material = models.CharField(
        max_length=150, 
        blank=True, 
        null=True
    )
    weight = models.FloatField(
        blank=True, 
        null=True
    )
    diameter = models.FloatField(
        blank=True, 
        null=True
    )
    thickness = models.FloatField(
        blank=True, 
        null=True
    )
    ruler = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
    )
    year = models.IntegerField(
        blank=True, 
        null=True
    )
    count = models.IntegerField(
        blank=True, 
        null=True
    )
    description = models.TextField(
        blank=True, 
        null=True
    )
    serie = models.ForeignKey(
        Serie,
        on_delete=models.DO_NOTHING, 
        related_name='coins', 
        blank=True, 
        null=True
    )
    catalog_image = models.ImageField(
        upload_to='coin_images', 
        blank=True, 
        null=True
    )
    price = models.FloatField(
        blank=True, 
        null=True
    )
    mint = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
    )
    theme = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
    )
    
    objects = CatalogCoinManager()
    
    def __str__(self):
        return self.par

    def __repr__(self):
        return f'CatalogCoin({self.id})'
        
    def get_absolute_url(self):
        return reverse('catalog_detail_coins', args=[self.id])

    @property
    def par(self):
        return f'{self.face_value} {self.currency}'
    
    
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

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    condition = models.CharField(
        choices=COIN_CONDITION, 
        max_length=50
    )
    catalog_coin = models.ForeignKey(
        CatalogCoin,
        related_name='real_coins',
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    image = models.ImageField(
        upload_to='coin_images',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name='coins'
    )
    status = models.CharField(
        choices=COIN_STATUS, 
        default=DEFAULT_STATUS,
        max_length=20
    )

    def __str__(self):
        return f'{self.catalog_coin} {self.year}'

    def __repr__(self):
        return f'Coin({self.id})'
