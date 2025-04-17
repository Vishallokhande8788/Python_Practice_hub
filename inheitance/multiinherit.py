'''
aquring property more than one clas onto single child class one after  another is called is called mulilevel inheritance 

'''

class Vehicles:
    def start(self):
        print("car started...")

class Car(Vehicles):
    def speed(self):
        print(" running with 8788 kmph")

class SportsCar(Car):
    def music(self):
        print("plying music...")


sp = SportsCar()
sp.start()
sp.music()
sp.speed()

mr = Car()
mr.start()
mr.speed()
