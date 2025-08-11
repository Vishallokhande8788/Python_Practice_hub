from django.contrib import admin
from classviewsapp.models import beer

# Register your models here.
class beerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'color')

admin.site.register(beer, beerAdmin)