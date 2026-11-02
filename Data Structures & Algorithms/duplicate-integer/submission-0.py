"""
UNDERSTAND
input: list of int
output: boolean representing whether a number appears more than once in the list

PLAN
double for loop, second loop will check if j matches i, if so return true
otherwise return false
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False