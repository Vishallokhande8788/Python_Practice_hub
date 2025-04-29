

'''
# Operator overloading in Python allows you to define how operators (like `+`, `-`, `*`, etc.) behave for your custom objects.

# Example (in short):
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading +
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__
print(p3.x, p3.y)  # Output: 4 6

# You override special magic methods like:
'''
'''
- `__add__` for `+`
- `__sub__` for `-`
- `__mul__` for `*`
- `__eq__` for `==`
- `__lt__` for `<`, etc.
'''


print(10+20)
print('java' + " python")

print(2*3)
print('java'*4)

class Book :
    def __init__(self , pages):
        self.pages = pages
        
    def __add__ (self , other):
        print('add magic method called ')
        return self.pages + other.pages
    

b1 = Book(400)
b2 = Book(500)
b3 = Book(600)

print("Total pages : " , b1 + b2 )
print("Total pages : " , b2 + b3)
