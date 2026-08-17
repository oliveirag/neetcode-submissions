from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    count = 0 # initialize count
    length = len(nums) # get the length of nums
    for i in range(length): # loop through nums
        if nums[i] == x: # if current element is equal to x increase count
            count += 1
        else:
            continue # if not equal, go to next iteration of loop
    return count

# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
