import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = [] # create max heap
    for num in nums: # for each number in nums
        heapq.heappush(max_heap, -num) # add number to max_heap and negate it
    
    reversed_list = [] # create new list
    while len(max_heap) > 0:
        reversed_list.append(-heapq.heappop(max_heap))

    return reversed_list

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
