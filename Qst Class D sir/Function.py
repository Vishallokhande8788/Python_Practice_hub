# #  Used returen value of function 
# #  used o return dependa on condition 
# #  returns word retun value to fuction 


# def sip (amnt):
#     returnAmnt=amnt + 1000
#     return returnAmnt

# rv = sip(5000)
# print(rv)

# print(sip(9000))

# print("***** Welcome to QST SIP plan *****")
# name = input("Enter your name: ")
# amnt = int(input("Enter your amount: "))
# total_Amnt = sip(amnt)
# if total_Amnt >= 10000:
#     print("Your total return value is 9.85 % ")
# elif total_Amnt >= 5000 and total_Amnt < 10000:
#     print("Your total return value is 7.2 % ")
# else:
#     print("Your total return value is 6.2 % ")



# # # python function can return multiple values
# # #QUE =  WRITE A PRORAM FOR PRIT ADD SUB MUL DIV IN ONE FUNCTION

# # def f1(a , b):
# #     add = a + b
# #     sub = a - b
# #     mul = a * b
# #     div = a / b
# #     return add , sub , mul , div
    
# # a = int(input("Enter a: "))
# # b = int(input("Enter b: "))

# # add , sub , mul , div = f1(a , b)
# # print("Add : " , add)
# # print("Sub : " , sub)
# # print("Mul : " , mul)
# # print("Div : " , div)


# def ZigZag(num):
#     if num % 3 == 0 and  num % 5 == 0 :
#         print("ZigZag")
#     elif num % 3 == 0:
#         print('ZIG')
#     elif num % 5 == 0:
#         print("ZAG")
#     else :
#         print(f"{num} is not divisible 3 and 5")
#     return 

# ZigZag(6)
# ZigZag(10)
# ZigZag(30)
# ZigZag(7 )

## 18/03/2025

## map(): if we want to perform some common operations on each and every element present inside in a sequence

# # map(fun , sequence):
# # where fun is used to writting mapping logic and sequence may list , tuple , set ,....?

# def Double (num):
        # return num*2

# l= [1,2,3,4,5,6,7,8,9,10]
# output = list(map(Double , l))
# print(output)

# l = [1,2,3,4,5,6,7,8,9,10]
# output = tuple(map(lambda x : x*2 , l))
# print(output)

# output = set(map(lambda x : x*2 , l))
# print(output)
# # eg :
# friendNames = ["Vishal", "shubham", "bhagesh", "Akshay", "sushil", "Yes"]

# DeveloperNames = list(map(lambda name: name + " developer", friendNames))

# print(DeveloperNames)

# friendNames = ["Vishal", "shubham", "bhagesh", "Akshay", "sushil", "Yes"]

# filterDevloperNames = list(filter(lambda name: len(name) % 2 == 0, friendNames))
# print(filterDevloperNames)

# #  eg : take string from user and print owels presemt in using ilter function

# userInput = input("Enter a string: ")

# filterString = list(filter(lambda x: x in 'aeiouAEIOU', userInput))

# print(filterString)

# # eg filter on bases on category
# productList = [
#     {
#     "ProductId":1,
#     "ProductName":"iPhone",
#     "Price":10000,
#     "Category":"Mobile",
#     },
#     {"productId":2,
#      "ProductName":"Samsung",
#      "Price":20000,
#      "Category":"Mobile",
#      },
#      {"productId":3,
#       "ProductName":"Dell",
#       "Price":30000,
#       "Category":"Laptop",
#       },
#       {"productId":4,
#        "ProductName":"HP",
#        "Price":40000,
#        "Category":"Laptop",
#        }

#     ]

# filterProducts = list(filter(lambda Products: Products["Category"] == "Mobile", productList))
# print(filterProducts)

# # 19/03/2025

# # Function Recursin

# def f1(num):
#     print(num)
#     if num > 0:
#         f1(num-1)
# f1(4)
