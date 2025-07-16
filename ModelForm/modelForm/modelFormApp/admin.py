from django.contrib import admin
from modelFormApp.models import modelForm

# Register your models here.

class modelFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'address', 'image')

admin.site.register(modelForm, modelFormAdmin)
