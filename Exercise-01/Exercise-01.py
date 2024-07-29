# Q1: Add two numbers
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

str_num1: str = input("Enter the first number: ")

str_num2: str = input("Enter the second number: ")

int_num1: int = int(str_num1)

int_num2: int = int(str_num2)

sum: int = int_num1 + int_num2

print(f"The sum of {int_num1} and {int_num2} is {sum}.")