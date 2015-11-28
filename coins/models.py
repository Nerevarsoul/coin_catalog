from django.db import models


# Create your models here.
class Coins(models.Model):
	
	country = models.CharField(max_length=50)
	year = models.IntegerField()
	currency = models.CharField(max_length=50)
	face_value = models.IntegerField()
	mint = models.CharField(max_length=50)
	metal = models.CharField(max_length=50)
	ruler = models.CharField(max_length=50)
	number = models.CharField(max_length=50)
	circulation = models.IntegerField()
	condition = models.CharField(max_length=50)