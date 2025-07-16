from django.contrib import admin
from modelformapp.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pname','price','quantity')
admin.site.register(Product,ProductAdmin)