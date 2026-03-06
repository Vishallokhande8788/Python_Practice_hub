from django.http import HttpResponse
from  django.shortcuts import render

def home(request):
    return HttpResponse("hello you are at home ")


def about(request):
    return HttpResponse("hello you are at about ")


def contact(request):
    return HttpResponse("hello you are at contact section ")    

def htmlPage(request):
    return render(request , "website/index.html")

def ok(request):
    return render(request , "website/ok.html")

def order(request):
    return render (request , "website/order.html")