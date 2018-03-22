import uuid

from django.urls import reverse
from django.db import models

from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

from accounts.models import User
from .managers import *

__all__ = ('CatalogCoin', 'Coin', 'Serie',)


class Serie(TimeStampedModel, MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']

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
    parent = TreeForeignKey(
        'self', null=True, blank=True, 
        related_name='children', db_index=True, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Serie({self.id})'


class CatalogCoin(TimeStampedModel):
    
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
    crause_number = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    my_number = models.CharField(
        max_length=10,
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
        if self.theme:
            return f'{self.face_value} {self.currency} {self.year} {self.theme}'
        else:
            return f'{self.face_value} {self.currency} {self.year}'
    
    
class Coin(TimeStampedModel):

    COIN_STATUS = (
        ('in_collection', 'в коллекции'),
        ('for_exchange', 'на обмен'),
        ('in_wishlist', 'в списке желаний'),
        ('in_storage', 'в запаснике'), 
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
        max_length=50,
        default=DEFAULT_CONDITION
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
        blank=True,
        null=True
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

    objects = CoinManager()

    def __str__(self):
        return f'{self.catalog_coin}'

    def __repr__(self):
        return f'Coin({self.id})'
