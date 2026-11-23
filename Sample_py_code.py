# print('Hello World!!')
# print(25)
# print("Age: ", 25)

name = 'Yogesh'
# name1 = "Gauri"
# age = 25
# print("Name:", name, " Age:", age)
# print("Name:", name1, " Age:", age)
# print(type(name))
# print(type(name1))
# height = 5.11
# weight = 70

# name = input("Enter your name:")
# print("Hello ", name)

# age = input("Enter your age:")
# print(type(age))
# age = int(age)
# print(type(age))
# height = float(input("Enter Height:"))
"""
Common conversion functions:
int() → convert to integer
float() → convert to float
str() → convert to string
bool() → convert to boolean
"""

"""
Write a program that asks for your name and age, then prints:
Hello <name>, you are <age> years old.
"""
# print("Hello",name, ", you are", age,"years old.")

# Take two numbers as input, convert them to integers, and print their sum.
# num1 = int(input("Enter number 1:"))
# num2 = int(input("Enter number 2:"))
# print("Result=",num1+num2)

# Check and print the data type of these values: 25, 3.5, "Python", False
# print(type(25))
# print(type(3.5))
# print(type("Python"))
# print(type(False))

# print(10>5)
# print(10==5)
# print(10 != 5)
# print(10>=10)
# print(True and False)
# print(True or False)
# print(not True)

x=10
x += 5  # Same as x = x + 5 
x -= 3
x *= 2

"""
# under 18 or 18+
age = int(input("Enter your Age: "))

if age>=18:
    print("Congrates your 18+ !!")
else:
    print("You are minor. Wait for ", 18 - age, "years to get in proper age.")

# marks and grades:
marks= int(input("Enter marks you obtained: "))

if marks>=90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 40:
    print("Pass.")
else:
    print("Fail.")



import math       # Can also import specific things: from math import sqrt, pi
# print(math.sqrt(16))
# print(math.pi)

count = 1
# while count <6:
#     print("Final value: ",6*count)
#     count +=1

# password = ""
# while count<3 and password != 'Password@1234':
#         password = input("Enter Password: ")
#         count +=1
# print("Access granted!!")

for i in range(4):
    print(i*i)
print('----------------------')
for i in range(1, 5):
    print(i)
print('----------------------')
for i in range(1,10,2):       # Print value after 2 places from first value.
    print(i)
print('----------------------')
name = "terminal"
for char in name:
    print(char)
"""
"""
# ==============================================================
# Take a number as input and print whether it is Even or Odd.
num = int(input("Enter number: "))
if num >= 0:
    if num%2 == 0:
        print("Even !!")
    else:
        print("Odd :(")
else:
    print("Number is negetive.")

# Print the multiplication table of any number (using for loop).
# Example: If input is 5 → print 5 × 1 = 5 up to 5 × 10 = 50
num = int(input("Enter a Number: "))
for i in range(1, 11):
    print(num," x ",i, " = " ,num * i)
"""

# Write a program that keeps asking for a number until the user enters 0. Then print the sum of all numbers entered.
total = 0
while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break
    total += num
   
print("Total sum: ", total)

# Import the math module and print the square root of a number given by the user.
import math
# num = int(input("Enter a number: "))
# print(math.sqrt(num))