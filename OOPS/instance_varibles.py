
# what is instance variable
# when instance variable created or destroyed
# what is memory management / what is garbage collection
# where we can create a instance variable (in constructor , instance method by using self)



# # where we can create a instance variable 
# class Test:
#     def __init__(self):
#         self.a=10

#         def m1(self):
#             self.b = 20


# t = Test()
# print(t.__dict__)

# t.m1()
# print(t.__dict__)
# t.c =30 
# print(t.__dict__)
# print('.....t2.....')

# t2 = Test()
# print(t2.__dict__)
# print(t2.a)


# # How to accss instance variable
# # inside class by using self and outside class by using object-reference name

# class Test:
#     def __init__(self):
#         self.a=100

#     def m1(self):
#         print(self.a) # instance variable access inside class


# t=Test()
# t.m1()
# print(t.a) # instance variable access outside class

# how to delete instance variable

class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        del self.a


t=Test()
print(t.__dict__ )
t.m1()
print(t.__dict__ )

t2 = Test()
print(t2.__dict__ )
del t2.b
print(t2.__dict__ )