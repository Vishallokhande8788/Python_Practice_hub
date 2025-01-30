# Creating Lists
empty_list = []  # An empty list
numbers = [1, 2, 3, 4, 5]  # A list of numbers
fruits = ['apple', 'banana', 'cherry']  # A list of strings
mixed_list = [1, 'apple', 3.14, True]  # A mixed list with different data types

# Accessing List Elements
print(f"First element of numbers: {numbers[0]}")  # Indexing starts from 0
print(f"Last element of fruits: {fruits[-1]}")  # Negative indexing starts from the end

# Slicing Lists
subset_numbers = numbers[1:4]  # Slice from index 1 to 3 (exclusive of 4)
print(f"Subset of numbers (index 1 to 3): {subset_numbers}")
subset_fruits = fruits[:2]  # Slice from the start to index 1 (exclusive of 2)
print(f"Subset of fruits (first two): {subset_fruits}")

# Modifying Lists
numbers[2] = 10  # Change the third element of numbers to 10
print(f"Updated numbers list: {numbers}")

# Adding Elements
numbers.append(6)  # Add an element at the end of the list
print(f"After appending: {numbers}")

# Inserting Elements
numbers.insert(2, 7)  # Insert 7 at index 2
print(f"After inserting 7 at index 2: {numbers}")

# Removing Elements
numbers.remove(10)  # Remove the first occurrence of 10
print(f"After removing 10: {numbers}")

# Popping Elements
popped_element = numbers.pop()  # Remove and return the last element
print(f"After popping: {numbers}, popped element: {popped_element}")

# List Length
length_of_numbers = len(numbers)
print(f"Length of numbers list: {length_of_numbers}")

# Checking if an Element Exists
if 'banana' in fruits:
    print(f"Banana is in the fruits list.")
else:
    print(f"Banana is not in the fruits list.")

# List Concatenation
combined_list = numbers + fruits  # Combine two lists
print(f"Combined list: {combined_list}")

# List Repetition
repeated_list = [1, 2, 3] * 3  # Repeat a list three times
print(f"Repeated list: {repeated_list}")

# Sorting Lists
unsorted_numbers = [3, 1, 4, 2, 5]
unsorted_numbers.sort()  # Sort the list in ascending order
print(f"Sorted numbers: {unsorted_numbers}")

# Reversing Lists
unsorted_numbers.reverse()  # Reverse the list
print(f"Reversed numbers: {unsorted_numbers}")

# List Comprehensions (Creating a New List)
squared_numbers = [x**2 for x in numbers]  # Create a new list of squared numbers
print(f"Squared numbers: {squared_numbers}")

# Nested Lists
nested_list = [1, [2, 3], 4]  # List inside a list
print(f"Nested list: {nested_list}")
print(f"Accessing element inside nested list: {nested_list[1][0]}")  # Access 2 from the nested list

# Iterating through a List
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Copying a List
numbers_copy = numbers.copy()  # Create a shallow copy of the numbers list
print(f"Copied numbers list: {numbers_copy}")

# Clearing a List
numbers.clear()  # Remove all elements from the list
print(f"Cleared numbers list: {numbers}")
