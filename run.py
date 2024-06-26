# ------------>   1   <---------------

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print(f"The Area of Rectangle is:{area}")

# # ------------>   2   <---------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
# ------------>   3   <---------------

reversed_string = input("Enter a String:")

print(reversed_string[::-1]) 

# ------------>   4   <---------------
number = int(input("Enter a number:"))

factorial_number = 1

for i in range(1, number + 1):
    factorial_number *= i

print(f"The factorial of {number} is: {factorial_number}")

# ------------>   5   <---------------

input_string = input("Enter a string: ")

if input_string == input_string[::-1]:
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")

# ------------>   6   <---------------

num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())

largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print("The largest number is:", largest)

# ------------>   7   <---------------

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest = {simple_interest}")

# ------------>   8   <---------------

sentence = input("Enter a sentence: ")

words = sentence.split()
word_length = len(words)

print(f"The number of words in the sentence is: {word_length}")

# ------------>   9   <---------------
number = input("Enter a number: ")

sum_of_digits = 0

for digit in number:
    sum_of_digits += int(digit)

print("The sum of digits in the number is:", sum_of_digits)
