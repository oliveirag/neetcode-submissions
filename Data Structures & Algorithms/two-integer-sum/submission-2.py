"""
UNDERSTAND:
Given a list of integers, and a integer target representing the number we have to add up two indices
Returning a list containing the two indices which add up to target
Edge cases: none, every input has exactly one pair of indices i and j that satisfy the condition

MATCH:
Double for loop

PLAN:
loop thru nums[i]
loop thru nums[j]
if nums[i] + nums[j] == target
return [i,j]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]
