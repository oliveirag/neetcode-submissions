"""
USING 1 DICTIONARY

UNDERSTAND:
input - two strings
output - boolean representing if the two strings are anagrams
edge cases: if string is empty

MATCH: hash maps

PLAN:
if strings are not the same length:
    return False
create hashmap
loop thru first word:
    if char is in the hashmap:
        increase its count
    if not:
        add it to the hashmap
loop thru second word:
    if char exists in hashmap and its count is greater than zero:
        decrement the count since you are "using" it
    else:
        word is not an anagram return false
if we go thru entire loop return true
(both words are anagrams)
    
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram = {}
        for char in s:
            if char in anagram:
                anagram[char] += 1
            else:
                anagram[char] = 1
        for char in t:
            if char in anagram and anagram[char] > 0:
                anagram[char] -= 1
            else:
                return False
        return True
        