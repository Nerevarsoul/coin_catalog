from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import CatalogCoin


@receiver(post_save, sender=CatalogCoin)
def catalog_coin_post_save_receiver(sender, instance, created, **kwargs):
    if instance.serie and created:
        instance.serie.amount += 1
        instance.serie.save()


@receiver(pre_delete, sender=CatalogCoin)
def catalog_coin_pre_delete_receiver(sender, instance, **kwargs):
    if instance.serie:
        instance.serie.amount -= 1
        instance.serie.save()
