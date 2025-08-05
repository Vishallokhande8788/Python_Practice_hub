from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'cookieproapp/home.html')

def name_view(request):
    return render(request,'cookieproapp/name.html')

def age_view(request):
    name = request.GET['uname']
    response = render(request,'cookieproapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def qualification_view(request):
    age = request.GET['uage']
    response = render(request,'cookieproapp/qual.html',{'age':age})
    response.set_cookie('age',age)
    return response

def result(request):
    qual = request.GET['uqual']
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    return render(request,'cookieproapp/result.html',{'name':name,'age':age,'qual':qual})