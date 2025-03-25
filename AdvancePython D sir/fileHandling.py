# # 25 / 03 / 2025

# # file handling
# # how to open file in python 
# #  syntay : ("filename", " opening mode")

# # opening mode :
# # w: write mode (new  file  is created)
# # r: read mode (new flwe wont ceated)
# # a: append mode (new file is created)

# # example :
# # Open the file "file.txt" in write mode ("w")
# f = open("file.txt", "w")

# # Print a message indicating that the file has been opened successfully
# print("file is opened successfully")

# # Check if the file is writable and print the result
# print("is file writable : ", f.writable())

# # Check if the file is readable and print the result
# print("is file readable : ", f.readable())

# # Print the name of the file
# print("file name : ", f.name)

# # Print the mode in which the file was opened (in this case, 'w' for write)
# print("file mode : ", f.mode)

# # Check if the file is closed and print the result (it should be False right now)
# print("is file closed : ", f.closed)

# # Close the file
# f.close()

# # Check if the file is closed after calling close() and print the result (it should be True now)
# print("file is closed : ", f.closed)


# # Writing data into the file :
# # Open the file "file.txt" in write mode ("w")
# f = open("file.txt", "w")

# # Write a line of text into the file with a newline at the end
# f.write("Hello World\n")

# # Write another line of text into the file with a newline at the end
# f.write("This is a new line\n")

# # Write a third line of text into the file with a newline at the end
# f.write("This is the second line\n")

# # Close the file after writing
# f.close()

# Open the file "file.txt" in write mode ("w")
f = open("file.txt", "w")

# List of drinks (each item includes a newline character at the end)
drinks = ['kingfisher\n', 'coke\n', 'water\n', 'milk\n']

# Write the list of drinks into the file
f.writelines(drinks)

# Close the file after writing
f.close()

# Print confirmation that the data has been written into the file
print("Data written into the file")
