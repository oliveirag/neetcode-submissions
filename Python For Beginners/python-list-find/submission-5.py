from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    for i in range(len(nums)): # loop through indexes
        if nums[i] == target: # if the current value is equal to target
            return i # return the index
    # one-liner
    return nums.index(target)

# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

