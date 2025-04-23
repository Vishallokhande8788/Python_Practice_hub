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

### Example in Python:
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the method
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks


# Let me know if you want this in another language or need a deeper explanation!