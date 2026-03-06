from django.shortcuts import render

# Create your views here.

def allChai(request):
    return render (request , "Chai/all_chai.html")  


def coffee(request):
    return render (request , "Chai/coffee.html")

def redirectUrl(request):
    return render (request , "Chai/redirecturl.html")