from django.contrib import admin
from django.utils.html import format_html
from modelFormApp.models import modelForm

class modelFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'address', 'show_image')

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="20" height="20" style="object-fit: cover;" />', obj.image.url)
        return "No Image"

    show_image.short_description = 'Profile Image'

admin.site.register(modelForm, modelFormAdmin)
