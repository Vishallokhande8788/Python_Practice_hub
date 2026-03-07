"""
URL configuration for ChaiorDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/" , views.home , name='home'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path("htmlpage/",views.htmlPage,name='htmlpage'),
    path('ok/',views.ok,name='ok'),
    path('order/',views.order,name='order'),
    path('tailwind/',views.tailwind,name='tailwind'),

    path("__reload__/", include("django_browser_reload.urls")),


    path("chai/", include('Chai.urls')),
    path('chai' , include('Chai.urls') , name='coffee'),
    path('' , include('Chai.urls') , name='redirect')


] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
