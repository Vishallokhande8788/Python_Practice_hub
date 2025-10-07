from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def studentsView(request):
    students_list = {
        'id':1,
        'name':'John',
        'age':20,
        'gender':'Male'

    }

    return JsonResponse(students_list)

