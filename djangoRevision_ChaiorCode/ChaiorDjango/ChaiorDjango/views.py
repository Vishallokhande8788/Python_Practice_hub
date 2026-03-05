from django.http import HttpResponse

def home(request):
    return HttpResponse("hello you are at home ")


def about(request):
    return HttpResponse("hello you are at about ")


def contact(request):
    return HttpResponse("hello you are at contact section ")    