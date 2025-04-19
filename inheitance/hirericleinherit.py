''' 
hirericle nheritance : one parent property is extended by more thn ne hild class at the same time 
'''

# class Animal:
#     def eat(self):
#         print(" Eating...")

# class Cat(Animal):
#     def talk(self):
#         print('meau meau ....')

# class Dog(Animal):
#     def bark(self):
#         print("Bhow bhow....")

# A = Dog()
# A.eat()
# A.bark()
# A.talk()


# Multiple child classes inherit from one parent class.

# Parent Class
class Vehicle:
    def start(self):
        print("Vehicle starts")

# Child Class 1
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Child Class 2
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

# Create objects
car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()
