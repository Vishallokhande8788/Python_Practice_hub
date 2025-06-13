# Empty tuple
empty_tuple = ()

# Tuple with multiple values
my_tuple = (1, 2, 3, 4, 5)

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)

# Tuple with a single element (Comma is required)
single_tuple = (10,)  # Correct
not_a_tuple = (10)    # This is just an integer

# Creating a tuple using the tuple() constructor
tuple_from_list = tuple([1, 2, 3, 4])
tuple_from_string = tuple("Python")


# Indexing (0-based index)
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # Output: 10
print(my_tuple[-1]) # Output: 50 (last element)

# Slicing a tuple
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[::2])  # Output: (10, 30, 50) (Step slicing)


# Tuple Creation
tup1 = (1, 2, 3, 4, 5)
tup2 = ("a", "b", "c")
tup3 = (10, 20, 30, 40, 50)

# Accessing Elements
print("First Element:", tup1[0])
print("Last Element:", tup1[-1])
print("Sliced Tuple:", tup1[1:4])  # (2, 3, 4)

# Tuple Methods
print("Count of 3:", tup1.count(3))  # 1
print("Index of 4:", tup1.index(4))  # 3

# Tuple Concatenation
concat_tup = tup1 + tup2
print("Concatenated Tuple:", concat_tup)

# Tuple Repetition
repeat_tup = tup2 * 3
print("Repeated Tuple:", repeat_tup)

# Checking Membership
print("Is 3 in tup1?", 3 in tup1)  # True

# Tuple Length
print("Length of tup1:", len(tup1))

# Converting Between Tuples & Lists
list_from_tup = list(tup1)
list_from_tup.append(6)
tup_from_list = tuple(list_from_tup)
print("Modified Tuple:", tup_from_list)

# Unpacking Tuples
a, b, c, d, e = tup1
print("Unpacked Values:", a, b, c, d, e)

# Nested Tuples
nested_tup = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tup[1])  # (2, 3)
print("Access Nested Element:", nested_tup[1][0])  # 2

# Tuple with *args in Functions
def sum_numbers(*args):
    return sum(args)

print("Sum of Numbers:", sum_numbers(*tup1))

# Using Tuples as Dictionary Keys
coordinates = {
    (10.123, 20.456): "Mumbai",
    (25.789, 30.678): "Delhi"
}
print("Location:", coordinates[(10.123, 20.456)])

# Looping Through a Tuple
print("Looping through tuple:")
for item in tup1:
    print(item, end=" ")


