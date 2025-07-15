from django.shortcuts import render
from addimageapp import views
from addimageapp.models import Employee
from addimageapp.forms import EmployeeForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    form = EmployeeForm()
    print("get request")
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')
        return render(request,'home.html', {'form': form})

def index(request):
    emps = Employee.objects.all()
    return render(request, 'home.html', {'emps':emps})
