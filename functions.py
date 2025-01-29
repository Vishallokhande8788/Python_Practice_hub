# 1. **Basic Function** - A simple function that adds two numbers.
def add_numbers(x, y):
    return x + y  # The function returns the sum of x and y.

# Call the function with arguments 10 and 5
result = add_numbers(10, 5)
print(f"Sum of 10 and 5 is: {result}")  # Output: Sum of 10 and 5 is: 15

# 2. **Function with Default Arguments** - A function with a default value for a parameter.
def greet(name="Guest"):
    return f"Hello, {name}!"  # If no name is provided, it defaults to "Guest".

# Call the function without providing the name (uses default "Guest")
greeting = greet()
print(greeting)  # Output: Hello, Guest!

# Call the function with a name provided
greeting_with_name = greet("Alice")
print(greeting_with_name)  # Output: Hello, Alice!

# 3. **Function with Multiple Return Values** - A function can return multiple values as a tuple.
def get_student_info():
    name = "Bob"
    age = 20
    grade = "A"
    return name, age, grade  # Returning multiple values

# Call the function and unpack the returned values into variables
student_name, student_age, student_grade = get_student_info()
print(f"Student Name: {student_name}, Age: {student_age}, Grade: {student_grade}")
# Output: Student Name: Bob, Age: 20, Grade: A

# 4. **Function with Keyword Arguments** - You can call functions using keyword arguments.
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

# Call the function using keyword arguments
description = describe_person(age=30, city="New York", name="Alice")
print(description)  # Output: Alice is 30 years old and lives in New York.

# 5. **Lambda Function (Anonymous Function)** - A short, unnamed function for simple tasks.
multiply = lambda x, y: x * y  # A lambda function to multiply two numbers

# Call the lambda function
product = multiply(4, 3)
print(f"Product of 4 and 3 is: {product}")  # Output: Product of 4 and 3 is: 12

# 6. **Recursive Function** - A function that calls itself. This example calculates factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Call the recursive function to calculate factorial of 5
fact_of_5 = factorial(5)
print(f"Factorial of 5 is: {fact_of_5}")  # Output: Factorial of 5 is: 120

# 7. **Function with Variable Number of Arguments** - Using *args to accept a variable number of arguments.
def sum_of_numbers(*args):
    return sum(args)  # The sum() function adds all numbers passed in *args

# Call the function with multiple arguments
total_sum = sum_of_numbers(10, 20, 30, 40)
print(f"Sum of numbers: {total_sum}")  # Output: Sum of numbers: 100

# 8. **Function with Keyword Arguments** - Using **kwargs to accept variable keyword arguments.
def describe_person_v2(**kwargs):
    description = ""
    for key, value in kwargs.items():
        description += f"{key}: {value}\n"
    return description

# Call the function with keyword arguments
person_description = describe_person_v2(name="Bob", age=25, city="Los Angeles", occupation="Engineer")
print(person_description)
# Output:
# name: Bob
# age: 25
# city: Los Angeles
# occupation: Engineer
