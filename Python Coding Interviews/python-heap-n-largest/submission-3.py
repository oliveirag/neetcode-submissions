import heapq
from typing import List


def get_max_element(arr: List[int]) -> int:
    return heapq.nlargest(1, arr)[0] # return the value of smallest element


def get_max_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    return heapq.nlargest(4, arr) # return the 4 largest elements (already decreasing order)


def get_max_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    max_2 = heapq.nlargest(2, arr) # return the 2 largest elements
    max_2.reverse() # reverse the list so it's in increasing order
    return max_2 # return reversed list



# do not modify below this line
print(get_max_element([1, 2, 3]))
print(get_max_element([3, 2, 1, 4, 6, 2]))
print(get_max_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_max_4_elements([4, 9, 7, 3, 2, 7, 4, 6, 2]))
print(get_max_4_elements([4, 9, 7, 2, 1, 3, 2, 3, 4, 6, 2, 3]))
print(get_max_4_elements([4, 7, 2, 3, 2, 4, 6, 2]))

print(get_max_2_elements([4, 5, 3, 7]))
print(get_max_2_elements([8, 8, 7, 9]))
print(get_max_2_elements([1, 2, 3, 9, 8, 7, 6]))

