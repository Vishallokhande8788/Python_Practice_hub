from django.shortcuts import render
from modelformapp.models import Product
# Create your views here.

def product(request):
    product_list = Product.objects.all()
    return render(request,'modelformapp/product.html',{'product_list':product_list})



