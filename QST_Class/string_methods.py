# 05/03/2025

# x = input("Enter a string: ")
# print(x.title())
# print(x.upper())
# print(x.capitalize())
# print(x.lower())
# print(str.isalnum(x))
# print(str.isalpha(x))
# print(str.isascii(x))
# print(str.isdigit(x))
# print(str.islower(x))
# print(str.isnumeric(x))

a = "hello sir good\tmorning"

# endswith() - Check if the string ends with 'morning'
print(a.endswith("morning"))

# expandtabs() - Expands tabs in the string (useful if there are any '\t' characters)
print(a.expandtabs(8))
print(a)

# find() - Find the position of the first occurrence of 'sir'
print(a.find("sir"))

# count() - Count how many times 'sir' appears in the string
print(a.count("sir"))

# index() - Find the position of 'sir', raises an error if not found
print(a.index("sir"))

# replace() - Replace 'sir' with 'Akshay'
print(a.replace("sir", "Akshay"))

