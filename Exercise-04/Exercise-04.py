# Q4: Triangle Perimeters
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
# Here's a sample run of the program (user input is in bold italics):
# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

str_side1: str = input("What is the length of side 1? ")

str_side2: str = input("What is the length of side 2? ")

str_side3: str = input("What is the length of side 3? ")

float_side1: float = float(str_side1)

float_side2: float = float(str_side2)

float_side3: float = float(str_side3)

perimeter: float = float_side1 + float_side2 + float_side3

print(f"The perimeter of the triangle is {perimeter}")