from django.contrib import admin
from .models import ChaiVarity, ChaiCertificate, ChaiReview, Store


# Inline for reviews (One-to-Many)
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2


# ChaiVarity Admin
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]


# Store Admin (Many-to-Many)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)   # ✅ Correct way for ManyToMany fields


# ChaiCertificate Admin (One-to-One)
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')   # ✅ removed extra space in 'chai'


# Register models in Admin
admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
    