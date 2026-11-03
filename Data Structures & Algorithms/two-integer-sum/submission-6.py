"""
OPTIMAL SOLUTION using hash maps

UNDERSTAND:
input: list of ints, and an int target representing the # we are trying to add up to
output: list with the two indices adding up to target

MATCH:
dictionaries / hash maps

PLAN:
create a dict
for each number and index in the list
initialize the difference
check if the number that adds to the target exist in our hashmap
if it does return the list of that index and our current index
if not, add the value to our hash map
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in new_dict:
                return [new_dict[diff], i]
            new_dict[num] = i

        
        