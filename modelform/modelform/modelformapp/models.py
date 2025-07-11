from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField()
    price = models.FloatField()
    quantity = models.IntegerField()
    