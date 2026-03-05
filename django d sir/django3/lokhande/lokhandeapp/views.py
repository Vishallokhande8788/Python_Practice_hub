from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lokhande(request):
    return HttpResponse("Hello lokhande.")