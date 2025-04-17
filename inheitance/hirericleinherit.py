''' 
hirericle nheritance : one parent property is extended by more thn ne hild class at the same time 
'''

class Animal:
    def eat(self):
        print(" Eating...")

class Cat(Animal):
    def talk(self):
        print('meau meau ....')

class Dog(Animal):
    def bark(self):
        print("Bhow bhow....")

A = Dog()
A.eat()
A.bark()
A.talk()
