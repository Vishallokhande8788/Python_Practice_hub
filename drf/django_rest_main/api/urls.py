from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet , basename='employee')


urlpatterns = [
    # URL for getting all students or adding a new one (GET, POST)
    path('students/', views.studentsView),

    # URL for getting a single student by ID (GET)
    path('students/<int:pk>/', views.studentDetailView),

    # # URL pattern for the Employees API view
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('', include(router.urls)),

]






  