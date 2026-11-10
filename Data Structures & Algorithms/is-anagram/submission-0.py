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
        add each letter to the hashmap


"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = set()
        for char in s:
            anagram.add(char)
        for char in t:
            if char not in anagram:
                return False
        return True

        
        
        