# Q6: Delete a number 
# Consider a list named numbers with the elements [1, 2, 3, 4, 5]. Use list method to delete the number 3?

from typing import List

numbers: List[int] = [1, 2, 3, 4, 5]

numbers.remove(3)

print(numbers)