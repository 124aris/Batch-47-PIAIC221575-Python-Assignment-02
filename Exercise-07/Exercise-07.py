# Q7: Creating a list You have two lists:
# list1 with elements [1, 2, 3]
# list2 with elements [4, 5, 6].
# Create a program using list method to add the elements of list2 to list1.

from typing import List

list1: List[int] = [1, 2, 3]

list2: List[int] = [4, 5, 6]

list1.extend(list2)

print(list1)