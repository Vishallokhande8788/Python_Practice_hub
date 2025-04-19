'''
aquring property more than one clas onto single child class one after  another is called is called mulilevel inheritance 

'''

# class Vehicles:
#     def start(self):
#         print("car started...")

# class Car(Vehicles):
#     def speed(self):
#         print(" running with 8788 kmph")

# class SportsCar(Car):
#     def music(self):
#         print("plying music...")


# sp = SportsCar()
# sp.start()
# sp.music()
# sp.speed()

# mr = Car()
# mr.start()
# mr.speed()


#  A class inherits from a child class which already inherits from a parent class.

# Parent Class
class Grandfather:
    def old_story(self):
        print("Grandfather: Tells old stories")

# Intermediate Class
class Father(Grandfather):
    def advice(self):
        print("Father: Gives advice")

# Child Class
class Son(Father):
    def play(self):
        print("Son: Plays cricket")

# Create object
s = Son()
s.old_story()  # From Grandfather
s.advice()     # From Father
s.play()       # From Son
