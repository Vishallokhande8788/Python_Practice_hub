from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
# ---------------------------
# API View for all students
# ---------------------------
@api_view(['GET', 'POST'])
def studentsView(request):
    # Handle GET request → Fetch all students
    if request.method == 'GET':
        # Retrieve all student records from the database
        students = Student.objects.all()
        # Serialize multiple student objects (many=True)
        serializer = StudentSerializer(students, many=True)
        # Return all student data with HTTP 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Handle POST request → Add new student
    elif request.method == 'POST':
        # Deserialize incoming request data into Student model
        serializer = StudentSerializer(data=request.data)
        # Check if data is valid according to serializer rules
        if serializer.is_valid():
            # Save new student record in database
            serializer.save()
            # Return created student data with HTTP 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If validation fails, print errors for debugging
        print(serializer.errors)
        # Return validation errors with HTTP 400 Bad Request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------
# API View for single student
# ---------------------------
@api_view(['GET' , 'PUT' , 'DELETE'])
def studentDetailView(request, pk):
    try:
        # Try to fetch a single student by primary key (ID)
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        # If no student found, return HTTP 404 Not Found
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Handle GET request → Return single student details
    if request.method == 'GET':
        # Serialize the student object
        serializer = StudentSerializer(student)
        # Return serialized student data with HTTP 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  Class-based view for Employees

class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeesDetail(APIView):
    def get_object (self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404 

    def get(self,request, pk):
        employee = self.get_object(pk) 
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)                                                                 