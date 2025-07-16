from django.contrib import admin
from projectapp.models import Employee
from projectapp.models import student

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("ename", "esal", "eadd")

admin.site.register(Employee, EmployeeAdmin)

class studentAdmin(admin.ModelAdmin):
    list_display = ("sid", "sname", "smarks")

admin.site.register(student, studentAdmin)