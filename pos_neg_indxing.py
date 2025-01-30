# List for demonstration
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Positive Indexing (Indexing from the beginning, starting from 0)
print("Positive Indexing:")
print(f"Element at index 0 (first element): {fruits[0]}")  # First element (apple)
print(f"Element at index 1 (second element): {fruits[1]}")  # Second element (banana)
print(f"Element at index 4 (fifth element): {fruits[4]}")  # Fifth element (elderberry)


# Negative Indexing (Indexing from the end, starting from -1)
print("\nNegative Indexing:")
print(f"Element at index -1 (last element): {fruits[-1]}")  # Last element (elderberry)
print(f"Element at index -2 (second-to-last element): {fruits[-2]}")  # Second to last (date)
print(f"Element at index -4 (fourth-to-last element): {fruits[-4]}")  # Fourth from last (banana)

# Combining Positive and Negative Indexing with Slicing
print("\nPositive and Negative Indexing with Slicing:")
print(f"Elements from index 1 to 3 (positive indexing): {fruits[1:4]}")  # Elements from index 1 to 3 (banana, cherry, date)
print(f"Elements from index -4 to -2 (negative indexing): {fruits[-4:-1]}")  # Elements from index -4 to -2 (banana, cherry, date)

# Accessing a sublist with Positive and Negative Indexing
print("\nAccessing a Sublist Using Both Indexing Types:")
positive_negative_slice = fruits[1:-1]  # Positive indexing start, negative indexing end
print(f"Sublist from index 1 to the second-to-last: {positive_negative_slice}")  # banana, cherry, date
