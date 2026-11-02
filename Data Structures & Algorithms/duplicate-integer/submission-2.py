"""
better solution using sets

UNDERSTAND:
input - list of int
output - boolean representing whether a number appears more than once in the list

MATCH: sets

PLAN:
create a set representing the numbers seen, loop thru each number in list, if it is already in list, return true
otherwise, add it to list
if we went thru entire list with no matches found return false
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
                if num in seen:
                    return True
                seen.add(num)
        return False
