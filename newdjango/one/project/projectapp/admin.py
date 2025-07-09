from django.contrib import admin
from projectapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("ename", "esal", "eadd")

admin.site.register(Employee, EmployeeAdmin)