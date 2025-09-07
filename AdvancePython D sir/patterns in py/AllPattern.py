# All Common Python Patterns in One File

def square_pattern(n):
    for i in range(n):
        print("* " * n)

def right_triangle(n):
    for i in range(1, n+1):
        print("* " * i)

def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

def pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)

def diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * (2*i-1))
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * (2*i-1))

def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def number_pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def floyds_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()

def binary_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print((i+j) % 2, end=" ")
        print()

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def hollow_diamond(n):
    for i in range(n):
        print(" "*(n-i-1), end="")
        for j in range(2*i+1):
            if j == 0 or j == 2*i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n-2, -1, -1):
        print(" "*(n-i-1), end="")
        for j in range(2*i+1):
            if j == 0 or j == 2*i:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# Run all patterns
n = 5
print("Square Pattern:")
square_pattern(n)

print("\nRight Triangle:")
right_triangle(n)

print("\nInverted Right Triangle:")
inverted_right_triangle(n)

print("\nPyramid:")
pyramid(n)

print("\nInverted Pyramid:")
inverted_pyramid(n)

print("\nDiamond:")
diamond(n)

print("\nNumber Triangle:")
number_triangle(n)

print("\nNumber Pyramid:")
number_pyramid(n)

print("\nFloyd's Triangle:")
floyds_triangle(n)

print("\nBinary Triangle:")
binary_triangle(n)

print("\nHollow Square:")
hollow_square(n)

print("\nHollow Diamond:")
hollow_diamond(n)
