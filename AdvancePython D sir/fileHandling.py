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







# # Open the file "file.txt" in write mode ("w")
# f = open("file.txt", "w")

# # List of drinks (each item includes a newline character at the end)
# drinks = ['kingfisher\n', 'coke\n', 'water\n', 'milk\n']

# # Write the list of drinks into the file
# f.writelines(drinks)

# # Close the file after writing
# f.close()

# # Print confirmation that the data has been written into the file
# print("Data written into the file")









# ## reading data from the file :

# # Open the file "file.txt" in read mode ("r")
# f = open("file.txt", "r")

# # Read the entire content of the file and store it in the variable `data`
# data = f.read()
# print("Complete file content:")
# print(data)

# # Move the file pointer back to the start of the file
# f.seek(0)

# # Read the first 5 characters from the file and store it in the variable `data1`
# data1 = f.read(5)
# print("First 5 characters:")
# print(data1)

# # Check if the file is readable (this returns a boolean)
# print("Is file readable:", f.readable())

# # Move the file pointer back to the start again before reading lines
# f.seek(0)

# # Read all lines from the file into a list and print each line
# allLine = f.readlines()
# print("Reading each line:")
# for line in allLine:
#     print(line)

# # Close the file after reading
# f.close()

# #example : create file f1, f2 , f3 and transfer f1 , f2 file data into f3

# f1 = open("f1.txt", "a")
# f1.write("AAAAAAAAAAA\n")
# f1.write("BBBBBBBBBBB\n")
# f1.close()

# f2 = open("f2.txt", "a")
# f2.write("CCCCCCCCCCC\n")
# f2.write("DDDDDDDDDDD\n")
# f2.close()

# f3 = open("f3.txt", "a")

# f1 = open("f1.txt", "r")
# f3.write(f1.read())  
# f1.close()

# f2 = open("f2.txt", "r")
# f3.write(f2.read()) 

# f3.close()

# print("Contents of f1.txt and f2.txt have been appended to f3.txt")

# #or

# f1 = open("f1.txt", "r")
# f2 = open("f2.txt", "r")
# f3 = open("f3.txt", "w")
# f3.write(f1.read())
# f3.write(f2.read())
# f1.close()
# f2.close()
# f3.close()