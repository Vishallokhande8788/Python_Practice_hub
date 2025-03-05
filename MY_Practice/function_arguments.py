# 1. **Positional Arguments** - Arguments passed in the correct order.
def add(x, y):
    return x + y  # Adds two numbers

# Call the function with positional arguments
result = add(10, 5)
print(f"Sum (Positional Arguments) of 10 and 5 is: {result}")  # Output: 15

# 2. **Default Arguments** - Arguments that have default values.
def greet(name="Guest"):
    return f"Hello, {name}!"  # If no name is provided, defaults to "Guest"

# Call the function with no argument (defaults to "Guest")
greeting_default = greet()
print(greeting_default)  # Output: Hello, Guest!

# Call the function with a custom argument
greeting_custom = greet("Alice")
print(greeting_custom)  # Output: Hello, Alice!

# 3. **Keyword Arguments** - Arguments passed by explicitly specifying parameter names.
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

# Call the function with keyword arguments
description = describe_person(name="Bob", age=25, city="New York")
print(description)  # Output: Bob is 25 years old and lives in New York.

# 4. **Variable-Length Positional Arguments (`*args`)** - Function accepts an arbitrary number of positional arguments.
def sum_of_numbers(*args):
    return sum(args)  # Sums up all the values passed in *args

# Call the function with multiple arguments
total_sum = sum_of_numbers(10, 20, 30, 40)
print(f"Sum of numbers (using *args): {total_sum}")  # Output: 100

# Call the function with only one argument
total_sum_single = sum_of_numbers(5)
print(f"Sum of numbers (using *args) with one argument: {total_sum_single}")  # Output: 5

# 5. **Variable-Length Keyword Arguments (`**kwargs`)** - Function accepts an arbitrary number of keyword arguments.
def describe_person_v2(**kwargs):
    description = ""
    for key, value in kwargs.items():
        description += f"{key}: {value}\n"
    return description

# Call the function with multiple keyword arguments
person_description = describe_person_v2(name="Alice", age=30, city="Los Angeles", occupation="Engineer")
print(f"Description (using **kwargs):\n{person_description}")
# Output:
# name: Alice
# age: 30
# city: Los Angeles
# occupation: Engineer

# 6. **Mixing Positional, Default, and Keyword Arguments** - Using a combination of argument types.
def full_profile(name, age, city="Unknown", occupation="Not Provided"):
    return f"{name} is {age} years old, lives in {city}, and works as a(n) {occupation}."

# Call the function with all arguments
profile_full = full_profile("Charlie", 28, city="San Francisco", occupation="Developer")
print(f"Full Profile (mixing positional, default, and keyword arguments):\n{profile_full}")
# Output: Charlie is 28 years old, lives in San Francisco, and works as a(n) Developer.

# Call the function with default values for city and occupation
profile_default = full_profile("Eve", 35)
print(f"Full Profile with Default Values:\n{profile_default}")
# Output: Eve is 35 years old, lives in Unknown, and works as a(n) Not Provided.
