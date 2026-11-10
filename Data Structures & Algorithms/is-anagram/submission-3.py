"""
UNDERSTAND:
input - two strings
output - boolean representing if the two strings are anagrams
edge cases: if string is empty

MATCH: hash maps

PLAN:
create hashmap
loop thru first word:
    add each letter to the hashmap
loop thru second word:
    IF letter does not exist in hashmap
        return False
return True if loop ends
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for char in s:
            if char in anagram:
                anagram[char] = 0
            else:
                anagram[char] = 1
        for char in t:
            if char not in anagram:
                return False
        return True

        
        
        