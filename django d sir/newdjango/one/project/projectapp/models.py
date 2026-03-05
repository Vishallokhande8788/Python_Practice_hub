from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eadd = models.CharField(max_length=100)

class student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    smarks = models.IntegerField()
    