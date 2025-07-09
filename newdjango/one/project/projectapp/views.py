from django.shortcuts import render
from projectapp.models import Employee
# Create your views here.
def emp_list_view(request):
    emplist = Employee.objects.all()
    return render(request, "index.html", {"emplist":emplist})