# abstract clas: partialy implemented class
#  any python which is child of ABC class is called a abstract classs in python 
# ABC class is present inside abc module 

# ex:1
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