numbers = [2, 4, 6, 8, 10]

# Step 1: Double each number using map and a lambda function
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Step 2: Find the product of the doubled numbers using a loop
product_of_doubled = 1
for number in doubled_numbers:
    product_of_doubled *= number

print(product_of_doubled)
