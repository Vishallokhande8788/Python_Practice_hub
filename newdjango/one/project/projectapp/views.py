from django.shortcuts import render
from projectapp.models import Employee
from projectapp.models import student
# Create your views here.
def emp_list_view(request):
    emplist = Employee.objects.all()
    return render(request, "index.html", context={"emplist":emplist})

def hii_view(request):
    name = 'vishal'
    age = 25
    marks = 100

    return render(request, "student.html", context={"name":name, "age":age, "marks":marks})

def stu_view(request):
    stu_list = student.objects.all()
    return render(request, "student.html", context={"stu_list":stu_list})