from django.contrib import admin
from modelFormApp.models import modelForm

# Register your models here.
list_display = ('name', 'age', 'gender', 'address', 'image')

admin.site.register(modelForm, list_display)