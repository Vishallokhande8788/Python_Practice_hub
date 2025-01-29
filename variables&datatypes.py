# 1. String (str) - A string is a sequence of characters (text). 
# It can be enclosed in either single quotes (' ') or double quotes (" ").

name = "John"  # A variable holding a string value
print("Name:", name)  # Output: John

# 2. Integer (int) - An integer is a whole number without a decimal point.
age = 30  # A variable holding an integer value
print("Age:", age)  # Output: 30

# 3. Float (float) - A float is a number with a decimal point.
height = 5.9  # A variable holding a float value
print("Height:", height)  # Output: 5.9

# 4. Boolean (bool) - A boolean can only have two values: True or False.
is_student = True  # A variable holding a boolean value
print("Is student:", is_student)  # Output: True

# 5. List (list) - A list is a collection of values, which can be of different types.
fruits = ["apple", "banana", "cherry"]  # A list holding string items
print("Fruits:", fruits)  # Output: ['apple', 'banana', 'cherry']

# 6. Tuple (tuple) - A tuple is similar to a list, but it is immutable (cannot be changed after creation).
coordinates = (10, 20)  # A tuple holding two integers
print("Coordinates:", coordinates)  # Output: (10, 20)

# 7. Dictionary (dict) - A dictionary holds key-value pairs. Each key is unique.
person = {"name": "Alice", "age": 25, "city": "New York"}  # A dictionary
print("Person:", person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 8. Set (set) - A set is an unordered collection of unique items.
colors = {"red", "blue", "green"}  # A set holding unique color names
print("Colors:", colors)  # Output: {'red', 'blue', 'green'}

# 9. None - None is a special value in Python used to represent the absence of a value.
nothing = None  # A variable holding None (no value)
print("Nothing:", nothing)  # Output: None

# You can also change the type of a variable:
# Let's change the 'age' variable to a string:
age = "thirty"  # Now 'age' is a string, not an integer
print("Age as a string:", age)  # Output: thirty

# Demonstrating type conversion:
# Convert 'age' back to an integer if it's a valid number:
if age.isdigit():  # Checks if the string 'age' is a valid number
    age = int(age)  # Convert the string to an integer
    print("Age as an integer:", age)  # If it's a valid number, it will be converted
else:
    print("Cannot convert 'age' to an integer.")  # If it's not a valid number

# Convert a float to an integer (removes the decimal part):
height_as_int = int(height)  # This converts the float to an integer (without rounding)
print("Height as integer:", height_as_int)  # Output: 5

# Checking the type of variables using the type() function:
print("Type of 'name':", type(name))  # <class 'str'>
print("Type of 'age':", type(age))  # <class 'str'> (because 'age' is now a string)
print("Type of 'height':", type(height))  # <class 'float'>
print("Type of 'is_student':", type(is_student))  # <class 'bool'>
print("Type of 'fruits':", type(fruits))  # <class 'list'>
print("Type of 'coordinates':", type(coordinates))  # <class 'tuple'>
print("Type of 'person':", type(person))  # <class 'dict'>
print("Type of 'colors':", type(colors))  # <class 'set'>
print("Type of 'nothing':", type(nothing))  # <class 'NoneType'>
