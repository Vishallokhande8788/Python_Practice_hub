# 1. For loop with a list
print("1. For loop with a list:")
my_list = [10, 20, 30, 40, 50]
for num in my_list:
    print(num)
    
print("\n")  # Newline for separation

# 2. For loop with range()
print("2. For loop with range:")
for i in range(5):  # Loop from 0 to 4
    print(i)

print("\n")  # Newline for separation

# 3. While loop with a condition
print("3. Basic while loop:")
counter = 0
while counter < 5:
    print(counter)
    counter += 1  # Increment the counter by 1 each time
    
print("\n")  # Newline for separation

# 4. While loop with an else statement
print("4. While loop with else:")
n = 0
while n < 3:
    print("Inside the while loop:", n)
    n += 1
else:
    print("Exited the while loop.")
    
print("\n")  # Newline for separation

# 5. Infinite while loop with break
print("5. Infinite while loop with break:")
count = 0
while True:  # This is an infinite loop
    count += 1
    print("Loop count:", count)
    
    if count == 5:  # When count reaches 5, break the loop
        print("Breaking the loop.")
        break  # Exit the loop
        
print("\n")  # Newline for separation

# 6. For loop with break
print("6. For loop with break:")
for i in range(10):
    if i == 5:  # Break when i reaches 5
        print("Breaking the for loop at i =", i)
        break
    print(i)
    
print("\n")  # Newline for separation

# 7. While loop with continue (skip iteration)
print("7. While loop with continue:")
x = 0
while x < 5:
    x += 1
    if x == 3:  # Skip printing 3
        continue
    print(x)
    
print("\n")  # Newline for separation

# 8. For loop with continue (skip iteration)
print("8. For loop with continue:")
for i in range(1, 6):
    if i == 4:  # Skip printing 4
        continue
    print(i)
