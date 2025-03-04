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


a = lambda a ,b : a+b
s = lambda a,b : a-b

print(a(5,6))
print(s(18,6))

