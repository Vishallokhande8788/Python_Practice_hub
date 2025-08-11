from django.db import models
from django.urls import reverse

# Create your models here.

class beer(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=100)

def get_absolute_url(self):
    return reverse("list")