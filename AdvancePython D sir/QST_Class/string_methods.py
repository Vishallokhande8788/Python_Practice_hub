# # 05/03/2025

# # x = input("Enter a string: ")
# # print(x.title())
# # print(x.upper())
# # print(x.capitalize())
# # print(x.lower())
# # print(str.isalnum(x))
# # print(str.isalpha(x))
# # print(str.isascii(x))
# # print(str.isdigit(x))
# # print(str.islower(x))
# # print(str.isnumeric(x))

# a = "hello sir good\tmorning"

# # endswith() - Check if the string ends with 'morning'
# print(a.endswith("morning"))

# # expandtabs() - Expands tabs in the string (useful if there are any '\t' characters)
# print(a.expandtabs(8))
# print(a)

# # find() - Find the position of the first occurrence of 'sir'
# print(a.find("sir"))

# # count() - Count how many times 'sir' appears in the string
# print(a.count("sir"))

# # index() - Find the position of 'sir', raises an error if not found
# print(a.index("sir"))

# # replace() - Replace 'sir' with 'Akshay'
# print(a.replace("sir", "Akshay"))


# Using splitlines() to split the string into a list of lines
# a = "hello sir \ngood morning\nhow are you\ndoing today"

# a = a.splitlines()
# print(a)
 
# a = "   hello sir good morning   "
# print(a)
# print(a.strip())   # "hello sir good morning" (spaces on both sides removed)
# print(a.lstrip())  # "hello sir good morning   " (spaces on the left removed)
# print(a.rstrip())  # "   hello sir good morning" (spaces on the right removed)

# string Formatting
# age = 22
# print("my name is {} i am {} years old ".format("Vishal", age))


num = 44
format_num =f"{num:10}"
print(format_num)
