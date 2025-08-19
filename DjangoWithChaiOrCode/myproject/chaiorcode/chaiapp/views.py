from django.shortcuts import render 
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
 
# Create your views here.
def home(request):
    return render(request, 'chaiapp/home.html')

def hello(request):
    return render (request, 'chaiapp/hello.html')

def index(request):
    chais = ChaiVarity.objects.all() 
    return render (request , 'chaiapp/index.html' , {'chais' : chais})

def layout(request):
    return render (request , 'chaiapp/layout.html')

def chai_detail(request ,chai_id):
    chai = get_object_or_404(ChaiVarity , pk =chai_id)
    return render (request , 'chaiapp/chai_detail.html' , {'chai' : chai})