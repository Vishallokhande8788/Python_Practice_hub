
# types of variables in python

# global variable
# local variable

# # 1.  global variables
# #they are available outside the function

# name = "Rahul"
# def f1():
#      print(name)
    
# def f2():
#      print(name)
    
# f1()
# f2()
# # #use of global keyword

# # A) to modify value of global variable inside function 

# name = "Vishal"
# def f1():
#      global name
#      name="Akahay"
#      print(name)

# def f2(): 
#      print(name)

# f1()
# f2()
# # B)  to modify value of global variable outside function

# def f1():
#      global a
#      a = 10
#      print(a)

# def f2(): 
#      print(a)

# f1()
# f2()

# # globl to local variable acces using global function 

# a = 100
# def f1():
#     a = 200
#     print(globals()['a'])
#     print(a)
# f1()

# # e.g.
# a = 10
# b = 20
# def f1():
#     a = 100
#     b = 200
#     print(a+b)
#     print(globals()['a']+globals()['b'])
# f1()






# # 2 . local variables
# #they are  available only inside the function

# def f1():
#      name = "Akahay"
#      print(name)
     
# def f2(): 
#      print(name)

# f1()
# f2()    



