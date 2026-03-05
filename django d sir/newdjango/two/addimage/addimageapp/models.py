from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.IntegerField()
    eimg=models.ImageField(upload_to='images/')