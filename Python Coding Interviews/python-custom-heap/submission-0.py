import heapq
from typing import List

def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = [] # create new heap

# trick to turn min heap into max heap using tuple: negating the number means the largest original number becomes the smallest negated number, so it gets popped first
# the original value (num), is kept in the tuple to be retrieved later without negating back

    for num in nums: # for each number in nums
        pair = (-num, num) # create a tuple for each number
        heapq.heappush(max_heap, pair) # push pair onto max_heap

    res = [] # initialize list to hold the final sorted output
    while len(max_heap) > 0: # while there are elements in the heap
        pair = heapq.heappop(max_heap) # pop the smallest tuple (largest original number)
        original = pair[1] # extract second element of tuple (original number)
        res.append(original) # add the original number to result list

    return res # return the final list sorted and reversed

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
