# This program demonstrates typecasting and taking user input.

# 1. Taking user input:
# Using input() function to get user input. By default, input() returns a string.
print("Enter your age:")
user_input_age = input()  # Taking user input as a string
print(f"Your age (as string): {user_input_age}")

# 2. Typecasting (Type Conversion):
# Convert the string input to an integer using int().
user_age = int(user_input_age)  # Convert the string to an integer
print(f"Your age (as integer): {user_age}")

# 3. Perform a mathematical operation (example: add 5 years to the user's age)
new_age = user_age + 5
print(f"In 5 years, you will be {new_age} years old.")

# 4. Taking another input: Let's take the user's height as a floating point number.
print("Enter your height in meters:")
user_input_height = input()  # Taking user input for height as a string
print(f"Your height (as string): {user_input_height}")

# Typecasting the height to float (to allow decimal values)
user_height = float(user_input_height)  # Convert the string to a float
print(f"Your height (as float): {user_height}")

# 5. Perform an operation using the height (example: calculate the total height after growing 0.2 meters)
new_height = user_height + 0.2
print(f"After growing 0.2 meters, your height will be {new_height} meters.")

# 6. Combining both age and height for a fun message:
print(f"Hello, {user_age} years old, {user_height} meters tall person!")
