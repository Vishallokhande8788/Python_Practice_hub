# # 24/03/2025

# import math

# print(math.e)  # Prints Euler's number (approx. 2.718), the base of natural logarithms
# print(math.pi)  # Prints the value of Pi (approx. 3.14159), the ratio of a circle's circumference to its diameter
# print(math.ceil(10.6))  # Rounds 10.6 upwards to the nearest integer, i.e., 11
# print(math.floor(10.6))  # Rounds 10.6 downwards to the nearest integer, i.e., 10
# print(math.fabs(-10.6))  # Returns the absolute value of -10.6, i.e., 10.6
# print(math.factorial(5))  # Calculates the factorial of 5 (5! = 5 * 4 * 3 * 2 * 1 = 120)
# print(math.sqrt(100))  # Calculates the square root of 100, i.e., 10
# print(math.fsum([1, 2, 3, 4, 5, 6]))  # Returns the sum of a list of floating-point numbers with high precision (21.0)


# ###### EXTRA EG  ###############

# # Constants
# print(math.e)  # Euler's number (base of natural logarithms), approximately 2.718
# print(math.pi)  # Pi, the ratio of a circle's circumference to its diameter, approximately 3.14159
# print(math.tau)  # Tau, equal to 2 * Pi, approximately 6.28318
# print(math.inf)  # Represents positive infinity
# print(math.nan)  # Represents "Not a Number" (NaN)

# # Trigonometric functions
# print(math.sin(math.pi / 2))  # Sine of Pi/2, which is 1
# print(math.cos(math.pi))  # Cosine of Pi, which is -1
# print(math.tan(math.pi / 4))  # Tangent of Pi/4, which is 1
# print(math.asin(1))  # Inverse sine of 1, which is Pi/2
# print(math.acos(-1))  # Inverse cosine of -1, which is Pi
# print(math.atan(1))  # Inverse tangent of 1, which is Pi/4
# print(math.degrees(math.pi))  # Converts Pi radians to degrees (180 degrees)
# print(math.radians(180))  # Converts 180 degrees to radians (Pi)

# # Logarithmic functions
# print(math.log(10))  # Natural logarithm of 10 (log base e)
# print(math.log10(100))  # Logarithm of 100 base 10, which is 2
# print(math.log2(8))  # Logarithm of 8 base 2, which is 3

# # Power and Exponential functions
# print(math.exp(1))  # Exponential of 1, i.e., e^1 ≈ 2.718
# print(math.pow(2, 3))  # 2 raised to the power of 3, i.e., 8
# print(math.sqrt(16))  # Square root of 16, which is 4
# print(math.isqrt(16))  # Integer square root of 16, which is 4 (returns an integer)

# # Hyperbolic functions
# print(math.sinh(1))  # Hyperbolic sine of 1
# print(math.cosh(1))  # Hyperbolic cosine of 1
# print(math.tanh(1))  # Hyperbolic tangent of 1

# # Rounding functions
# print(math.ceil(10.1))  # Ceil of 10.1 (rounds up), which is 11
# print(math.floor(10.9))  # Floor of 10.9 (rounds down), which is 10
# print(math.trunc(10.6))  # Truncates 10.6 (removes the decimal), which is 10

# # Absolute value
# print(math.fabs(-10.6))  # Absolute value of -10.6, which is 10.6

# # Factorial and Combinations
# print(math.factorial(5))  # Factorial of 5 (5! = 120)
# print(math.comb(5, 2))  # Number of ways to choose 2 items from 5, i.e., 10
# print(math.perm(5, 2))  # Number of ways to arrange 2 items from 5, i.e., 20

# # Sum with precision
# print(math.fsum([1.0, 2.0, 3.0, 4.0]))  # Sum of the numbers with high precision, i.e., 10.0

# # Special functions
# print(math.gcd(60, 48))  # Greatest common divisor of 60 and 48, which is 12
# print(math.lcm(60, 48))  # Least common multiple of 60 and 48, which is 240

# # Checking if a number is a perfect square
# print(math.isqrt(25))  # Integer square root, returns 5 (perfect square check)
# print(math.isqrt(20))  # Integer square root, returns 4 (not a perfect square)

# # Checking if a number is NaN or Infinite
# print(math.isnan(math.nan))  # Returns True, as math.nan is Not a Number
# print(math.isinf(math.inf))  # Returns True, as math.inf represents positive infinity

# # Taking user input for the radius of the circle
# import math

# UserInput = int(input("Enter the radius of the circle: "))
# area = math.pi * (UserInput ** 2) # Calculating the area of the circle (Area = π * r^2)
# print(f"The area of the circle with radius {UserInput} is: {area}")

