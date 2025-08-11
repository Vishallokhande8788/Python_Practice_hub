from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class page2(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    pageName = models.CharField(max_length=100)

    def __str__(self):
        return f"Author:{self.author.username} PageName:{self.pageName}"