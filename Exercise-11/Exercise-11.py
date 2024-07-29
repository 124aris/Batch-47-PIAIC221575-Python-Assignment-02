# Q11: Get a List
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1
# Enter a value: 2
# Enter a value: 3
# Enter a value:
# Here's the list: ['1', '2', '3']

from typing import List

def get_list() -> None:
    values_list: List = []
    while True:
        input_value: str = input("Enter a value: ")
        if input_value == "":
            break
        values_list.append(input_value)
    print("Here's the list:", values_list)

get_list()