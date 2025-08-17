from django.shortcuts import render 
# Create your views here.
def home(request):
    return render(request, 'chaiapp/home.html')

def hello(request):
    return render (request, 'chaiapp/hello.html')

def index(request):
    return render (request , 'chaiapp/index.html')

def layout(request):
    return render (request , 'chaiapp/layout.html')