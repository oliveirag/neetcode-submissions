from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    for num in nums1: # for each number in the first list
        sorted_set.add(num) # add that number to the sorted set (duplicates are ignored)
    
    for num in nums2: # for each number in the second list
        sorted_set.discard(num) # remove that number from the sorted set if number is there
                                # .discard does nothing if value is not in the set
                                # using .remove could give us an error

    return list(sorted_set)[:3] # convert to a list of the first three values in sorted order

# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
