import uuid

from django.urls import reverse
from django.db import models

from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

from accounts.models import User
from .managers import *

__all__ = ('CatalogCoin', 'Coin', 'Serie', 'Country',)


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

    objects = SeriesManager()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Series({self.id})'


class CatalogCoin(TimeStampedModel):
    class Meta:
        unique_together = (('serie', 'theme'),)
    
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    country = models.CharField(
        help_text='Страна выпуска',
        max_length=50
    )
    currency = models.CharField(
        max_length=50
    )
    face_value = models.IntegerField()
    material = models.CharField(
        help_text='Материал изготовления',
        max_length=150, 
        blank=True, 
        null=True
    )
    weight = models.FloatField(
        help_text='Вес',
        blank=True, 
        null=True
    )
    diameter = models.FloatField(
        help_text='Диаметр',
        blank=True, 
        null=True
    )
    thickness = models.FloatField(
        help_text='Толщина',
        blank=True, 
        null=True
    )
    ruler = models.CharField(
        help_text='Правитель изображенный на монете',
        max_length=50, 
        blank=True, 
        null=True
    )
    year = models.IntegerField(
        help_text='Год выпуска',
        blank=True, 
        null=True
    )
    mintage = models.IntegerField(
        help_text='Тираж',
        blank=True, 
        null=True
    )
    description = models.TextField(
        help_text='Описание',
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
    series = models.ManyToManyField(
        Serie,
        related_name='series_coins',
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
        help_text='Монетный двор',
        max_length=50, 
        blank=True, 
        null=True
    )
    theme = models.CharField(
        max_length=250,
        blank=True, 
        null=True
    )
    crause_number = models.CharField(
        help_text='Номер по каталогу Краузе',
        max_length=10,
        blank=True,
        null=True
    )
    my_number = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    is_issued = models.BooleanField(
        help_text='Выпущена или запланирована',
        default=True
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
        ('exchanged', 'обмененно'),
    )

    COIN_CONDITION = (
        ('unknown', 'неизвестно'),
        ('proof', 'proof'),
        ('BU', 'BU'),
        ('UNC', 'UNC'),
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
        related_name='coins',
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
    source = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    objects = CoinManager()

    def __str__(self):
        return f'{self.catalog_coin}'

    def __repr__(self):
        return f'Coin({self.id})'


class Country(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    flag = models.CharField(max_length=2, blank=True, null=True)
    union = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
