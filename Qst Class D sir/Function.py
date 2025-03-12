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



# # python function can return multiple values
# #QUE =  WRITE A PRORAM FOR PRIT ADD SUB MUL DIV IN ONE FUNCTION

# def f1(a , b):
#     add = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return add , sub , mul , div
    
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# add , sub , mul , div = f1(a , b)
# print("Add : " , add)
# print("Sub : " , sub)
# print("Mul : " , mul)
# print("Div : " , div)


def ZigZag(num):
    if num % 3 == 0 and  num % 5 == 0 :
        print("ZigZag")
    elif num % 3 == 0:
        print('ZIG')
    elif num % 5 == 0:
        print("ZAG")
    else :
        print(f"{num} is not divisible 3 and 5")
    return 

ZigZag(6)
ZigZag(10)
ZigZag(30)
ZigZag(7 )

