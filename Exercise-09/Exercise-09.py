# Q9: Index Method
# You have a list called colors with the elements ['red', 'blue', 'green', 'yellow']. If you use the index method to find the position of 'green', what will the index be?

from typing import List

colors: List[str] = ['red', 'blue', 'green', 'yellow']

index: int = colors.index('green')

print(index)