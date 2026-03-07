from django.db import models
from django.utils import timezone
# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML" , 'MASALA'),
        ("GR" , 'GINGER'),
        ("SL" , 'SILI'),
        ("KL" , 'KALE'),
        ("EL" , 'ELLCHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE) 

    def __str__(self):
        return self.name