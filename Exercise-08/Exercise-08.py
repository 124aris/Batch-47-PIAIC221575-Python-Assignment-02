# Q8: Pop method
# You have a list named items with the elements [10, 20, 30, 40]. If you use the pop method without any arguments, what will the list look like and what value will be removed?

from typing import List

items: List[int] = [10, 20, 30, 40]

remove_item: int = items.pop()

print(items)

print(remove_item)