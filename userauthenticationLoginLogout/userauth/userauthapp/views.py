from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'userauthapp/home.html')


@ login_required
def pyExam(request):
    return render(request, 'userauthapp/python.html')