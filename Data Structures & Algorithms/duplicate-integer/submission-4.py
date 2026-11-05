"""
UNDERSTAND
input - list of ints
output - boolean representing whether the value appears more than once in the array

MATCH: sets

PLAN
create new set
loop thru the list
if the number is in the list
return true
otherwise add that number to the list
if we go thru entire loop and no # is in the set, return False

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



        
