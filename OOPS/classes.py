# # how to ceate a class in python

# '''

# syntex:

# class ClassName:
#      doc string
#      constructor
#      instance method
#      class method
#      static method


# syntex :
#     ref_variable  ClassNmae()

#     student : 
#     name , marks ,  roll na , g name 
# '''

# class Student:
#     def __init__(self):
#         self.name = 'Vishal Lokhande'
#         self.marks = 100
#         self.roll_no = 123456
#         self.gender = 'male'


# s = Student()
# print(s.name)
# print(s.marks)
# print(s.roll_no)
# print(s.gender)

# # 14/04/2025


# class Student:
#     def __init__(self , name , marks , rollno):
#         self.name = name
#         self.marks = marks
#         self.rollno = rollno 

#     def disp_students(self):
#         print('student name : ' , self.name)
#         print('student Marks : ', self.marks)
#         print('student rollno : ' ,  self.rollno)


# s = Student ('AAA' , 90.30 , 111)
# s.disp_students()

# s2 = Student ('BBB' , 80.80 , 222)
# s2.disp_students()

# s3 = Student('ccc' , 70.70 , 333)
# s3.disp_students()

    

# instance variable
#  global variable
#  local variable
# what is instance variable
# when instance variable created or destroyed
# what is memory management / what is garbage collection
# where we can create a instance variable (in constructor , instance method by using self)




# where we can create a instance variable 
class Test:
    def __init__(self):
        self.a=10

        def m1(self):
            self.b = 20


t = Test()
print(t.__dict__)

t.m1()
print(t.__dict__)
t.c =30 
print(t.__dict__)
print('.....t2.....')

t2 = Test()
print(t2.__dict__)
print(t2.a)


        