#  method default argument

# class Test:
#     def m1(self, a=0, b=0 , c = 0):
#         print('m1() executed')

# t  = Test()
# t.m1()
# t.m1(1)
# t.m1(1,2)
# t.m1(1,2,3)


# eg = calculator : add (1,2,3) jitne bhi user argument dega sab add hone chaheye 

# class Calculator:
#     def add(self, *args):  # yahan *args matlab user jitne chahe numbers de sakta hai
#         total = 0
#         for num in args:
#             total += num
#         print("Sum:", total)

# c = Calculator()
# c.add(1, 2, 3)           
# c.add(10, 20)            
# c.add(100)                
# c.add(1, 2, 3, 4, 5, 6)
# c.add(1,2,3,4,5,6,7,8,9)


#                 or

class Test():
    def m1(self , *a):
        print('addition of numbers : ',sum(a))

t = Test()
t.m1(1,2,3,4,5,6,7,8,9)
t.m1(1,2,3,4,5,6,7,8,9,10)  
