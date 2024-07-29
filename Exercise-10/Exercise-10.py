# Q10: Get last element
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

from typing import List

def get_last_element(list: List) -> None:
    print(list[-1])

example: List[int] = [1, 2, 3, 4, 5, 6]

get_last_element(example)