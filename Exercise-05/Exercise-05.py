# Q5: Square Number
# Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0

str_num: str = input("Type a number to see its square: ")

float_num: float = float(str_num)

square: float = float_num * float_num

print(f"{float_num} squared is {square}")