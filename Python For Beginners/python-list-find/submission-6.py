from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    # version 1: loop through indexes
    for i in range(len(nums)):
        if nums[i] == target: # if the current value is equal to target
            return i # return the index
    # version 2: one-liner
    return nums.index(target)

# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

