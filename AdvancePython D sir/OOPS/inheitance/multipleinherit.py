''' 

multiple inheritnce : more than one parent class into single child class at the same time 

'''
''' 

multiple inheritnce : more than one parent class into single child class at the same time 

'''

# # e.g=1

# class Parent1:
#     def m1(self):
#         print("m1 () of parent 1")

# class Parent2:
#     def m2(self):
#         print("m2 () o parent 1 ")


# class Child (Parent1 , Parent2): pass

# c = Child()
# c.m1()
# c.m2()


# # eg = 2  = is type ka eg only python me he chalta hai bas 

# class parent1:
#     def m1(self):
#         print("m1 () of parent 1 ")

# class Parent2:
#     def m1(self):
#         print("m2 () of parnt 2 ")

# class Child (Parent2 , Parent1 ): pass # jo pahala prameter aayega wo he run hoga bas dusra nahi 

# c = Child()
# c.m1()





#  One child class inherits from two or more parent classes
# Parent Class 1
class Father:
    def skill1(self):
        print("Father: Knows farming")

# Parent Class 2
class Mother:
    def skill2(self):
        print("Mother: Knows cooking")

# Child Class
class Child(Father, Mother):
    def skill3(self):
        print("Child: Knows coding")

# Create object
c = Child()
c.skill1()  # From Father
c.skill2()  # From Mother
c.skill3()  # From Child

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