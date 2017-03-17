from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals


COUNTRY_STATUS = (
    (1, 'Не существующая'),
    (2, 'Существующая'),
)


class Image(models.Model):

    image = models.ImageField(upload_to='coin_images',)


class Country(models.Model):

    name = models.CharField(max_length=50)
    status = models.IntegerField(choices=COUNTRY_STATUS)
    slug = models.SlugField(max_length=55)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('country_view', args=[self.slug])
