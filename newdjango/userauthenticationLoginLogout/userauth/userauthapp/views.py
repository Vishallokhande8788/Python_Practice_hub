from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'userauthapp/home.html')


@login_required
def pyExam(request):
    return render(request, 'userauthapp/python.html')

@login_required
def javaExam(request):
    return render(request, 'userauthapp/java.html')

def jsExam(request):
    return render(request, 'userauthapp/js.html')   

def logout(request):
    return render(request, 'userauthapp/logout.html')

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect("accounts/login")
    return render(request, 'userauthapp/signup.html' , {'form':form})