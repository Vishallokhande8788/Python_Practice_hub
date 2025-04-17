'''
intertance = aquiring  properties of a class into another class is called inheritance
 it i also known as subclassing as is-s- relationship
adv : code reusibility 
'''

class Animal: #parent class/ base class / super class
    def eat(self):
        print("eating briyani....")


class Cat(Animal): # child class / derived class / sub class
    def talk(self):
        print('meow meow ....')

class Dog(Animal):
    def speak(self):
        print('bhow bhow ....')


print('Animal object')
a=Animal()
a.eat()
print('Cat object')
c=Cat()
c.eat()
c.talk()

d = Dog()
d.eat()
d.speak()          