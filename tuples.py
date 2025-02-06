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
