# how to ceate a class in python

'''

syntex:

class ClassName:
     doc string
     constructor
     instance method
     class method
     static method


syntex :
    ref_variable  ClassNmae()

    student : 
    name , marks ,  roll na , g name 
'''

class Student:
    def __init__(self):
        self.name = 'Vishal Lokhande'
        self.marks = 100
        self.roll_no = 123456
        self.gender = 'male'


s = Student()
print(s.name)
print(s.marks)
print(s.roll_no)
print(s.gender)