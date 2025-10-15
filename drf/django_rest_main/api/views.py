from django.shortcuts import render , get_object_or_404
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
from rest_framework import mixins , generics
from rest_framework.generics import CreateAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView , ListAPIView 
from rest_framework import viewsets
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

# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK) 

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmployeesDetail(APIView):
#     def get_object (self, pk):
#         try:
#             return Employee.objects.get(id=pk)
#         except Employee.DoesNotExist:
#             raise Http404 

#     def get(self,request, pk):
#         employee = self.get_object(pk) 
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

# #  mixin-based view for Employees

# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get (self , request):
#         return self.list(request)

#     def post (self , request):
#         return self.create(request) 

# class EmployeeDetail(mixins.RetrieveModelMixin ,mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get (self , request , pk):
#         return self.retrieve(request, pk)

#     def put (self , request , pk):
#         return self.update(request, pk)

#     def delete (self , request , pk):
#         return self.destroy(request, pk)
        

# #  generic-based view for Employees

# class Employees(generics.ListAPIView , CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'


# ViewSet for Employee model

class EmployeeViewSet(viewsets.ViewSet):
    def list (self , request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create (self , request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve (self , request , pk=None):
        employee = get_object_or_404(Employee , pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data , status=status.HTTP_200_OK)
 