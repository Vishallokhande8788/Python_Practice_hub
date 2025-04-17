''' 

multiple inheritnce : more than one parent class into single child class at the same time 

'''

# e.g=1

class Parent1:
    def m1(self):
        print("m1 () of parent 1")

class Parent2:
    def m2(self):
        print("m2 () o parent 1 ")


class Child (Parent1 , Parent2): pass

c = Child()
c.m1()
c.m2()


# eg = 2  = is type ka eg only python me he chalta hai bas 

class parent1:
    def m1(self):
        print("m1 () of parent 1 ")

class Parent2:
    def m1(self):
        print("m2 () of parnt 2 ")

class Child (Parent2 , Parent1 ): pass # jo pahala prameter aayega wo he run hoga bas dusra nahi 

c = Child()
c.m1()