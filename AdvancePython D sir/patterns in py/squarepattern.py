# 31/03/2025

# n = int(input("Enter the number of rows: "))
# print("* " * n) 

# a = int(input("Enter the number of rows: "))
# for i in range(a):
#     print("* " * a)


# b = int(input("enter a no to print pattern : "))
# for i in range(b):
#     print((str(i + 1 )+" ")* b)

# c = int(input("enter a no : "))
# for i in range(c):
#     print((chr(i+65)+" ") * c)


# d = int(input("enter a no : "))
# for i in range(d-1,-1,-1 ):  #starts from n-1 and go down to 0
#     print((chr(i+69)+ " ") * d )

# d = int(input("enter a no : "))
# for i in range(d-1,-1,-1 ):  #starts from n-1 and go down to 0
#     print((str(i+ 1) +  " ") * d )

# e = int(input("enter a no : "))
# for i in range(e):
#     for j in range(e):
#         print(j+1 , end=' ' * e)
#     print()


# f = int(input("Enter a number: "))

# # Outer loop to handle rows
# for i in range(f):
#     # Inner loop to print numbers from f to 1
#     for j in range(f-1, -1, -1):
#         print(str(j+1), end=' ')  # Print numbers separated by a single space
#     print()  # Newline after each row


# g = int(input("Enter a number: "))
# for i in range(g):
#     print('* ' * (i+1))


# h = int(input("Enter a number: "))
# for i in range(h-1,-1,-1):
#     print("* " * (i-1))


# j =int(input('enter a no :' ))
# for i in range(j-1,-1,-1) :
#     print((chr(i+65) + " ") * (i+1) )


# k = int(input("enter a no : "))
# for i in range(k):
#     print(((chr(k-i+65)) + ' ' ) * (i+1))

#  reversed 

# k = int(input("enter a no : "))
# for i in range(k):
#     print((chr(k-i+64) + " ") * (i+1))

# l = int(input("enter a no : "))
# for i in range(l):
#     for j in range(i):
#         print((j ) , end=' ')
#     print()

# l = int(input("enter a no : "))
# for i in range(l):
#     for j in range(i):
#         print(chr(j + 65 ) , end=' ')
#     print()5z


# m = int(input("enter a no : "))
# for i in range(m):
#     for j in range(i):
#         print(chr(m-j+64) , end=" ")
#     print()

# reverce 


# m = int(input("enter a no : "))
# for i in range(m-1,-1,-1):
#     for j in range(i):
#         print(chr(m-j+64) , end=" ")
#     print()

n = int(input("enter a no : "))
for i in range(n):
    print((str(n + 1) + " " ) * (i+1) )