# 24/04/2025

# Duck typing in Python is a concept where the type or class of an object is less important than the methods or behavior it supports.
# Short definition:
# “If it looks like a duck and quacks like a duck, it’s a duck.”


# e.g = 1
'''
class Cat:
    def talk (self):
        print("Meow.. Meow..")

class Dog:
    def talk (self):
        print("Boww... Boww...")

class Goat:
    def talk (self):
        print("myahh... myahh...")


def talkingTest(animalList):
    for animal in animalList:
        animal.talk()


animals = [Cat(), Dog(), Goat()]
talkingTest(animals)

'''

# e.g = 2
'''
class Hero:
    def speed(self):
        print('80 kmph')

class Honda:
    def speed(self):
        print('50 kmph')
    
class Bajaj:
    def speed(self):
        print('70 kmph')

class Fortuner:
    def speed(self):
        print('210 kmph')

def speedTest(vehicleList):
    for vehicle in vehicleList:
        vehicle.speed()

vehicles = [Hero(), Honda(), Bajaj(), Fortuner()]
speedTest(vehicles) 
'''
    

