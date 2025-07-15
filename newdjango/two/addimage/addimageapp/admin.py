from django.contrib import admin
from addimageapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid','ename','esal' , 'eimg')

admin.site.register(Employee,EmployeeAdmin)

