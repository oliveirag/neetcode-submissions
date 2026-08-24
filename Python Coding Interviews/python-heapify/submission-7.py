import heapq
from typing import List

# NOTE: heapify does NOT create a new string, it modifies the original
def heapify_strings(strings: List[str]) -> List[str]:
    heapq.heapify(strings)
    return strings

def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)
    return integers

def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums) # transform the list into a heap
    sort = [] # create new list
    for i in range(len(nums)): # loop thru each number in heap
        sort.append(heapq.heappop(nums)) # add smallest priority to the list first
    return sort # return the sorted list in ascending order


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
