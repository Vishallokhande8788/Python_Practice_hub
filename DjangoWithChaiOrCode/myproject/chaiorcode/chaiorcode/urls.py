

from django.contrib import admin
from django.urls import path , include 
from django.conf import settings
from django.conf.urls.static import static
from chaiapp import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , views.home , name='home'),
    path("hello/" ,views.hello , name='hello'),
    path('layout/',views.layout , name='layout'),
    path("index/", include('chaiapp.urls')),
    path("chai_store/", views.chai_store_view, name='chai_store'),   # ✅ correct



    path("__reload__/", include("django_browser_reload.urls")),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
