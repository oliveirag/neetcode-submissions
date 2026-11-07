"""
UNDERSTAND:
input - string
output - boolean representing if the string is a palindrome

MATCH: two pointer

PLAN: 
create a new palindrome remove all whitespaces from the string
initialize left
initialize right
while left is less than or equal to right (as long as they dont cross)
if the character pointed to by left is the same as character pointed to by right
    increment left by 1
    decrement right by 1
else: (if characters are not the same)
    return False
return true after the while loop

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''.join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(palindrome)-1
        while left <= right:
            if palindrome[left] == palindrome[right]:
                left += 1
                right -= 1
            else:
                return False
        return True