# 1. Arithmetic Operators
# These operators are used for basic arithmetic operations like addition, subtraction, etc.

# Addition
a = 10
b = 5
print("Addition:", a + b)  # Output: 15

# Subtraction
print("Subtraction:", a - b)  # Output: 5

# Multiplication
print("Multiplication:", a * b)  # Output: 50

# Division (float result)
print("Division (float result):", a / b)  # Output: 2.0

# Floor Division (integer result, removes decimal)
print("Floor Division:", a // b)  # Output: 2

# Modulus (remainder of division)
print("Modulus (remainder):", a % b)  # Output: 0

# Exponentiation (power of a number)
print("Exponentiation (a^b):", a ** b)  # Output: 100000

# 2. Comparison Operators
# These operators compare two values and return a boolean result (True or False).

# Equal to
print("Equal to:", a == b)  # Output: False

# Not equal to
print("Not equal to:", a != b)  # Output: True

# Greater than
print("Greater than:", a > b)  # Output: True

# Less than
print("Less than:", a < b)  # Output: False

# Greater than or equal to
print("Greater than or equal to:", a >= b)  # Output: True

# Less than or equal to
print("Less than or equal to:", a <= b)  # Output: False

# 3. Assignment Operators
# These operators are used to assign values to variables.

# Assigning value
x = 10
print("Assigned value to x:", x)  # Output: 10

# Add and assign (x = x + 5)
x += 5
print("x after x += 5:", x)  # Output: 15

# Subtract and assign (x = x - 3)
x -= 3
print("x after x -= 3:", x)  # Output: 12

# Multiply and assign (x = x * 2)
x *= 2
print("x after x *= 2:", x)  # Output: 24

# Divide and assign (x = x / 6)
x /= 6
print("x after x /= 6:", x)  # Output: 4.0

# Floor divide and assign (x = x // 2)
x //= 2
print("x after x //= 2:", x)  # Output: 2

# Modulus and assign (x = x % 3)
x %= 3
print("x after x %= 3:", x)  # Output: 2

# Exponentiate and assign (x = x ** 3)
x **= 3
print("x after x **= 3:", x)  # Output: 8

# 4. Logical Operators
# These operators are used to combine conditional statements.

# AND (True if both conditions are True)
condition1 = True
condition2 = False
print("AND (True if both are True):", condition1 and condition2)  # Output: False

# OR (True if at least one condition is True)
print("OR (True if at least one is True):", condition1 or condition2)  # Output: True

# NOT (True if the condition is False)
print("NOT (inverts the boolean):", not condition1)  # Output: False

# 5. Identity Operators
# These operators compare the memory locations of two objects.

# "is" (checks if both variables point to the same object in memory)
a = [1, 2, 3]
b = a
print("a is b (check if both point to same object):", a is b)  # Output: True

# "is not" (checks if two variables do not point to the same object in memory)
c = [1, 2, 3]
print("a is not c (check if both point to different objects):", a is not c)  # Output: True

# 6. Membership Operators
# These operators are used to test if a value is present in a sequence (like a list or string).

# "in" (True if value is found in the sequence)
fruits = ["apple", "banana", "cherry"]
print("'banana' in fruits:", "banana" in fruits)  # Output: True

# "not in" (True if value is not found in the sequence)
print("'orange' not in fruits:", "orange" not in fruits)  # Output: True

# 7. Bitwise Operators
# These operators work on the binary representation of numbers.

# AND (&)
num1 = 5  # 101 in binary
num2 = 3  # 011 in binary
print("Bitwise AND:", num1 & num2)  # Output: 1 (001 in binary)

# OR (|)
print("Bitwise OR:", num1 | num2)  # Output: 7 (111 in binary)

# XOR (^)
print("Bitwise XOR:", num1 ^ num2)  # Output: 6 (110 in binary)

# NOT (~)
print("Bitwise NOT:", ~num1)  # Output: -6 (inverts bits)

# Left shift (<<)
print("Left shift (num1 << 1):", num1 << 1)  # Output: 10 (1010 in binary)

# Right shift (>>)
print("Right shift (num1 >> 1):", num1 >> 1)  # Output: 2 (010 in binary)
