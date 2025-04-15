# static variables
# what is static variable
# when static variable created or destroyed
# what is memory management / what is garbage collection
# where we can create a static variable 

'''
directly inside class
inside constructor , instance method , static mathed using class name 
inside class method either using class name or cls 
outisde class by using class name

'''

'''
class Test:
    a = 10
    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c = 30

    
    @classmethod
    def m2(cls):
        Test.d = 40
        cls.e=50

    @staticmethod
    def m3():
        Test.f = 60

t=Test()
t.m1()
t.m2()
t.m3()
Test.g = 70
print(Test.__dict__)

'''






