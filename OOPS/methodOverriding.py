# class Parent:
#     def property(self):
#         print("Parent property")

#     def investment(self):
#         print("Parent investment")


# class Child(Parent):

#     def investment(self):
#         print("Child investment")


# c = Child()
# c.property()
# c.investment()  


#           or 
# **Method overriding** in short:

# It's when a **subclass provides a specific implementation** of a method that is already defined in its **superclass**.

# **Key points:**
# - Method name, parameters, and return type must be the same.
# - Happens in **inheritance**.
# - Allows **runtime polymorphism** (dynamic method dispatch).

### Example

'''
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the method
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks


# Let me know if you want this in another language or need a deeper explanation!
'''

class shape:
    def area(self):
        print('area is xyz ....')

class square:
    def area(shape):
        print('side square ')
        print('ok')

class rectangle :
    def area(shape):
        print("l * b ")

class cirle:
    def area (shape):
        print("paya r square ")

class cone :
    def area(self):
        print("i am a cone ")

s= shape()
s.area()

s = square()
s.area()

r = rectangle()
r.area()

c = cirle()
c.area()

c = cone()
c.area()