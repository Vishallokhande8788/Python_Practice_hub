
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






# 26/03/2025

# #tell(): it will return current position of file pointer

f=open('f1.txt','r')
print('File Pointer Location : ' ,f.tell())
print(f.read(2))
print('file pointer location : ', f.tell())
print(f.read(2))
print('file pointer location : ', f.tell())
print(f.read(4))
print('file pointer location : ', f.tell())

##  moving file pointer a a specific location 

# # f.seek(12) :

# print(f.read(4))

# f=open('f5.txt','w')
# f.write("All Students are stupid")
# f.seek(17)
# f.write("Smart!!!!")
# f.close()