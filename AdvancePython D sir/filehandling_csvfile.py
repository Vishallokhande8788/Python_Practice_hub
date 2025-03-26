# # 26/03/2025

# # Working with csv (comma  sepreated value .xls ) file 

# import csv

# # Open the file in write mode ('w') to write data into the CSV
# with open("product.csv", "w", newline='') as f:
#     # Create a CSV writer object
#     csv_writer = csv.writer(f)
    
#     # Writing the header row
#     csv_writer.writerow(["Product Name", "Price", "Quantity"])
    
#     # Writing data row
#     csv_writer.writerow([111, "Katrin", 100])

# print("Product saved")

## eg : write data how  many produst do you want to save


import csv

# Open the file in write mode
f = open('product.csv', 'w', newline='')

# Create a CSV writer object
csv_writer = csv.writer(f)

# Write the header row
csv_writer.writerow(["Pid", "Product Name", "Price", "Quantity"])

# Initialize product id
pid = 101

# Ask the user for the number of products to save
userChoice = int(input("How many products do you want to save: "))

# Loop to take user input for each product
for i in range(userChoice):
    productName = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    
    # Write the product details to the CSV file
    csv_writer.writerow([pid, productName, price, quantity])
    
    # Increment the product id
    pid += 1

# Close the file
f.close()

# Print success message
print("Products saved successfully!")

