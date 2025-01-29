# Example of 1. Simple `if` statement
print("1. Simple `if` statement:")
x = 10
if x > 5:
    print("x is greater than 5.")  # This will be printed because x is indeed greater than 5.

print("\n")

# Example of 2. `if-else` statement
print("2. `if-else` statement:")
y = 3
if y > 5:
    print("y is greater than 5.")
else:
    print("y is less than or equal to 5.")  # This will be printed because y is less than 5.

print("\n")

# Example of 3. `if-else-elif` statement
print("3. `if-else-elif` statement:")
z = 7
if z > 10:
    print("z is greater than 10.")
elif z == 7:
    print("z is equal to 7.")  # This will be printed because z is 7.
else:
    print("z is less than 7.")

print("\n")

# Example of 4. Nested `if-else-elif` statement
print("4. Nested `if-else-elif` statement:")

a = 4
b = 7
if a > 5:
    if b > 5:
        print("Both a and b are greater than 5.")
    else:
        print("a is greater than 5, but b is not.")
elif a == 4:
    if b > 5:
        print("a is equal to 4, but b is greater than 5.")  # This will be printed because a is 4 and b is greater than 5.
    else:
        print("a is equal to 4, and b is less than or equal to 5.")
else:
    print("Neither condition is met.")

print("\n")
