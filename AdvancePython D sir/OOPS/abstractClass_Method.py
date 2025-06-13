# abstract clas: partialy implemented class
#  any python which is child of ABC class is called a abstract classs in python 
# ABC class is present inside abc module 

# ex:1

'''
from abc import *

class Test(ABC):
    def m1(self):
        print("m1 is abstract")

t = Test()
t.m1()

# ex:2
class Test :
    def m1(self):
        print("m1 is abstract")
    @abstractmethod
    def m2(self):
        pass

t = Test()
t.m1()
t.m2()

# ex:3
class Test (ABC):
    def m1(self):
        print("m1 is abstract")
    @abstractmethod
    def m2(self):
        pass

t = Test()
t.m1()
t.m2()
'''

'''
from abc import *
class Greet (ABC):
    def wish (self):
        print("Quality software wishing you....")


    @abstractmethod
    def greet (self):
        pass

class Diwali (Greet):
    def greet (self):
        print("Happy Diwali")

class Holi (Greet):
    def greet (self):
        print("Happy Holi")

d = Diwali()
d.wish()
d.greet()

print("...........")

h = Holi()
h.wish()
h.greet()
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    def calc(self):
        print("Calculating area of shape...")

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of square: {self.side * self.side}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of rectangle: {self.length * self.width}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of circle: {3.1416 * self.radius * self.radius}")

# Object creation and method calls
s = Square(4)
s.area()

r = Rectangle(5, 3)
r.area()

c = Circle(2)
c.area()
