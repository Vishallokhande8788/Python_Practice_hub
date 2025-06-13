# Define a sample string
my_string = "  Hello, Python World!  "

# 1. `strip()`: Removes leading and trailing whitespaces
stripped_string = my_string.strip()
print(f"Stripped string: '{stripped_string}'")  # Output: 'Hello, Python World!'

# 2. `lower()`: Converts all characters in the string to lowercase
lowercase_string = my_string.lower()
print(f"Lowercase string: '{lowercase_string}'")  # Output: '  hello, python world!  '

# 3. `upper()`: Converts all characters in the string to uppercase
uppercase_string = my_string.upper()
print(f"Uppercase string: '{uppercase_string}'")  # Output: '  HELLO, PYTHON WORLD!  '

# 4. `title()`: Capitalizes the first letter of each word
title_string = my_string.title()
print(f"Title case string: '{title_string}'")  # Output: '  Hello, Python World!  '

# 5. `capitalize()`: Capitalizes only the first character of the string
capitalized_string = my_string.capitalize()
print(f"Capitalized string: '{capitalized_string}'")  # Output: '  hello, python world!  '

# 6. `swapcase()`: Swaps lowercase to uppercase and vice versa
swapped_case_string = my_string.swapcase()
print(f"Swapped case string: '{swapped_case_string}'")  # Output: '  hELLO, pYTHON wORLD!  '

# 7. `replace()`: Replaces a substring with another substring
replaced_string = my_string.replace("Python", "Java")
print(f"Replaced string: '{replaced_string}'")  # Output: '  Hello, Java World!  '

# 8. `find()`: Finds the index of the first occurrence of a substring, or returns -1 if not found
index_of_python = my_string.find("Python")
print(f"Index of 'Python': {index_of_python}")  # Output: 7

# 9. `count()`: Returns the number of times a substring appears in the string
count_python = my_string.count("Python")
print(f"Count of 'Python': {count_python}")  # Output: 1

# 10. `startswith()`: Checks if the string starts with the specified substring
starts_with_hello = my_string.startswith("Hello")
print(f"Starts with 'Hello'? {starts_with_hello}")  # Output: False

# 11. `endswith()`: Checks if the string ends with the specified substring
ends_with_world = my_string.endswith("World!")
print(f"Ends with 'World!'? {ends_with_world}")  # Output: False

# 12. `isalpha()`: Returns True if all characters in the string are alphabetic
is_alpha = "Hello".isalpha()
print(f"Is 'Hello' alphabetic? {is_alpha}")  # Output: True

# 13. `isdigit()`: Returns True if all characters in the string are digits
is_digit = "12345".isdigit()
print(f"Is '12345' a digit? {is_digit}")  # Output: True

# 14. `isalnum()`: Returns True if all characters in the string are alphanumeric
is_alnum = "Hello123".isalnum()
print(f"Is 'Hello123' alphanumeric? {is_alnum}")  # Output: True

# 15. `isspace()`: Returns True if all characters in the string are whitespace
is_space = "   ".isspace()
print(f"Is whitespace only? {is_space}")  # Output: True

# 16. `split()`: Splits the string into a list based on whitespace
words = my_string.split()
print(f"List of words: {words}")  # Output: ['Hello,', 'Python', 'World!']

# 17. `join()`: Joins a list of strings into one string with a specified separator
joined_string = " ".join(["Hello", "Python", "World!"])
print(f"Joined string: '{joined_string}'")  # Output: 'Hello Python World!'

# 18. `zfill()`: Pads the string with zeros on the left, making the string of the specified length
zfilled_string = "42".zfill(5)
print(f"Zero-filled string: '{zfilled_string}'")  # Output: '00042'

# 19. `expandtabs()`: Expands tabs (\t) in the string to spaces (default is 8 spaces per tab)
string_with_tabs = "Hello\tWorld!"
expanded_tabs_string = string_with_tabs.expandtabs(4)
print(f"Expanded tabs string: '{expanded_tabs_string}'")  # Output: 'Hello   World!'

# 20. `partition()`: Splits the string into a 3-part tuple based on the first occurrence of a separator
partitioned_string = my_string.partition("Python")
print(f"Partitioned string: {partitioned_string}")  # Output: ('  Hello, ', 'Python', ' World!  ')

# 21. `rfind()`: Returns the index of the last occurrence of a substring (or -1 if not found)
last_index_of_python = my_string.rfind("Python")
print(f"Last index of 'Python': {last_index_of_python}")  # Output: 7

# 22. `rstrip()`: Removes trailing whitespaces (spaces, tabs, newlines)
rstrip_string = my_string.rstrip()
print(f"Right-stripped string: '{rstrip_string}'")  # Output: '  Hello, Python World!'

# 23. `lstrip()`: Removes leading whitespaces
lstrip_string = my_string.lstrip()
print(f"Left-stripped string: '{lstrip_string}'")  # Output: 'Hello, Python World!  '
