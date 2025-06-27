from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def proapp(request):
    return HttpResponse("proapp")