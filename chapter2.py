# que 1
# a = int(input("number 1 : "))
# b = int(input("number 2 : "))
# print("num 1 + num 2 = " ,a+b)

# que 2
# a = int(input("enter a number : "))
# print(a/2)

# # que 3
# a = (input("enter : "))
# print(type(a))

# # que 4
# a = 30
# b= 40
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is lesser than b")

# # que 5
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# c = (a+b)/2
# print(c)

# # que 6
# a = int(input("enter a number : "))
# print(a**2)


# This code takes an input hour from the user, compares it with the current system time, and prints a greeting ("Good morning," "Good afternoon," "Good evening," or "Good night") based on the given hour.


# hour = int(input("enter a time : "))
# import time
# timestamp = time.strftime('%H:%M:%S')
# a = int(timestamp.split(':')[0])


# if hour >= 5 and  hour  <=10 :
#     print(("Good morning"))
# elif hour >11 and hour <=16 :
#     print("good afternoon")
# elif hour > 17 and hour <= 20:
#     print("good evening")
# elif hour > 21 and hour <= 24:
#     print ("good Night ")
# elif hour > 0 and hour <5 :
#     print("good Night")
# else:
#     print("enter a valid time ")

# Define a sample string
my_string = "Hello, Python World!"

# 1. Slicing the string
# Slicing allows us to extract a part of the string
# Syntax: my_string[start:end:step]

# Extract "Hello"
sliced_part_1 = my_string[:5]  # From the start to index 5 (not including 5)
print(f"Sliced part 1: {sliced_part_1}")  # Output: Hello

# Extract "Python"
sliced_part_2 = my_string[7:13]  # From index 7 to 13 (not including 13)
print(f"Sliced part 2: {sliced_part_2}")  # Output: Python

# Extract "World" using a step
sliced_part_3 = my_string[14:19:2]  # From index 14 to 19 with a step of 2
print(f"Sliced part 3: {sliced_part_3}")  # Output: Wrld

# Extract from the end of the string
sliced_part_4 = my_string[-6:]  # Last 6 characters
print(f"Sliced part 4: {sliced_part_4}")  # Output: World!

# 2. String Operations

# 2.1 String Length
length = len(my_string)
print(f"Length of string: {length}")  # Output: 20

# 2.2 String Concatenation
greeting = "Hello"
name = "Alice"
greeting_name = greeting + " " + name  # Concatenating two strings
print(f"Greeting message: {greeting_name}")  # Output: Hello Alice

# 2.3 String Repetition
repeated = "Hi! " * 3  # Repeat the string 3 times
print(f"Repeated string: {repeated}")  # Output: Hi! Hi! Hi! 

# 2.4 String Methods

# Convert to uppercase
upper_case = my_string.upper()
print(f"Uppercase string: {upper_case}")  # Output: HELLO, PYTHON WORLD!

# Convert to lowercase
lower_case = my_string.lower()
print(f"Lowercase string: {lower_case}")  # Output: hello, python world!

# Replace part of the string
replaced_string = my_string.replace("Python", "Java")
print(f"Replaced string: {replaced_string}")  # Output: Hello, Java World!

# Check if the string starts with a specific word
starts_with_hello = my_string.startswith("Hello")
print(f"Starts with 'Hello'? {starts_with_hello}")  # Output: True

# Check if the string ends with a specific word
ends_with_world = my_string.endswith("World!")
print(f"Ends with 'World!'? {ends_with_world}")  # Output: True

# Find the index of a substring
index_of_python = my_string.find("Python")
print(f"Index of 'Python': {index_of_python}")  # Output: 7

# Split the string into a list of words
words = my_string.split()
print(f"Words in string: {words}")  # Output: ['Hello,', 'Python', 'World!']

# 2.5 String Formatting
# Using f-strings for formatting
age = 25
formatted_string = f"My age is {age}."
print(formatted_string)  # Output: My age is 25.

# 3. String Equality Check
is_equal = (my_string == "Hello, Python World!")
print(f"Strings are equal? {is_equal}")  # Output: True

# 4. String Join (joining a list into a string)
words_list = ['I', 'am', 'learning', 'Python']
joined_string = " ".join(words_list)  # Join words with space
print(f"Joined string: {joined_string}")  # Output: I am learning Python
