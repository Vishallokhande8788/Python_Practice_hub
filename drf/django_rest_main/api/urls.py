from django.urls import path
from . import views

urlpatterns = [
    # URL for getting all students or adding a new one (GET, POST)
    path('students/', views.studentsView),

    # URL for getting a single student by ID (GET)
    path('students/<int:pk>/', views.studentDetailView),

    # URL pattern for the Employees API view
    # When the client requests 'employees/', it will be handled by the Employees class-based view
    path('employees/', views.Employees.as_view()),

    # by Getting url using primary key (pk)
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

]






  