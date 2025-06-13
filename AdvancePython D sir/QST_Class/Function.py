# print("Hello World")
# # print("Hello World")  # this is a comment
# def greet():
#     print("Hello World")

# greet()

# # add function
# def addition(a, b):
#         print(a + b)
# addition(1, 2)

# # count even number
# def even_number():
#     user_input = int(input("how many even numbers do you want to find: "))
#     for i in range(1, user_input + 1):
#         if i % 2 == 0:
#             print(i)
# even_number()

# # age calculator
# def calc_age(birth_year):
#     current_year = 2025
#     age = current_year - birth_year
#     print(`tour age is {age} years`)

# calc_age(2003)

# # def f1(x):
# #     b=x**2
# #     print(b)

# #     def start():
# #         x=5
# #         f1(x)
# # start()

# # given errob because of b is a local scope variable

# # correct code
# def f1(y):
#     b=y**2
#     return b

# def start():
#         x=5
#         return_var=f1(x)
#         print(return_var)
# start()

# 04/03/2025

#  lambda function:

# x=f1
# print(id(x))
# print(id(f1))

# print(x(8))


# a = lambda a ,b : a+b
# s = lambda a,b : a-b

# print(a(5,6))
# print(s(18,6))

# a = lambda a  : a**2
# print(a(5))

# b = lambda a: a[::-1]
# print(b('hello'))

# c = lambda a,b:len(a)+len(b)
# print(c('hello ','vishal sir'))

# def multiplier (num):
#     return lambda x : x*num

# multiply_by_2 = multiplier(2)
# multiply_by_4 = multiplier(4)
# multiply_by_6 = multiplier(6)

# print(multiply_by_2(5))
# print(multiply_by_4(5))
# print(multiply_by_6(5))

