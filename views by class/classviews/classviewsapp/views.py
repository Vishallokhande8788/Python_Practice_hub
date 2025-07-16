from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from classviewsapp import beer
from django.views.generic import TemplateView , CreateView
# Create your views here.

class HelloView(View):
    def get(self, request):
        return HttpResponse("welcome to class base  views")

class BeerListView(TemplateView):
    template_name = "beerList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["name"]= "pravin"
        context["marks"]= 98
        context["roll no "]= 123456

        return context

class BeerCreateView(CreateView):
    model = beer
    fields = "__all__"