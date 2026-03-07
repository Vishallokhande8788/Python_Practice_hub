from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.

chais = ChaiVariety.objects.all()

def allChai(request):
    return render (request , "Chai/all_chai.html" ,{"chais" : chais})


def coffee(request):
    return render (request , "Chai/coffee.html")

def redirectUrl(request):
    return render (request , "Chai/redirecturl.html")