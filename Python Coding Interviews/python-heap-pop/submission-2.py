import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    new_list = [] # create a new list
    for i in range(len(heap)): # while there are elements in the heap
        element = heapq.heappop(heap) # store the smallest priority in element
        new_list.append(element) # add element to list
    return new_list # return list

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
