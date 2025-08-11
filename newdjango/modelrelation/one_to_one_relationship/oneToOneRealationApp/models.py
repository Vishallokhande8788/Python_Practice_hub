from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class page(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    pageName = models.CharField(max_length=100)

    def __str__(self):
        return f"Author:{self.author.username} PageName:{self.pageName}"
    
