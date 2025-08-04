from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'cookieprojectapp/home.html')

def pageCount(request):
    if 'count' in request.COOKIES:
        if 'count' in request.COOKIES:
            newcount = int(request.COOKIES['count'])+1
        else :
            newcount = 1

        request.COOKIES['count'] = newcount
        response = render(request,'cookieprojectapp/count.html',{'count':newcount})
        response.set_cookie('count',newcount)
        return response
    