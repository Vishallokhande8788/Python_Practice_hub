from django.urls import path
from . import views

urlpatterns = [
    # URL for getting all students or adding a new one (GET, POST)
    path('students/', views.studentsView),

    # URL for getting a single student by ID (GET)
    path('students/<int:pk>/', views.studentDetailView),
]
