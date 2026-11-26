from typing import List

# list comprehension
def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    grid = [[value] * cols for _ in range(rows)] # "[value] * cols" creates the first list of values
    return grid                                  # "for _ in range(rows)" multiplies that list by rows
                                                 # the _ is a throwaway loop variable
# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
